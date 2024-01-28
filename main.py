import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from config import Config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY
# os.environ["OPENAI_ORGANIZATION"] = Config.OPENAI_ORGANIZATION_ID


class CustomCrew:
    def __init__(self, topic):
        self.topic = topic

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        research_analyst = agents.research_analyst(self.topic)
        marketing_specialist = agents.marketing_specialist()

        # Custom tasks include agent name and variables as input
        do_research = tasks.research(
            research_analyst,
            self.topic,
        )

        write_the_report = tasks.write_report(
            marketing_specialist,
            self.topic
        )

        # Define your custom crew here
        crew = Crew(
            agents=[research_analyst, marketing_specialist],
            tasks=[do_research, write_the_report],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    topic = input(dedent("""Enter a topic: """))

    custom_crew = CustomCrew(topic)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
