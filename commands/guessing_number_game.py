import random


async def guessing_number_game(client, message):
  n = int(message.content.split()[1])
  secret_number = random.randint(1, n)
  await message.channel.send('Guess the number!')

  if n is None:
    n = 100

  def check(m):
    return m.author == message.author and m.channel == message.channel

  while True:
    await message.channel.send('Please input your guess: ')
    guess_msg = await client.wait_for('message', check=check)

    try:
      guess = int(guess_msg.content)
    except ValueError:
      await message.channel.send('Should be a number!\n')
      continue

    await message.channel.send(f'You guessed: {guess}')

    if guess < secret_number:
      await message.channel.send('Too small!')
    elif guess > secret_number:
      await message.channel.send('Too big!')
    else:
      await message.channel.send('You win!')
      break
