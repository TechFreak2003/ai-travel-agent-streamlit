import openai
from openai.error import RateLimitError
import os
from agents.tools.flights_finder import find_flights
from agents.tools.hotels_finder import find_hotels

def call_openai_agent(user_input, openai_key):
    openai.api_key = openai_key

    tools = [
        {
            "type": "function",
            "function": {
                "name": "find_flights",
                "description": "Search for flights between two cities on a specific date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {"type": "string", "description": "Departure city"},
                        "destination": {"type": "string", "description": "Arrival city"},
                        "date": {"type": "string", "description": "Travel date (YYYY-MM-DD)"},
                    },
                    "required": ["origin", "destination", "date"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "find_hotels",
                "description": "Search for hotels in a given city for specific dates",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name"},
                        "check_in": {"type": "string", "description": "Check-in date (YYYY-MM-DD)"},
                        "check_out": {"type": "string", "description": "Check-out date (YYYY-MM-DD)"},
                    },
                    "required": ["city", "check_in", "check_out"],
                },
            },
        },
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a helpful travel agent who helps users book flights and hotels."},
                {"role": "user", "content": user_input},
            ],
            tools=tools,
            tool_choice="auto",
        )

        message = response["choices"][0]["message"]

        # If OpenAI recommends a function call
        if message.get("tool_calls"):
            tool_call = message["tool_calls"][0]
            function_name = tool_call["function"]["name"]
            arguments = eval(tool_call["function"]["arguments"])  # you can also use `json.loads(...)`

            if function_name == "find_flights":
                return find_flights(**arguments)
            elif function_name == "find_hotels":
                return find_hotels(**arguments)

        # Otherwise return the assistant's reply
        return message["content"]

    except RateLimitError:
        return "⚠️ Rate limit exceeded! Please check your OpenAI plan and quota."

    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

