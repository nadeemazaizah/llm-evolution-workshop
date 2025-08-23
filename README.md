# LLM Evolution Workshop: Travel Assistant Journey 🗺️

A comprehensive workshop demonstrating the evolution of LLM applications from simple prompting to sophisticated multi-agent systems with Model Context Protocol (MCP) integration.

## 🎯 Workshop Overview

This workshop uses a **Travel Assistant** use case to showcase the progression of LLM applications:

1. **Simple LLM Prompting** - Basic travel recommendations
2. **RAG Enhancement** - Knowledge-base powered suggestions  
3. **Single Agent with Tools** - Real-time data integration
4. **Multi-Agent Collaboration** - Specialized agent coordination
5. **MCP Integration** - Enterprise-grade system integration

## 🛠️ Technology Stack

- **Framework**: AutoGen 0.4+ (Latest stable)
- **LLM**: OpenAI GPT-4o-mini 
- **Language**: Python 3.9+
- **Architecture**: Event-driven agents with publish-subscribe patterns

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/nadeemazaizah/llm-evolution-workshop.git
cd llm-evolution-workshop
```

### 2. Set Up Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your OpenAI API key
OPENAI_API_KEY=your_actual_api_key_here
```

### 4. Run Workshop
```bash
# Check environment setup
python workshop_runner.py --check-env

# Run full workshop
python workshop_runner.py

# Run specific part
python workshop_runner.py --part 3

# Interactive mode
python workshop_runner.py --interactive
```

## 📚 Workshop Structure

### Part 1: Simple LLM Prompting (30 min)
**Goal**: Understand baseline capabilities and limitations

- Basic travel recommendation function
- Direct LLM API calls with simple prompts
- **Limitations**: No memory, no real-time data, generic responses

```python
# Example: Basic prompting
assistant = SimpleTravelAssistant()
plan = assistant.plan_trip("Paris", 3, "budget traveler")
```

### Part 2: RAG Enhancement (45 min)  
**Goal**: Add contextual knowledge and improve responses

- Travel knowledge base with destinations, attractions, cuisine
- Vector-based retrieval for contextual recommendations
- **Improvements**: Specific venues, seasonal awareness, cultural tips

```python
# Example: RAG-enhanced planning
rag_assistant = RAGTravelAssistant()
plan = rag_assistant.plan_trip_with_rag("Tokyo", 4, "spring", "culture focused")
```

### Part 3: Single Agent with Tools (60 min)
**Goal**: Integrate real-time data and external APIs

- Weather API for forecast-aware planning
- Flight search for current prices and availability  
- Hotel finder with real ratings and pricing
- Events API for local activities

```python
# Example: Tool-enabled agent
agent = ToolEnabledTravelAgent()
plan = agent.create_comprehensive_travel_plan(
    destination="Barcelona",
    origin="London", 
    budget=3500,
    departure_date="2024-03-15"
)
```

### Part 4: Multi-Agent Collaboration (75 min)
**Goal**: Demonstrate specialization and coordination

**Specialized Agents**:
- **Flight Specialist**: Airline comparisons, route optimization
- **Hotel Specialist**: Location analysis, amenities evaluation  
- **Activity Planner**: Itinerary creation, cultural experiences
- **Budget Manager**: Cost optimization, expense tracking
- **Coordinator**: Plan synthesis and quality assurance

```python
# Example: Multi-agent system
system = MultiAgentTravelSystem()
plan = system.plan_trip_collaborative(
    destination="Rome",
    origin="New York",
    budget=4000,
    preferences="art, architecture, cuisine"
)
```

### Part 5: MCP Integration (60 min)
**Goal**: Enterprise-grade scalability and system integration

**MCP Servers**:
- **travel-data**: Comprehensive destination database
- **pricing-api**: Real-time market pricing
- **content-cms**: Dynamic travel content
- **enterprise-travel**: Corporate policies and rates

```python
# Example: MCP-integrated enterprise planning
mcp_system = AdvancedMCPTravelSystem()
plan = mcp_system.create_enterprise_travel_plan(
    destination="Tokyo",
    traveler_profile={"role": "Senior Executive"},
    enterprise_requirements={"policy_compliance": True}
)
```

## 🎓 Learning Objectives

By the end of this workshop, you'll understand:

- **Evolution Path**: When and why to use each approach
- **AutoGen Framework**: Event-driven agent architecture  
- **Multi-Agent Patterns**: Specialization and coordination
- **Integration Strategies**: Tools, APIs, and MCP protocols
- **Production Considerations**: Scalability and maintainability

## 📊 Comparison Matrix

