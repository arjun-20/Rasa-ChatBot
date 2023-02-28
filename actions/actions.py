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

# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import operator



class ActionAdd(Action):

    def name(self) -> Text:
        return "action_add"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the values of the number1 and number2 slots
        num1 = next(tracker.get_latest_entity_values("number1", None))
        num2 = next(tracker.get_latest_entity_values("number2", None))
        # print(number1)

        # # Add the numbers
        #result = operator.add(float(num1), float(num2))
        if num1 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the first number.")
        elif num2 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the second number.")
        else:
            result = float(num1) + float(num2)
            dispatcher.utter_message(f"The sum of {num1} and {num2} is {result}.")

        # Send the result back to the user
        #dispatcher.utter_message(text=f"The sum of {num1} and {num2} is {result}")

        return []


class ActionSubtract(Action):

    def name(self) -> Text:
        return "action_subtract"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the values of the number1 and number2 slots
        num1 = next(tracker.get_latest_entity_values("number1", None))
        num2 = next(tracker.get_latest_entity_values("number2", None))

        if num1 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the first number.")
        elif num2 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the second number.")
        else:
            if float(num1) > float(num2):
                result = float(num1) - float(num2)
            else:
                result = float(num2) - float(num1)

            dispatcher.utter_message(f"The difference of {num1} and {num2} is {result}.")

        return []


class ActionMultiply(Action):

    def name(self) -> Text:
        return "action_multiply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num1 = next(tracker.get_latest_entity_values("number1", None))
        num2 = next(tracker.get_latest_entity_values("number2", None))

        if num1 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the first number.")
        elif num2 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the second number.")
        else:
            result = float(num1) * float(num2)
            dispatcher.utter_message(f"The product of {num1} and {num2} is {result}.")

        return []


class ActionDivide(Action):

    def name(self) -> Text:
        return "action_divide"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        num1 = next(tracker.get_latest_entity_values("number1", None))
        num2 = next(tracker.get_latest_entity_values("number2", None))

        if num1 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the first number.")
        elif num2 is None:
            dispatcher.utter_message("I'm sorry, I didn't catch the second number.")
        else:
            result = float(num1) / float(num2)
            dispatcher.utter_message(f"The quotient of {num1} and {num2} is {result}.")

        return []



