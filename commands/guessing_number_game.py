import random


async def guessing_number_game(client, message):
  words = message.content.split()
  if len(words) == 2:
    n = int(message.content.split()[1])
    secret_number = random.randint(1, n)
    
  elif len(words) == 3:
    n1 = int(message.content.split()[1])
    n2 = int(message.content.split()[2])
    secret_number = random.randint(n1, n2)
    
  else:
    secret_number = random.randint(1, 100)

  await message.channel.send('Adivinhe o número!')

  def check(m):
    return m.author == message.author and m.channel == message.channel

  while True:
    await message.channel.send('Tenta um número aí:')
    guess_msg = await client.wait_for('message', check=check)

    try:
      guess = int(guess_msg.content)
    except ValueError:
      await message.channel.send('Tem que ser número!\n')
      continue

    await message.channel.send(f'**{guess}**??')

    if guess < secret_number:
      await message.channel.send('Muito baixo!')
    elif guess > secret_number:
      await message.channel.send('Muito alto!')
    else:
      await message.channel.send('Acertou! 👏👏🥳🥳🎉🎉🎊🎊')
      break