| Approach | Speed | Expertise | Coverage | Quality | Scalability |
|----------|-------|-----------|----------|---------|-------------|
| Simple Prompting | ⚡ Fast | 📚 General | ✅ Basic | 👍 Good | ❌ Limited |
| RAG Enhanced | 🔄 Moderate | 📊 Contextual | ✅ Better | ⭐ Improved | 🔧 Moderate |
| Single Agent + Tools | ⏱️ Dynamic | 🛠️ Capable | 🎯 Comprehensive | 🏆 High | 📈 Good |
| Multi-Agent | 🤝 Collaborative | 🎯 Specialized | ⭐ Excellent | 💎 Superior | ✅ High |
| MCP Integrated | 🏢 Enterprise | 🔗 Connected | 🌐 Complete | 🏆 Production | 🚀 Massive |

## 🛡️ Prerequisites

- **Python 3.9+** experience
- **Basic LLM knowledge** (prompting, APIs)
- **API integration** understanding
- **OpenAI API key** (required)

## 📁 Project Structure

```
llm-evolution-workshop/
├── README.md                          # This file
├── requirements.txt                   # Dependencies
├── workshop_runner.py                 # Main workshop script
├── workshop_plan.md                   # Detailed workshop guide
├── .env.example                       # Environment template
├── src/
│   ├── part1_simple_prompting/
│   │   └── simple_travel_assistant.py
│   ├── part2_rag_enhancement/  
│   │   └── rag_travel_assistant.py
│   ├── part3_single_agent_tools/
│   │   └── tool_enabled_agent.py
│   ├── part4_multi_agent_collaboration/
│   │   └── multi_agent_system.py
│   └── part5_mcp_integration/
│       └── mcp_integrated_system.py
```

## 🎯 Use Cases by Approach

**Choose Your Level**:

- **Simple Prompting**: Quick prototypes, static content
- **RAG Enhancement**: Knowledge-intensive apps, documentation
- **Single Agent + Tools**: Personal assistants, dynamic workflows  
- **Multi-Agent**: Complex domains, enterprise applications
- **MCP Integration**: Production systems, multi-tenant platforms

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Microsoft AutoGen Team** for the excellent framework
- **OpenAI** for powerful LLM APIs
- **Workshop participants** for feedback and improvements

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/nadeemazaizah/llm-evolution-workshop/issues)
- **Discussions**: [GitHub Discussions](https://github.com/nadeemazaizah/llm-evolution-workshop/discussions)
- **Email**: [Your contact email]

---

🌟 **Start your LLM evolution journey today!** 

Run `python workshop_runner.py` and discover how to build increasingly sophisticated AI agents.

From simple prompts to MCP-powered multi-agent systems, hands-on LLM development with AutoGen.

## 🚀 Quick Start

### Option 1: GitHub Codespaces (Recommended)

1. Click the green "Code" button on GitHub
2. Select "Codespaces" tab
3. Click "Create codespace on main"
4. Wait for the environment to set up automatically
5. Set up your environment variables (see below)

### Option 2: Local Development

1. Clone the repository:
```bash
git clone https://github.com/nadeemazaizah/llm-evolution-workshop.git
cd llm-evolution-workshop
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables (see below)

## 🔧 Environment Setup

1. Copy the environment template:
```bash
cp .env.template .env
```

2. Edit `.env` file with your Azure OpenAI credentials:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your_actual_api_key_here
AZURE_OPENAI_LLM_DEPLOYMENT=gpt-4o
AZURE_OPENAI_LLM_API_VERSION=2025-01-01-preview
```

### For GitHub Codespaces:
- Go to your GitHub repository settings
- Navigate to "Secrets and variables" → "Codespaces"
- Add a secret named `AZURE_OPENAI_API_KEY` with your actual API key

## 🏃‍♂️ Running the Demo

```bash
python autogen_test.py
```

## 📖 What This Demo Shows

The workshop demonstrates the evolution of LLM applications through three stages:

### Stage 1: Direct LLM Model Call
- Simple question-answer interaction
- No tools, no agents
- Basic LLM functionality

### Stage 2: LLM with Tools (Single Agent)
- Agent with mathematical tools
- Function calling capabilities
- Single agent workflow

### Stage 3: Team-based Multi-agent System
- Multiple specialized agents working together
- Round-robin conversation pattern
- Complex task completion with termination conditions

## 🛠 Key Technologies

- **AutoGen**: Multi-agent framework
- **Azure OpenAI**: LLM backend
- **Python**: Programming language
- **GitHub Codespaces**: Cloud development environment

## 📦 Dependencies

- `autogen-agentchat>=0.4.0`: Agent chat functionality
- `autogen-core>=0.4.0`: Core AutoGen components
- `autogen-ext>=0.4.0`: Extended AutoGen features
- `python-dotenv>=1.0.0`: Environment variable management

## 🔐 Security Notes

- Never commit your API keys to version control
- Use environment variables for sensitive information
- The `.env` file is ignored by git for security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the terms specified in the LICENSE file.
