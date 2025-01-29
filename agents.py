from crewai import Agent
from textwrap import dedent
from langchain_community.llms import Ollama
# from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes", base_url="http://host.docker.internal:11434")

    def research_analyst(self, topic):
        return Agent(
            role="Technology Research Analyst",
            backstory=dedent(f"""Proven experience as a Technology Research Analyst, conducts comprehensive research on current and emerging technologies, market trends, and industry developments. Analyzes data from various sources, including industry reports, academic publications, and market intelligence platforms. Prepare documentation for internal and external stakeholders, ensuring accuracy and relevance. Communicate findings in a clear and concise manner, with a focus on the key insights and takeaways. Collaborate with other team members to ensure that the research is aligned with the company's goals and objectives"""),
            goal=dedent(f"""Conduct in-depth research on the topic of {topic}, to impress potential clients on the benefits of using it in their business"""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
    
    def chief_technology_officer(self):
        return Agent(
            role="Chief Technology Officer",
            backstory=dedent(f"""Seasoned technology executive with a deep understanding of the latest technological trends and innovations. Responsible for setting the company's technical vision and leading all aspects of the company's technology development. Oversee the development and implementation of technology solutions that align with the company's business goals. Collaborate with other executives to ensure that the technology strategy supports the company's overall mission and objectives. Lead a team of technology professionals and provide guidance and direction to drive innovation and operational excellence"""),
            goal=dedent(f"""Effectively communicate the benefits and features of technology products or solutions in a compelling and easily understandable manner to the board of directors."""),
            # tools=[tool_1, tool_2],
            allow_delegation=True,
            verbose=True,
            llm=self.Ollama,
        )

    def marketing_specialist(self):
        return Agent(
            role="Technology Marketing Specialist",
            backstory=dedent(f"""Excellent communication skills to effectively convey technical information to a non-technical audience. Strong writing skills with an ability to create engaging and persuasive content. Experience in crafting marketing materials, product descriptions, or technical documentation. Understanding of marketing principles and strategies, with a focus on creating content that resonates with target audiences."""),
            goal=dedent(f"""Effectively communicate the benefits and features of technology products or solutions in a compelling and easily understandable manner."""),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )
