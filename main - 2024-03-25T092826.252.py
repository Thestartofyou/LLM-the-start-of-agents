import openai

# Set up your OpenAI API key
api_key = 'YOUR_API_KEY_HERE'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
openai.api_key = api_key

def generate_response(prompt):
    # Call the OpenAI API to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Specify the GPT-3 engine
        prompt=prompt,
        max_tokens=150  # Adjust the maximum number of tokens in the response as needed
    )
    return response.choices[0].text.strip()

# Example prompt
prompt = "What is the capital of France?"

# Generate a response using the LLM
response = generate_response(prompt)
print(response)
