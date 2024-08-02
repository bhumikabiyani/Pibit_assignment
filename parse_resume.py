import json

def parse_resume(resume_text):
    # Simulated parsing logic for demonstration purposes
    parsed_data = {
        "Personal Information": {
            "Name": "John Doe",
            "Contact Information": {
                "Email": "john.doe@example.com",
                "Phone": "+1234567890",
                "LinkedIn": "https://www.linkedin.com/in/johndoe",
                "Address": "123 Main St, Anytown, USA"
            }
        },
        "Experience": [
            {
                "Company": "Network18 Media and Investments Limited",
                "Position": "Software Developer Intern",
                "StartDate": "November 2023",
                "EndDate": "February 2024",
                "Responsibilities": [
                    "Developed a tool to create news shorts from long news videos using Gemini API, LLM models, Assembly AI, and NLP pipelines.",
                    "Collaborated with the editorial team to improve video processing workflows."
                ]
            }
        ],
        "Education": [
            {
                "Degree": "Bachelor of Technology",
                "Major": "Computer Science",
                "University": "ABC University",
                "GraduationYear": "2022"
            }
        ],
        "Projects": [
            {
                "Title": "Music Recommendation System using Machine Learning",
                "Date": "June 2024",
                "Description": "Built a recommendation system to suggest music tracks based on user preferences using machine learning techniques."
            },
            {
                "Title": "Shorts Extractor from long videos using LLM, NLP pipelines",
                "Date": "December 2023",
                "Description": "Developed a pipeline to extract short clips from long videos using LLM and NLP techniques."
            }
        ],
        "Skills": [
            "Machine Learning",
            "Python",
            "Data Structures and Algorithms",
            "SQL",
            "NLP"
        ],
        "Certifications": [
            {
                "Title": "Certified Data Scientist",
                "Issuing Organization": "Data Science Academy",
                "Date": "July 2023"
            }
        ]
    }
    return parsed_data

if __name__ == "__main__":
    resume_text = """[Insert Resume Content Here]"""
    parsed_data = parse_resume(resume_text)
    print(json.dumps(parsed_data, indent=4))
