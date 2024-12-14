from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionPlantCareAdvice(Action):
    def name(self):
        return "action_plant_care_advice"

    def run(self, dispatcher, tracker, domain):
        plant_type = tracker.get_slot("plant_type")
        care_action = tracker.get_slot("care_action")

        advice = f"For {care_action} your {plant_type}, ensure you follow appropriate guidelines."
        dispatcher.utter_message(text=advice)

        return []

class ActionHandlePlantProblem(Action):
    def name(self):
        return "action_handle_plant_problem"

    def run(self, dispatcher, tracker, domain):
        plant_type = tracker.get_slot("plant_type")
        plant_problem = tracker.get_slot("plant_problem")

        advice = f"It seems like your {plant_type} is having {plant_problem}. Try adjusting water, light, or soil conditions."
        dispatcher.utter_message(text=advice)

        return []
