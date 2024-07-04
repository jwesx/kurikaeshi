import random

import discord

responses = [
  "E aí!",
  "Fala!",
  "Oi, tudo sussa?",
  "Salve!", 
  "Tudo em cima?", 
  "Tranquilo?", 
  "Aê!",
  "E aí, brother!", 
  "Fala, galera!", 
  "Como tá?", 
  "O que de novo?", 
  "Blz?",
  "De boa?", 
  "Rolando tudo?", 
  "Como vai a vida?",
  "Tudo em ordem?", 
  "Tudo sussa?", 
  "Tudo tranquilo?",
  "O que tá acontecendo?", 
  "E o PodPah?", 
  "Pega a visão: meu pau na sua mão",
  "Viu Twitter hoje?", 
  "Precisa de mim?", 
  "PING! PONG!"
]


async def hello(message, client):
  randomResponse = random.choice(responses)

  if message.author == message.guild.me:
    return
  if client.user in message.mentions:
    await message.channel.send(randomResponse)
    if random.choice([0, 1]) == 1:
      await message.add_reaction(random.choice(['🔔', '📢']))
    else:
      return
