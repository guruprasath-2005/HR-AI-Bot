# HR AI Assistant

This project is a Python-based HR employee assistant that helps users search employee records, view employee details, and access related documents such as photos and official documents.

## Features

- Search employee details by Employee ID
- Display employee profile information
- Show employee photo
- Provide document download links for:
  - Aadhaar
  - PAN
  - 10th mark sheet
  - 12th mark sheet
  - Transfer Certificate
  - Degree
  - Experience certificate
- Include chatbot-style scripts that use an AI model for employee-related questions

## Project Structure

- `streamlit_app.py` - Main Streamlit web application
- `app/hr_chatbot.py` - Terminal-based HR chatbot using Ollama
- `app/chatbot.py` - Simple employee lookup chatbot
- `app/llm.py` - Basic LLM test script
- `app/open_document.py` - Helper to open employee files
- `employee.csv` - Employee dataset
- `Employee_Dataset_Synthetic_100/` - Employee documents and photos

## Technologies Used

- Python
- Streamlit
- pandas
- Ollama
- LangChain Ollama

## Setup

1. Create and activate a virtual environment
2. Install the required packages:
   ```bash
   pip install streamlit pandas langchain-ollama
   ```
3. Make sure Ollama is installed and running
4. Run the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Run Instructions

### Run the Streamlit app
```bash
streamlit run streamlit_app.py
```

### Run the chatbot script
```bash
python app/hr_chatbot.py
```

## Notes

- The app reads employee records from `employee.csv`
- Employee documents are stored under `Employee_Dataset_Synthetic_100/`
- The chatbot uses the `llama3` model through Ollama

## License

This project is for educational and demonstration purposes.
