import os
from crewai import Crew
from textwrap import dedent
from agents import CarAgents
from tasks import CarTasks

from dotenv import load_dotenv
load_dotenv(".env")


class CarCrew:
    def __init__(self, prompt):
        self.prompt = prompt

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CarAgents()
        tasks = CarTasks()

        # Define your custom agents and tasks here
        car_options_expert = agents.car_options_expert()
        car_specs_expert = agents.car_specs_expert()
        budget_advisor_expert = agents.budget_advisor_expert()
        user_reviews_expert = agents.user_reviews_expert()
        technology_feature_expert = agents.technology_feature_expert()
        car_recommendation_expert = agents.car_recommendation_expert()

        # Custom tasks include agent name and variables as input
        car_options = tasks.car_options(
            car_options_expert,
            self.prompt,

        )

        car_specs = tasks.car_specs(
            car_specs_expert,
        )

        budget_advise = tasks.budget_advice(
            budget_advisor_expert,
            self.prompt
        )

        user_reviews = tasks.user_reviews(
            user_reviews_expert
        )

        technology_features = tasks.technology_features(
            technology_feature_expert
        )

        recommend = tasks.recommend(
            car_recommendation_expert
        )

        # Define your custom crew here
        crew = Crew(
            agents=[car_options_expert, car_specs_expert, budget_advisor_expert,
                    user_reviews_expert, technology_feature_expert, car_recommendation_expert],
            tasks=[car_options, car_specs, budget_advise,
                   user_reviews, technology_features, recommend],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("hey")
    print("""
          ## Welcome to Car Recommendation Agent .
          Please provide me with your preferences and requirements for a car, such as:
            - Your budget range.
            - Desired body type (sedan, SUV, coupe, etc.).
            - Preferred brand or specific models you are interested in.
            - Fuel efficiency or performance priorities.
            - Any specific features or requirements (e.g., safety features, technology, cargo space).
            Feel free to include any other details that are important to you in selecting a car.
           """)
    print("-------------------------------")
    prompt = input(dedent("""Enter your prompt """))

    car_crew = CarCrew(prompt)
    result = car_crew.run()
    print("\n\n########################")
    print("## Here are your recommendations :")
    print("########################\n")
    print(result)
