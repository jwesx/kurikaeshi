import random


async def randomInt(message):
    n1 = int(message.content.split()[1])
    n2 = int(message.content.split()[2])

    choosen = random.randint(n1, n2)
    await message.channel.send(
        random.choice[f"Acho que {choosen} é um número bom...",
                      f"Talvez {choosen}?", f"E se {choosen} fosse o certo?",
                      f"Definitivamente {choosen}.", f"{choosen}",
                      f"{choosen}, por favor.", f"Não sei... {choosen}?"]
    )
