import openai
import os 

api_key = os.getenv("API_KEY") 

openai.api_key = api_key  # Replace with your key or use environment variables

def parse_tasks(user_input):
    prompt = f"""
    Extract tasks and due dates from the following text. 
    Return them as a JSON list with 'task', 'deadline' (if mentioned), and 'priority' (high/medium/low).
    
    Text:
    {user_input}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
