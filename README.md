🧠 Knowledge Graph Generator using Gemma 3 & Ollama | Streamlit App

This Streamlit application extracts structured graph data (entities and relationships) from natural language text using LangChain and locally running Gemma 3 LLM via Ollama. The generated knowledge graph is visualized interactively using PyVis.

    🔁 This app is designed for those who want to generate knowledge graphs privately on their local machine without relying on cloud APIs like OpenAI.

✨ Features

    📁 Two input modes:
    • Upload .txt files
    • Type or paste text directly

    🧠 Uses LangChainExperimental’s LLMGraphTransformer to extract entities and relations

    🕸️ Interactive knowledge graph visualization (PyVis + vis.js)

    ⚙️ Drag, zoom, and hover on nodes/edges to explore insights

    🧩 Works fully offline using Gemma 3 or any other model compatible with Ollama

    🔧 Easily switch to models like LLaMA 3, Phi-2, or Qwen2 if system resources are low

🛠️ Installation
✅ Prerequisites

    Python 3.10 or higher

    Ollama installed and a model like gemma3, llama3, or phi4 pulled locally

    Download Ollama: https://ollama.com
    Pull a model:

ollama pull gemma:4b
# or use another:
ollama pull llama3

📦 Dependencies

Install all required packages using the provided file:

pip install -r requirements.txt

Main dependencies:

    langchain, langchain-experimental

    langchain-ollama (instead of langchain-openai)

    streamlit, python-dotenv

    pyvis (for visualizing the graph)

⚙️ Setup

    Clone the repository

git clone https://github.com/arshi9854/knowledge_graph_generator.git
cd knowledge_graph_generator

    Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows

    Run the app

streamlit run app.py

    Visit http://localhost:8501 to interact with the app.

🚀 Usage Instructions

    Choose input method:

        Upload a .txt file or

        Paste your custom text into the text box

    Click "Generate Knowledge Graph"

    Wait a few moments while the LLM processes the content

    Explore the generated graph:

        🔍 Drag nodes

        📌 Hover for metadata

        🎯 Zoom in/out

        🔎 Filter relevant relationships

🧠 How It Works

    Input text is passed to LangChainExperimental's LLMGraphTransformer

    Gemma 3 LLM, running locally via Ollama, generates a structured graph representation

    The graph data includes:

        Nodes (Entities: e.g., Person, Organization, Event)

        Edges (Relationships between entities)

    The result is rendered using PyVis, which gives a dynamic and intuitive knowledge graph

🤖 Models You Can Use

You can switch out gemma3 with any of the following models (installed via Ollama):
Model Name	Resource Usage	Ideal For
gemma3	🟠 Medium	Balanced reasoning & speed
llama3	🔴 High	Deep reasoning, richer output
phi4-mini-reasoning	🟢 Low	Lightweight setups
qwen2:7b	🔴 High	Complex document parsing

Edit generate_knowledge_graph.py and replace this line:

llm = Ollama(model="gemma3", temperature=0)

With another model from your local list.
📌 Screenshot

(Make sure to update this with your actual image)
