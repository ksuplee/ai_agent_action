import os, time
from langchain_google_genai import ChatGoogleGenerativeAI

def get_agent_response(user_input):
    api_key = os.getenv("GOOGLE_API_KEY")
    print("API key exists?", bool(api_key))

    llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", api_key=api_key)
    prompt = f"질문에 대해 답변하되, 반드시 마지막에 [CONFIRMED]를 붙여줘: {user_input}"
    
    print("Calling Gemini...", time.strftime("%H:%M:%S"))
    out = llm.invoke(prompt)
    print("Returned!", time.strftime("%H:%M:%S"))
    # print(out.content)

    return out.content
    