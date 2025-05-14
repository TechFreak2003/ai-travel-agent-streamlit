import openai
from agents.tools.flights_finder import find_flights
from agents.tools.hotels_finder import find_hotels

def call_openai_agent(prompt, openai_api_key):
    openai.api_key = openai_api_key

    tools_info = """
    You can use the following tools:
    - To find flights, say: 'find flights to <destination>'
    - To find hotels, say: 'find hotels in <destination>'
    """

    if "find flights to" in prompt.lower():
        dest = prompt.split("to")[-1].strip()
        return find_flights(dest)
    elif "find hotels in" in prompt.lower():
        dest = prompt.split("in")[-1].strip()
        return find_hotels(dest)

    # Otherwise, ask GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful travel assistant."},
            {"role": "user", "content": prompt + tools_info}
        ]
    )
    return response['choices'][0]['message']['content']
