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
    

    def cto_task(self, agent, topic):
        return Task(
            description=dedent(
                f"""Work with the Technology Research Analyst and Technology Marketing Specialist to create a comprehensive report on the topic of {topic}. Use the information provided by the analyst to create a report that includes an executive summary, market overview, technology landscape, competitive analysis, and future predictions. Ensure that the report is well-structured, engaging, and informative. Use clear and concise language to communicate complex technical concepts to a non-technical board of directors. Provide insights and recommendations based on the research findings."""
            ),
            agent=agent,
        )
    

    def write_report(self, agent, audience, topic):
        return Task(
            description=dedent(
                f"""You do not need any tools to do your task. Distill the comprehensive market research provided by the Technology Research Analyst into a concise and engaging 1-page technology summary tailored for {audience}. The document should be 300 to 500 words and include a brief introduction, key features, and use cases. The goal is to communicate the key insights, benefits, and market positioning of {topic} in a way that resonates with the target audience. Translate complex technical language into easily understandable terms for a non-technical audience. Ensure that jargon and technical details are presented in a way that emphasizes the customer benefits. Describe the benefits and use cases of {topic}, and how it can be applied in different industries. 
                
                Give 3 versions of the 1-page summary, each with a different tone and style."""
            ),
            agent=agent,
        )
