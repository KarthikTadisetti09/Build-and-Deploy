import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure your API key is set as an environment variable

# Sample context for the AI
code = """
Node.js app is in the node-app folder with a simple build command.
Python app is in the python-app folder with no dependencies.
Java app is in the java-app folder using Maven for builds.
"""

# Make a request to the OpenAI API to generate YAML
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"Generate a GitHub Actions YAML file for a CI/CD pipeline based on this code:\n{code}"}
    ]
)

# Save the generated YAML to the deploy.yml file
with open('.github/workflows/deploy.yml', 'w') as f:
    f.write(response.choices[0].message['content'])
