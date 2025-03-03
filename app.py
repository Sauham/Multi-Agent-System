import os
from crewai import Agent, Task, Crew
from langchain.tools import Tool
import streamlit as st

# Mock web search tool (replace with Tavily/Serper API if available)
def mock_web_search(query):
    return f"Mock results for '{query}': Sample data relevant to steel industry and ABC Steel."

web_search_tool = Tool(
    name="Web Search",
    func=mock_web_search,
    description="Search the web for industry trends, company info, or datasets."
)

# Define Agents
industry_research_agent = Agent(
    role="Industry Research Analyst",
    goal="Research the steel industry and ABC Steel's offerings.",
    backstory="Expert in market research.",
    tools=[web_search_tool],
    verbose=True
)

use_case_agent = Agent(
    role="AI Use Case Specialist",
    goal="Generate AI/GenAI use cases for ABC Steel.",
    backstory="Specialist in AI/ML applications.",
    tools=[web_search_tool],
    verbose=True
)

resource_agent = Agent(
    role="Resource Collector",
    goal="Find datasets/resources for proposed use cases.",
    backstory="Expert in sourcing datasets.",
    tools=[web_search_tool],
    verbose=True
)

proposal_agent = Agent(
    role="Proposal Writer",
    goal="Compile research, use cases, and resources into a proposal.",
    backstory="Skilled in report creation.",
    verbose=True
)

# Define Tasks
research_task = Task(
    description="Research ABC Steel and the steel industry, focusing on operations, supply chain, and customer experience.",
    agent=industry_research_agent,
    expected_output="A summary of ABC Steel's industry and key focus areas."
)

use_case_task = Task(
    description="Analyze steel industry trends and propose 5 AI/GenAI use cases for ABC Steel.",
    agent=use_case_agent,
    expected_output="A list of 5 AI/GenAI use cases with descriptions and benefits."
)

resource_task = Task(
    description="Search for datasets/resources relevant to the use cases (e.g., predictive maintenance, quality control).",
    agent=resource_agent,
    expected_output="A markdown section with clickable resource links."
)

proposal_task = Task(
    description="Compile research, use cases, and resources into a structured proposal for ABC Steel.",
    agent=proposal_agent,
    expected_output="A final report in markdown format."
)

# Create Crew
crew = Crew(
    agents=[industry_research_agent, use_case_agent, resource_agent, proposal_agent],
    tasks=[research_task, use_case_task, resource_task, proposal_task],
    verbose=2
)

# Streamlit UI
def main():
    st.title("AI Use Case Generator for ABC Steel")
    st.write("Enter a company name to generate an AI/GenAI use case proposal.")
    
    company = st.text_input("Company Name", "ABC Steel")
    if st.button("Generate Proposal"):
        with st.spinner("Generating proposal..."):
            result = crew.kickoff()
            st.markdown(result)
            # Save to file
            with open("proposal.md", "w") as f:
                f.write(result)
            with open("proposal.md", "r") as f:
                st.download_button(
                    label="Download Proposal",
                    data=f.read(),
                    file_name=f"{company}_proposal.md",
                    mime="text/markdown"
                )

if __name__ == "__main__":
    main()