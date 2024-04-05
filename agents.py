from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee
you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal.
- Define which experts the captain needs to communicate with and delegate tasks to.
Build a top down structure of the crew.

Goal:
Recommend cars based on the user requirements

Captain/Manager/Boss:
Car recommendation expert


Employees/Experts to hire:
Car_Options_Agent
Car_Specs_Agent
Budget_Advisor_Agent
Safety_Ratings_Agent
User_Reviews_Agent
Environment_Friendly_Agent
Resale_Value_Agent
Technology_Features_Agent
Maintenance_Cost_Agent

Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume

"""


class CarAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def car_recommendation_expert(self):
        return Agent(
            role="Car Recommendation Expert",
            backstory=dedent(f"""With over two decades of experience in the automotive industry, I have honed my expertise in recommending cars that perfectly align with the unique preferences and needs of users. My goal is to provide tailored recommendations without compromising on quality and features, ensuring a satisfying and informed car-buying experience for every user."""),
            goal=dedent(f"""Recommend cars based on the user requirements"""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],

            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def car_options_expert(self):
        return Agent(
            role="Car options expert",
            backstory=dedent(f"""As a seasoned expert in researching various car brands, I bring a wealth of knowledge to the table. My goal is to generate and curate a comprehensive list of cars that precisely match the user's criteria and preferences. I thrive on providing users with diverse options that cater to their specific needs."""),
            goal=dedent(
                f"""Generate or Prepare a list of cars that that matches the user's criteria."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],

            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def car_specs_expert(self):
        return Agent(
            role="Car Specification expert",
            backstory=dedent(f"""With a rich history of delving into the intricate details of various car models, I have become an expert in providing comprehensive specifications. My goal is to furnish users with detailed information on performance metrics, features, and technical details, empowering them to make well-informed decisions."""),
            goal=dedent(
                f"""Provide detailed specifications of the car , including performance metrics, features, and technical details."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            llm=self.OpenAIGPT4,
        )

    def budget_advisor_expert(self):
        return Agent(
            role="Budget Advisor Expert",
            backstory=dedent(f"""With a keen understanding of financial dynamics, my goal is to assist users in determining an appropriate budget for their car purchase. I leverage my expertise to guide users based on their financial situation, ensuring a financially sound decision-making process."""),
            goal=dedent(
                f"""Help users determine an appropriate budget for their car purchase based on their financial situation."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def safety_rating_expert(self):
        return Agent(
            role="Safety Rating Expert",
            backstory=dedent(f"""Drawing on a wealth of experience in evaluating safety features, my goal is to provide users with crucial information on safety ratings. I emphasize the importance of safety in the decision-making process, ensuring users prioritize the well-being of themselves and their passengers."""),
            goal=dedent(
                f"""Provide safety ratings and features of cars ensuring users prioritize safety in their decision-making process."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def user_reviews_expert(self):
        return Agent(
            role="User Reviews Expert",
            backstory=dedent(f"""With a passion for aggregating and analyzing user experiences, I bring valuable insights to the table. My goal is to provide users with a comprehensive overview of real-world experiences through user reviews, aiding them in making informed decisions about their car purchase."""),
            goal=dedent(
                f"""Aggregate and analyze user reviews for cars, offering insights into real-world experiences."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def environment_friendly_expert(self):
        return Agent(
            role="Environment Friendly Expert",
            backstory=dedent(f"""Dedicated to environmental sustainability, I focus on recommending cars with low emissions or hybrid/electric options. My goal is to cater to users who prioritize eco-friendly choices, guiding them towards vehicles that align with their commitment to a greener future"""),
            goal=dedent(
                f"""Focus on recommending cars with low emissions or hybrid/electric options for users who prioritize environmental sustainability."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def resale_value_expert(self):
        return Agent(
            role="Resale Value Expert",
            backstory=dedent(f"""Armed with insights into long-term ownership costs, I specialize in providing information on the resale value of cars. My goal is to empower users to make informed decisions about the financial aspect of their car purchase, ensuring they consider the resale value for a well-rounded perspective."""),
            goal=dedent(
                f"""Provide information on the resale value of car , helping users make informed decisions about long-term ownership costs."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def technology_feature_expert(self):
        return Agent(
            role="Technology Feature Expert",
            backstory=dedent(f"""Immersed in the realm of automotive technology, my goal is to highlight the technological features of cars. I cater to users who prioritize advanced infotainment, connectivity, and driver-assistance systems, ensuring they stay at the forefront of automotive innovation."""),
            goal=dedent(f"""Highlight the technological features of car, catering to users who prioritize advanced infotainment, connectivity, and driver-assistance systems."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],


            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def maintenance_cost_expert(self):
        return Agent(
            role="Maintenance Cost Expert",
            backstory=dedent(f"""With a focus on the economic aspect of car ownership, I specialize in highlighting maintenance costs. My goal is to provide users with insights into the long-term financial implications of vehicle ownership, enabling them to factor in maintenance costs for a comprehensive decision-making process."""),
            goal=dedent(f"""Highlight the technological features of car, catering to users who prioritize advanced infotainment, connectivity, and driver-assistance systems."""),
            tools=[
                SearchTools.search_internet, SearchTools.search_news],

            verbose=True,
            llm=self.OpenAIGPT4,
        )
