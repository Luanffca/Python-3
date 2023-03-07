import openai

openai.api_key = "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"

engines = openai.Engine.list()

# for engine in engines.data:
#     print(engine.id)  # imprimindo várias engines


question = ''' qual o seu sabor favorito de sorvete ? '''
answer = openai.Completion.create(engine='text-davinci-001', prompt=question,
                         max_tokens=1000)  # tokens são as "palavras mais relevantes"

print(answer)

# sumarização
question = ''' Você: O que você tem feito?
Amigo: Assistindo filmes antigos.
Você: Você assistiu alguma coisa interessante?
Amigo: '''
answer = openai.Completion.create(engine='text-davinci-001', prompt=question,
                         max_tokens=1000)  

print(answer)

answer = openai.Image.create(prompt='Desenhe rostos aterrorizados', n=4, size='512x512')
answer = openai.Image.create(prompt='Desenhe o fundo mais profundo do mar de forma mais realista', n=4, size='512x512')
answer = openai.Image.create(prompt='Desenhe um monstro feio', n=4, size='512x512')

print(answer)