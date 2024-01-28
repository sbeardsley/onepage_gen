from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def research(self, agent, topic):
        return Task(
            description=dedent(
                f"""Conduct in-depth research on the topic of {topic}. The information gathered will be used to assist a document writer in creating a comprehensive report. Please provide insights into the current state of the technology, recent advancements, key players in the industry, potential challenges, and any notable trends. Additionally, include relevant statistics, case studies, and future predictions.  Ensure that the information is accurate and up-to-date. Provide enough content to fill a 5-page report."""
            ),
            agent=agent,
        )

    def write_report(self, agent, topic):
        return Task(
            description=dedent(
                f"""You do not need any tools to do your task. Distill the comprehensive market research provided by the Technology Research Analyst into a concise and engaging 1-page technology summary tailored for potential customers. The document should be 300 to 500 words and include a brief introduction, key features, and use cases. The goal is to communicate the key insights, benefits, and market positioning of {topic} in a way that resonates with the target audience. Translate complex technical language into easily understandable terms for a non-technical audience. Ensure that jargon and technical details are presented in a way that emphasizes the customer benefits. Describe the benefits and use cases of {topic}, and how it can be applied in different industries. 
                
                Give 3 versions of the 1-page summary, each with a different tone and style."""
            ),
            agent=agent,
        )
