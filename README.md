# LLM Evolution Workshop: Travel Assistant Journey 🗺️

A comprehensive workshop demonstrating the evolution of LLM applications from simple prompting to sophisticated multi-agent systems with Model Context Protocol (MCP) integration.

## 🎯 Workshop Overview

This workshop uses a **Travel Assistant** use case to showcase the progression of LLM applications through 5 distinct parts:

1. **Part 1: Simple LLM** - Basic travel recommendations using direct LLM calls
2. **Part 2: RAG Enhancement** - Knowledge-base powered suggestions with retrieval  
3. **Part 3: Single Agent with Tools** - Real-time data integration using external tools
4. **Part 4: Multi-Agent Collaboration** - Specialized agent coordination and teamwork
5. **Part 5: MCP Integration** - Enterprise-grade system integration with Model Context Protocol

## 🛠️ Technology Stack

- **Framework**: AutoGen 0.4+ (Latest stable)
- **LLM**: GitHub Models (GPT-4o-mini) - Free access to OpenAI models
- **Language**: Python 3.9+
- **Architecture**: Event-driven agents with publish-subscribe patterns
- **RAG**: TF-IDF vectorization with cosine similarity
- **MCP**: Model Context Protocol for enterprise integration

## � Prerequisites

Before you begin, you'll need:

- **Python 3.9+** installed
- **GitHub account** and **GitHub Personal Access Token** (Classic)
- **Basic Python knowledge**
- **Understanding of LLM concepts**

### Getting GitHub Models Access

1. Go to [GitHub Models](https://github.com/marketplace/models)
2. Sign in with your GitHub account
3. Generate a **Personal Access Token (Classic)** with appropriate permissions
4. You'll use this token as your `GITHUB_TOKEN` environment variable

> **Note**: GitHub Models provides free access to popular LLMs including GPT-4o-mini, Claude, and Llama models.

## �🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/nadeemazaizah/llm-evolution-workshop.git
cd llm-evolution-workshop
```

### 2. Set Up Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys
Create a `.env` file in the root directory:

```bash
# Copy example and edit
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux
```

Edit `.env` file:
```env
# GitHub Models API Key (required for all parts)
GITHUB_TOKEN=your_github_personal_access_token_here
```

### 4. Run Workshop Parts

Each part can be run independently:

```bash
# Part 1: Simple LLM
python src/part1_simple_llm/simple_travel_assistant.py

# Part 2: RAG Enhancement
python src/part2_rag/rag_travel_assistant.py

# Part 3: Single Agent with Tools
python src/part3_single_agent/single_agent_tools.py

# Part 4: Multi-Agent System
python src/part4_multi_agent/multi_agent_system.py

# Part 5: MCP Integration
python src/part5_mcp/mcp_integrated_autogen.py
```

## 📚 Workshop Structure
## 📚 Workshop Structure

### Part 1: Simple LLM
**Goal**: Understand baseline capabilities and limitations

- Basic travel recommendation function using GitHub Models
- Direct LLM API calls with simple prompts
- **Limitations**: No memory, no real-time data, generic responses
- **File**: `src/part1_simple_llm/simple_travel_assistant.py`

```python
# Example: Basic prompting
def get_travel_advice(user_query):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_query}]
    )
