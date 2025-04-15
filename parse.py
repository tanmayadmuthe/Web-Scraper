from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import re

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise EnvironmentError("GOOGLE_API_KEY not found in environment. Please check your .env file.")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

# Prompt template
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize Gemini
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

def beautify_text(raw_text):
    # Add spacing before each project title
    raw_text = re.sub(r'(?<=\n)([A-Z][a-zA-Z0-9\s]+)\nProject type:', r'\n\n🔹 \1\nProject type:', raw_text)

    # Turn tags into bullets
    raw_text = re.sub(r'#\s*', '• ', raw_text)

    return raw_text.strip()


def parse_with_gemini(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed batch: {i} of {len(dom_chunks)}")

        # Extract just the content
        content = getattr(response, "content", "").strip()

        if content:
            pretty_content = beautify_text(content)
            parsed_results.append(pretty_content)

    return "\n\n---\n\n".join(parsed_results)
