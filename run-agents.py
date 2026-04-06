from langchain.agents import Tool, initialize_agent
from langchain.llms import Ollama

# 1. Model lokalny
llm = Ollama(model="mistral")

# 2. Narzędzia (agent może nimi operować)
tools = [
    Tool(
        name="read_file",
        func=lambda filepath: open(filepath).read(),
        description="Read a file from the local project"
    ),
    Tool(
        name="run_test",
        func=lambda _: subprocess.run(["pytest"], capture_output=True).stdout.decode(),
        description="Run tests in the project"
    )
]

# 3. Agent
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# 4. Użycie
agent.run("Tell me someting about my gohugo project")