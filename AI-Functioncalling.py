from openai import OpenAI
import json


# ==============================
# Azure OpenAI Configuration
# ==============================

API_KEY = ""

BASE_URL = ""

MODEL_NAME = "gpt-4.1"   # Your Azure deployment name


client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


# ==============================
# Agent Tool
# ==============================

def get_domino_server_status():

    # In real project:
    # This can call:
    # - Domino API
    # - SQL Database
    # - Monitoring tool
    # - REST API

    server_information = {
        "server_name": "DOMINO-PROD-01",
        "status": "Running",
        "users_connected": 450,
        "mail_queue": 5,
        "last_backup": "2026-07-29 02:00 AM"
    }

    return server_information



# ==============================
# Agent Logic
# ==============================

def run_agent(user_question):


    # Step 1:
    # Agent decides whether tool is required

    if "server" in user_question.lower() or \
       "domino" in user_question.lower():


        print("\nAgent Decision:")
        print("Need server information -> Calling Tool")


        # Step 2:
        # Tool execution

        tool_result = get_domino_server_status()


        # Step 3:
        # Send tool result to LLM

        prompt = f"""

        You are an IT support AI Agent.

        User Question:
        {user_question}


        Server Information:
        {json.dumps(tool_result, indent=2)}


        Explain the answer clearly.
        """


        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an intelligent IT agent."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )


        return response.choices[0].message.content



    else:

        # Normal LLM response

        response = client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role":"user",
                    "content":user_question
                }
            ]

        )


        return response.choices[0].message.content




# ==============================
# Chat Interface
# ==============================

print("==============================")
print(" Azure AI Agent Demo ")
print("==============================")


while True:

    question = input("\nAsk: ")


    if question.lower()=="exit":
        break


    answer = run_agent(question)


    print("\nAI Agent:")
    print(answer)