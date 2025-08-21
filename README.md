# LLM Evolution Workshop

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
