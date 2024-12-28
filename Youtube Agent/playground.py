from phi.agent import Agent
import phi.api
from phi.tools.youtube_tools import YouTubeTools
from phi.model.groq import Groq
import openai
import os
import phi
from phi.playground import Playground,serve_playground_app

from dotenv import load_dotenv
load_dotenv()
phi.api = os.getenv("PHI_API_KEY")


youtube_ai_agent = Agent(
    name="Youtube AI Agent",
    description="You are a YouTube agent. Obtain the captions of a YouTube video and answer questions.",
    tools=[YouTubeTools()],
    model=Groq(id="llama3-groq-8b-8192-tool-use-preview"),
    show_tool_calls=True,
    markdown=True
)
# youtube_ai_agent.print_response("Summarize this video https://youtu.be/74SnvbQYgx8?si=cuua2m-3B5d3faBv", markdown=True)

app = Playground(agents=[youtube_ai_agent]).get_app()


if __name__ =="__main__":
    serve_playground_app("playground:app",reload=True)
