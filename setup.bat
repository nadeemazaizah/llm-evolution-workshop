@echo off
echo 🚀 Setting up LLM Evolution Workshop...

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.11 or higher.
    exit /b 1
)

:: Check Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set python_version=%%i
echo ✅ Python version: %python_version%

:: Install dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

:: Set up environment file
if not exist ".env" (
    echo 📝 Setting up environment file...
    copy .env.template .env
    echo ⚠️  Please edit the .env file with your Azure OpenAI credentials:
    echo    - AZURE_OPENAI_ENDPOINT
    echo    - AZURE_OPENAI_API_KEY
    echo    - AZURE_OPENAI_LLM_DEPLOYMENT
) else (
    echo ✅ Environment file already exists
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your Azure OpenAI credentials
echo 2. Run: python autogen_test.py
echo.
