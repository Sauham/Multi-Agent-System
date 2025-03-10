# AI Use Case Generator

## 📌 Project Overview
This project is an **AI Use Case Generator** that automates market research, AI/GenAI use case generation, and resource asset collection for companies. It is implemented using **CrewAI**, **LangChain**, and **Streamlit**, leveraging AI agents to analyze industry trends and propose AI applications.

---

## 🚀 Features
- **Industry Research**: Uses web search to analyze company/industry trends.
- **Use Case Generation**: AI-powered insights for AI/GenAI implementation.
- **Resource Collection**: Finds relevant datasets and assets.
- **Proposal Generation**: Creates a structured markdown report.
- **Streamlit UI**: Interactive web app for generating reports.

---

## 📂 Project Structure
```
📦 ai_use_case_generator
 ├── 📄 app.py  # Main Streamlit app
 ├── 📄 game.py  # Sample game implementation (not part of AI pipeline)
 ├── 📄 Dockerfile  # Containerization setup
 ├── 📄 requirements.txt  # Dependencies
 ├── 📄 README.md  # Project documentation
```

---

## 📌 Installation & Setup
1. **Clone the repository**:
   ```bash
   https://github.com/Sauham/Multi-Agent-System.git
   cd Multi-Agent-System
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

---

## 🐳 Docker Support
To run inside a Docker container:
1. **Build the image**:
   ```bash
   docker build -t ai-usecase-generator .
   ```
2. **Run the container**:
   ```bash
   docker run -p 8501:8501 ai-usecase-generator
   ```

---

## 🛠 Technologies Used
- **CrewAI**: Multi-agent AI automation.
- **LangChain**: LLM-based reasoning and AI tools.
- **Streamlit**: Web interface for user interaction.
- **Python**: Core programming language.

---

## 📜 License
This project is licensed under the **MIT License**.

