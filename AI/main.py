import openai 
from api_secrets import API_KEY

openai.api_key = API_KEY

pergunta = "diga que isso é um teste"

response = openai.Completion.create(engine="text-davinci-001", prompt=pergunta, max_tokens=6)

print(response)