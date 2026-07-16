import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file.")
    exit(1)

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

# Sample resume text for testing
RESUME_TEXT = """
John Doe
Software Engineer
Email: john.doe@email.com | 
Phone: (555) 123-4567

Summary: Experienced software engineer with 5 years of experience in full-stack development. 
Proficient in Python, JavaScript, React, and Node.js. Strong background in cloud computing (AWS, Azure).

Education:
- M.S. Computer Science, Stanford University (2018)
- B.S. Computer Engineering, MIT (2016)

Experience:
Senior Software Engineer | TechCorp Inc. (2021-Present)
- Led a team of 8 engineers building a microservices architecture
- Improved system performance by 40%
- Implemented CI/CD pipeline reducing deployment time by 60%

Software Engineer | CloudSolutions (2018-2021)
- Built RESTful APIs serving 1M+ requests daily
- Developed real-time data processing system
- Reduced infrastructure costs by 25%

Skills:
Programming: Python, JavaScript, Java, Go
Frontend: React, HTML, CSS, TypeScript
Backend: Node.js, Django, Spring Boot
Cloud: AWS (EC2, S3, Lambda), Azure, Docker, Kubernetes
Databases: PostgreSQL, MongoDB, Redis
Other: Git, CI/CD, Agile/Scrum, Microservices

Certifications:
- AWS Certified Solutions Architect (2022)
- Kubernetes Administrator (CKA) (2021)
"""

def call_gemini(prompt: str) -> str:
    """Helper function to call Gemini API"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"ERROR: {e}"

def save_results(results: dict):
    """Save results to a JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"results_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    return filename

def main():
    print("🔬 Prompt Engineering Lab")
    print("=" * 50)
    print("Task: Extract key information from a resume")
    print("Testing 4 prompting styles...\n")
    
    results = {}
    
    # 1️⃣ Zero-Shot Prompting
    print("1️⃣ Zero-Shot Prompting...")
    zero_shot_prompt = f"""
    Extract the following information from this resume and present it in a clear, organized format:
    
    1. Full Name
    2. Email
    3. Phone
    4. Education (degree, university, year)
    5. Work Experience (company, role, duration, key achievements)
    6. Skills (technical and soft skills)
    7. Certifications
    
    Resume:
    {RESUME_TEXT}
    """
    results["zero_shot"] = call_gemini(zero_shot_prompt)
    print("   ✅ Done")
    
    # 2️⃣ Few-Shot Prompting
    print("2️⃣ Few-Shot Prompting...")
    few_shot_prompt = f"""
    I need you to extract information from a resume in this exact format:
    
    Example 1:
    Full Name: Jane Smith
    Email: jane.smith@company.com
    Phone: (987) 654-3210
    Education: B.S. Computer Science, Harvard University, 2020
    Experience: Software Engineer, ABC Tech, 2020-2023; Built scalable microservices
    Skills: Python, Java, AWS, Docker
    Certifications: AWS Certified Developer (2021)
    
    Example 2:
    Full Name: Bob Johnson
    Email: bob.j@tech.com
    Phone: (456) 789-1234
    Education: Ph.D. AI, MIT, 2018
    Experience: ML Engineer, AI Corp, 2018-2024; Developed LLM applications
    Skills: Python, PyTorch, TensorFlow, NLP
    Certifications: Google Professional ML Engineer (2022)
    
    Now extract the same information from this resume:
    
    Resume:
    {RESUME_TEXT}
    
    Format your response exactly like the examples above.
    """
    results["few_shot"] = call_gemini(few_shot_prompt)
    print("   ✅ Done")
    
    # 3️⃣ Chain-of-Thought Prompting
    print("3️⃣ Chain-of-Thought Prompting...")
    cot_prompt = f"""
    Extract key information from this resume. Let me guide you step by step:
    
    Step 1: First, identify the person's full name, email, and phone number.
    Step 2: Then, look at education section. List each degree, university, and year.
    Step 3: Review work experience. For each job, note the company, role, dates, and main achievements.
    Step 4: Compile all technical and soft skills mentioned.
    Step 5: List any certifications with dates.
    
    Now apply these steps to this resume:
    
    Resume:
    {RESUME_TEXT}
    
    Show your reasoning for each step, then provide the final extracted information.
    """
    results["chain_of_thought"] = call_gemini(cot_prompt)
    print("   ✅ Done")
    
    # 4️⃣ Structured-JSON Output Prompting
    print("4️⃣ Structured-JSON Output Prompting...")
    json_prompt = f"""
    Extract the following information from the resume and output it as a valid JSON object:
    
    Required fields:
    - full_name (string)
    - email (string)
    - phone (string)
    - education (array of objects with: degree, university, year)
    - experience (array of objects with: company, role, duration, achievements)
    - skills (array of strings)
    - certifications (array of objects with: name, year)
    
    IMPORTANT: Your response MUST be valid JSON only. No additional text.
    
    Resume:
    {RESUME_TEXT}
    """
    results["structured_json"] = call_gemini(json_prompt)
    print("   ✅ Done")
    
    # Save results
    filename = save_results(results)
    print(f"\n📁 Results saved to: {filename}")
    print("\n✅ All prompts executed successfully!")
    print("📝 Now create RESULTS.md with your analysis and comparison.")

if __name__ == "__main__":
    main()