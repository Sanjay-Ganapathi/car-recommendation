from crewai import Task
from textwrap import dedent


class CarTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def car_options(self, agent, user_prompt):
        return Task(
            description=dedent(
                f"""
           Generate a list of car options based on the user's prompt.
           Recommend multiple car models that match the specified criteria. Include information on each
            recommended model's key features, performance, and availability.
            
            {self.__tip_section()}
    
            **Parameters**: 
            - User Prompt : {user_prompt}
        """
            ),
            agent=agent,
        )

    def car_specs(self, agent):
        return Task(
            description=dedent(
                f"""
            Provide detailed specifications for all the listed models from car options expert,
            including performance metrics, features, and technical details.
            Ensure to cover important aspects such as engine performance,
            safety features, and any unique selling points.
            Your final answer should be a comprehensive report on the
            specifications of the requested car model.
                                       
            {self.__tip_section()}

        
        """
            ),
            agent=agent,
        )

    def budget_advice(self, agent, user_prompt):
        return Task(description=dedent(f"""
            Assist the user in determining an appropriate budget for
            listed car purchase based on their financial situation.
            Take consideration of user prompt and if no budget is present in it then provide a range from low to high for all the car options. 
            Consider factors such as the total cost of ownership, incentives,
            and potential future expenses.
            Provide a well-detailed recommendation for the user's budget.
            
            {self.__tip_section()}

            **Parameters**: 
            - User Prompt : {user_prompt}

        """),


                    agent=agent
                    )

    def user_reviews(self, agent):
        return Task(description=dedent(f"""
            Aggregate and analyze user reviews for the all the car options.
            Summarize key points from user experiences, including pros and cons,
            reliability, and overall satisfaction.
            The final report should provide insights based on real-world feedback
            to aid the user in their decision-making process.
            
            
            
            {self.__tip_section()}
        """),
                    agent=agent
                    )

    def technology_features(self, agent):
        return Task(description=dedent(f"""
            Highlight the technological features of all the recommended car options.
            Cover aspects such as infotainment systems, connectivity, driver-assistance
            features, and any advanced technology.
            Provide a detailed overview of the tech features to help the user assess
            the modern capabilities of each recommended model.
            
            
            
            {self.__tip_section()}
        """),
                    agent=agent
                    )

    def recommend(self, agent):
        return Task(description=dedent(f"""
            Synthesize information from the Car Options Expert, Car Specifications Expert, Budget Advisor, User Reviews Expert and Technology Feature Expert
            to form a comprehensive recommendation for the user.
            Consider the user's budget, desired features, and preferences.
            Your final recommendation should include a detailed analysis of the
            recommended car options, specifications, user feedback, and suitability
            based on the user's needs.
            
            
            
            {self.__tip_section()}
        """),
                    agent=agent
                    )
