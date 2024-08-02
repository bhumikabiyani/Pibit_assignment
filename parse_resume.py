import openai
import json

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Define the resume content
resume_content = input("Enter Resume Content: ")

# Define the function to parse resume content
def parse_resume(resume_text):
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=f"Parse the following resume into JSON format:\n\n{resume_text}",
        max_tokens=1500,
        temperature=0.2
    )
    return response.choices[0].text.strip()

# Parse the resume
parsed_json = parse_resume(resume_content)

# Convert the parsed JSON text to a Python dictionary
parsed_dict = json.loads(parsed_json)

# Print the formatted JSON
print(json.dumps(parsed_dict, indent=2))
