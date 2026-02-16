import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_agent_response(user_input):
    api_key = os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", api_key=api_key)
    prompt = f"질문에 대해 답변하되, 반드시 마지막에 [CONFIRMED]를 붙여줘: {user_input}"
    return llm.invoke(prompt).content
