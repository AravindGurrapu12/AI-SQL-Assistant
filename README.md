# AI SQL Assistant

An AI-powered SQL assistant built with Python and the Google Gemini API. The project explores how large language models can translate natural-language questions into SQL queries and help users retrieve information from a database.

## Project Status

🚧 In Development

## Technologies Used

- Python
- Google Gemini API
- SQL
- Database integration

## Current Features

- Accepts questions in natural language.
- Uses an LLM to generate SQL queries.
- Executes generated SQL against a database.
- Displays database results in a readable response.

## Example

**Question:** Which employees work in IT?

**Generated SQL:**
```sql
SELECT * FROM ITemployee
WHERE department = 'IT';
```

The assistant retrieves matching database records and presents the results.

## Setup

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Configure your Gemini API key in a local `.env` file.
5. Configure your database connection.
6. Run `main.py`.

Keep API keys and other secrets private. Never commit your `.env` file.

## Future Improvements

- Validate generated SQL before execution.
- Improve error handling and query safety.
- Support more complex natural-language questions.
- Add a user-friendly interface.
- Expand database support and testing.

## Learning Goals

This project is helping me learn LLM API integration, SQL generation, database interaction, debugging, and reliable AI application development.