import openai
import json

# Set up your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Define the resume content
resume_content = """
Bhumika Biyani

biyanibhumika121@gmail.com | linkedin.com/biyanibhumika121 | leetcode.com/bhumi121 | github.com/bhumikabiyani
Education
Lovely Professional University Jalandhar, Punjab
Bachelors of Technology in Computer Science and Engineering (AI-ML) Sep 2021 – Present
• Cumulative GPA : 8.47/10.0 (till 6th Sem)
• Expected Graduation by June 2025
• Relevant Coursework: Algorithms and Data Structure, Database Management System, Operating System, Computer
Network, Linear Algebra, Discrete Mathematics, Artificial Intelligence
St. Paul’s School Pali, Rajasthan, India
Senior Secondary School 2020 – 2021
• Percentage : 89%
St. Paul’s School Pali, Rajasthan, India
Secondary School 2018 – 2019
• Percentage : 93%
Projects
Music Recommendation System using Machine Learning June 2024
• Scraped Spotify data utilizing the WebAPI to compile a comprehensive dataset. Executed normalization, encoding,
and feature engineering to enhance data quality.
• Implemented content-based filtering techniques and trained a neural network model to deliver personalized music
recommendations.
• Designed the UI of the web app using Streamlit.
Shorts Extractor from long videos using LLM, NLP pipelines Dec 2023
• Implemented a project based on Large Language Models (LLM) and Python libraries to automate the creation of
short videos like youtube shorts from lengthy videos. It processes and extracts key highlights.
Resume ChatBot using LLM, Flask and Langchain Sep 2023
• Integrated an AI chatbot feature to my portfolio website. This chatbot creates a virtual representation of myself
using Flask and Langchain embeddings, and it possesses the ability to respond to any query, drawing upon the
extensive data I have compiled.
Fake News Prediction using Machine Learning July 2023
• By analyzing vast datasets of news articles, social media posts this model learns to identify patterns and characteristics
associated with fake news. It assigns a credibility score to news sources and articles, helping users make informed
decisions.
Churn Prediction using Logistic Regression Jan 2023
• Developed a robust model through Data Pre Processing, Data Analysis, Data Visualization and feature selection.
• Used logistic regression to identify at-risk customers. Evaluated and fine tuned model. Generated actionable insights.
Experience
Network18 Media and Investments Limited Live Project
Remote Nov 2023 – Feb 2024
• Worked with large data sets, trained and fine-tuned ML models, and utilized MS Excel for data analysis.
• Developed a tool to create news shorts from long news videos using Gemini API, LLM models, Assembly AI and
NLP pipelines. Learned and applied text preprocessing, vectorization, normalization and basics of neural networks.
Technical Skills
• Programming Languages and frameworks: Python, Java, Python - Flask, FastAPI, RestAPI
• Data Science and Machine Learning: Power BI, Data Science , Machine Learning, NLP Pipeline , Neural Networks,
Deep Learning Essentials, TensorFlow, MS Office, Statistics, Understanding of LLM models
• Database and Concepts: MySQL, MongoDB, Operating System, Computer Networks, Software Engineering
• Other Technologies: Power Platforms, Automation, Web Scrapping, Selenium, Data Structures and Algorithms
Achievements
• Certified as Advanced SQL Coder on HackerRank, it required strong proficiency in complex query formulation.
• Certified among Top 5% of Data Analytics Professionals by Pro5.ai after a comprehensive 3-hour assessment.
• Solved over 200 Data Structures and Algorithms (DSA) problems including all essential Data Structures.
• Completed 6 months Machine Learning and Data Science Program by GeeksForGeeks.
• Achieved 5-star rating in Python, Java and SQL coding on HackerRank and solved more than 170 problems.
• Achieved 2nd rank in Jugaad Hacks Hackathon.
"""

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