```

### Part 2: RAG Enhancement 
**Goal**: Add contextual knowledge and improve responses

- Travel knowledge base with destinations, attractions, cuisine
- TF-IDF vectorization for contextual retrieval
- **Improvements**: Specific venues, seasonal awareness, cultural tips
- **Files**: `src/part2_rag/rag_travel_assistant.py`, `src/part2_rag/rag/`

```python
# Example: RAG-enhanced planning
destinations = load_travel_data()
relevant_destinations = find_relevant_destinations(user_query, destinations)
enhanced_response = get_rag_enhanced_advice(user_query)
```

### Part 3: Single Agent with Tools
**Goal**: Integrate real-time data and external APIs

- Weather information for forecast-aware planning
- Flight search with mock pricing and availability  
- Currency conversion for budget planning
- **File**: `src/part3_single_agent/single_agent_tools.py`
- **Tools**: `src/part3_single_agent/tools/`

```python
# Example: Tool-enabled agent
agent = AssistantAgent(
    "travel_agent",
    model_client=model_client,
    tools=[get_weather_info, search_flights, convert_currency],
)
```

### Part 4: Multi-Agent Collaboration
**Goal**: Demonstrate specialization and coordination

**Specialized Agents**:
- **Flight Specialist**: Airline comparisons, route optimization
- **Budget Manager**: Cost optimization, expense tracking  
- **Travel Coordinator**: Plan synthesis and quality assurance

- **File**: `src/part4_multi_agent/multi_agent_system.py`

```python
# Example: Multi-agent system
team = SelectorGroupChat([flight_agent, budget_agent, coordinator_agent])
result = await Console(team.run_stream(task="Plan a trip to Tokyo"))
```

### Part 5: MCP Integration
**Goal**: Enterprise-grade scalability and system integration

**MCP Features**:
- **MCP Server**: FastMCP server with travel tools
- **Tool Integration**: Seamless tool access through MCP protocol
- **Scalability**: Enterprise-ready architecture

- **Files**: `src/part5_mcp/mcp_integrated_autogen.py`, `src/part5_mcp/mcp_server.py`

```python
# Example: MCP-integrated system
tools = mcp_server_tools(StdioServerParams(command="python", args=[mcp_server_path]))
agent = AssistantAgent("mcp_agent", model_client=model_client, tools=tools)
```

## 🎓 Learning Objectives

By the end of this workshop, you'll understand:

- **Evolution Path**: When and why to use each approach
- **AutoGen Framework**: Event-driven agent architecture  
- **Multi-Agent Patterns**: Specialization and coordination
- **Integration Strategies**: Tools, APIs, and MCP protocols
- **Production Considerations**: Scalability and maintainability
- **GitHub Models**: Free access to enterprise-grade LLMs

## 📊 Comparison Matrix

| Approach | Speed | Expertise | Coverage | Quality | Scalability |
|----------|-------|-----------|----------|---------|-------------|
| Simple Prompting | ⚡ Fast | 📚 General | ✅ Basic | 👍 Good | ❌ Limited |
| RAG Enhanced | 🔄 Moderate | 📊 Contextual | ✅ Better | ⭐ Improved | 🔧 Moderate |
| Single Agent + Tools | ⏱️ Dynamic | 🛠️ Capable | 🎯 Comprehensive | 🏆 High | 📈 Good |
| Multi-Agent | 🤝 Collaborative | 🎯 Specialized | ⭐ Excellent | 💎 Superior | ✅ High |
| MCP Integrated | 🏢 Enterprise | 🔗 Connected | 🌐 Complete | 🏆 Production | 🚀 Massive |

## 📁 Project Structure

```
llm-evolution-workshop/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment template
├── LICENSE                             # MIT License
└── src/
    ├── part1_simple_llm/
    │   └── simple_travel_assistant.py  # Basic LLM prompting
    ├── part2_rag/
    │   ├── rag_travel_assistant.py     # RAG-enhanced assistant
    │   └── rag/
    │       ├── rag_retrieval.py        # TF-IDF retrieval logic
    │       └── travel_data.json        # Travel knowledge base
    ├── part3_single_agent/
    │   ├── single_agent_tools.py       # Tool-enabled agent
    │   └── tools/
    │       ├── weather_tool.py         # Weather information
    │       ├── flight_tool.py          # Flight search
    │       └── currency_tool.py        # Currency conversion
    ├── part4_multi_agent/
    │   └── multi_agent_system.py       # Multi-agent collaboration
    └── part5_mcp/
        ├── mcp_integrated_autogen.py   # MCP-integrated system
        └── mcp_server.py               # FastMCP server
```

## 🎯 Use Cases by Approach

**Choose Your Level**:

- **Simple Prompting**: Quick prototypes, static content, basic Q&A
- **RAG Enhancement**: Knowledge-intensive apps, documentation, context-aware responses
- **Single Agent + Tools**: Personal assistants, dynamic workflows, real-time data  
- **Multi-Agent**: Complex domains, enterprise applications, specialized expertise
- **MCP Integration**: Production systems, multi-tenant platforms, enterprise scale

## 🔧 Environment Variables

Create a `.env` file in the root directory:

```env
# Required: GitHub Personal Access Token for GitHub Models
GITHUB_TOKEN=your_github_personal_access_token_here

# Optional: For development and debugging
DEBUG=false
LOG_LEVEL=INFO
```

## � Important Notes

- **GitHub Models is Free**: No cost for using GPT-4o-mini and other models
- **Rate Limits**: GitHub Models has generous rate limits for development
- **Token Security**: Never commit your `.env` file or tokens to git
- **Python Version**: Requires Python 3.9+ for AutoGen 0.4 compatibility

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you're running from the correct directory
```bash
# Run from project root
cd llm-evolution-workshop
python src/part1_simple_llm/simple_travel_assistant.py
```

2. **GitHub Token Issues**: Ensure your token has proper permissions
3. **Package Conflicts**: Use a clean virtual environment
4. **AutoGen Version**: Make sure you have AutoGen 0.4+

### Getting Help

- Check the error messages for specific guidance
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify your `.env` file is properly configured
- Make sure you're using Python 3.9+

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## � Acknowledgments

- **Microsoft AutoGen Team** for the excellent framework
- **GitHub Models** for free access to enterprise LLMs
- **OpenAI** for powerful language models
- **Workshop participants** for feedback and improvements

## � Support

- **Issues**: [GitHub Issues](https://github.com/nadeemazaizah/llm-evolution-workshop/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nadeemazaizah/llm-evolution-workshop/discussions)

---

🌟 **Start your LLM evolution journey today!** 

Experience the power of GitHub Models with AutoGen - from simple prompts to enterprise-ready multi-agent systems, all with free access to state-of-the-art language models.
