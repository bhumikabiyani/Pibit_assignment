# Resume Parser

This Python script parses a resume and converts it into a structured JSON format using OpenAI's ChatGPT API.

## Requirements

- Python 3.6 or higher
- OpenAI Python client library

## Setup

1. **Install Dependencies**: Ensure you have the OpenAI client library installed. You can install it using pip:

    ```bash
    pip install openai
    ```

2. **API Key**: Obtain an API key from OpenAI and set it in the script. If you don't have an API key, you can get one by signing up on the [OpenAI website](https://beta.openai.com/signup/).

## Usage

1. **Script Configuration**: Open the `resume_parser.py` file and replace `'your-openai-api-key'` with your actual OpenAI API key.

2. **Provide Resume Content**: Update the `resume_content` variable with the resume text you want to parse.

3. **Run the Script**: Execute the script using Python:

    ```bash
    python resume_parser.py
    ```

4. **View Output**: The script will print the parsed resume in JSON format.

