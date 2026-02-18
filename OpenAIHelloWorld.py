from openai import OpenAI
import os

class OpenAIHelloWorld:

    def __init__(self, user_input):
        self.user_input = user_input

    def process_input(self):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.responses.create(
            model="gpt-4.1-mini",
            input="Say Hello World to " + self.user_input
        )

        return response.output_text


print("Welcome to OpenAI")

name = input("Enter your name: ")

aqi = OpenAIHelloWorld(name)

result = aqi.process_input()

print(result)
