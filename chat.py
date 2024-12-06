import openai
from openai import OpenAI
import os

# Retrieve your OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)



assistant = client.beta.assistants.retrieve("asst_tO5ZZlAKF1ogX81dyrPH1Lqn")
#print(assistant)
print('\n')
# Create a thread
thread = client.beta.threads.create()
#print(thread.id)
print("\nType exit to quit\n")
while True:
    # Take input from user
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    # Create a message in the thread
    message = client.beta.threads.messages.create(
        #assistant_id = assistant.id,
        thread_id=thread.id,
        role="user",
        content=user_input
    )
    #print(message)
    # Run the assistant and poll for the result
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    #print (run)
    # Check the run status and print the assistant's response message
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_message = next(m.content[0].text.value for m in messages if m.role == "assistant")
        print(assistant_message)
    else:
        print(f"{run.status}")  
           




