#!/bin/bash

echo "🚀 Setting up LLM Evolution Workshop..."

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check Python version
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "✅ Python version: $python_version"

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Set up environment file
if [ ! -f ".env" ]; then
    echo "📝 Setting up environment file..."
    cp .env.template .env
    echo "⚠️  Please edit the .env file with your Azure OpenAI credentials:"
    echo "   - AZURE_OPENAI_ENDPOINT"
    echo "   - AZURE_OPENAI_API_KEY"
    echo "   - AZURE_OPENAI_LLM_DEPLOYMENT"
else
    echo "✅ Environment file already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your Azure OpenAI credentials"
echo "2. Run: python autogen_test.py"
echo ""
