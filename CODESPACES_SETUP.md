# Codespaces Secrets Configuration
# 
# To use this project in GitHub Codespaces, you need to set up the following secrets:
#
# 1. Go to your GitHub repository
# 2. Click Settings → Secrets and variables → Codespaces
# 3. Add the following repository secrets:
#
# AZURE_OPENAI_API_KEY: Your Azure OpenAI API key
#
# These secrets will be automatically available as environment variables
# in your Codespaces environment.

# The devcontainer.json file will automatically:
# - Install Python 3.11
# - Install required Python packages
# - Set up VS Code extensions for Python development
# - Configure VS Code settings for optimal development experience

# Once the Codespace starts:
# 1. Copy .env.template to .env: cp .env.template .env  
# 2. Edit .env with your specific endpoint and deployment name
# 3. The API key will be automatically loaded from secrets
# 4. Run: python autogen_test.py
