# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAddToCart(Action):

    def name(self) -> Text:
        return "action_add_to_cart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flower_type = tracker.get_slot("flower_type")
        cart = tracker.get_slot("cart") or []
        cart.append(flower_type)
        dispatcher.utter_message(text=f"{flower_type} has been added to your cart.")
        return [SlotSet("cart", cart)]

class ActionCheckAvailability(Action):

    def name(self) -> Text:
        return "action_check_availability"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flower_type = tracker.get_slot("flower_type")
        available = flower_type.lower() != "tulips"
        if available:
            dispatcher.utter_message(text=f"{flower_type} is available.")
        else:
            dispatcher.utter_message(text=f"Sorry, we don't have {flower_type} at the moment.")
        return []

class ActionRemoveFromCart(Action):

    def name(self) -> Text:
        return "action_remove_from_cart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        flower_type = tracker.get_slot("flower_type")
        cart = tracker.get_slot("cart") or []
        if flower_type in cart:
            cart.remove(flower_type)
            dispatcher.utter_message(text=f"{flower_type} has been removed from your cart.")
        else:
            dispatcher.utter_message(text=f"{flower_type} is not in your cart.")
        return [SlotSet("cart", cart)]

class ActionShowCart(Action):

    def name(self) -> Text:
        return "action_show_cart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cart = tracker.get_slot("cart") or []
        if cart:
            cart_items = ", ".join(cart)
            dispatcher.utter_message(text=f"Here are the items in your cart: {cart_items}")
        else:
            dispatcher.utter_message(text="Your cart is empty.")
        return []

class ActionClearCart(Action):

    def name(self) -> Text:
        return "action_clear_cart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Your cart has been cleared.")
        return [SlotSet("cart", [])]
