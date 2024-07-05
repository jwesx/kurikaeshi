import random


async def randomInt(message):
    words = message.content.split()
    n1 = 1
    n2 = 1
    if len(words) == 1:
        await message.channel.send(
            "E os números, fella?\n.!random <número> <número>\nSe colocar apenas um, escolho entre 1 e tal número."
        )
        return
    elif len(words) == 3:
        n1 = int(message.content.split()[1])
        n2 = int(message.content.split()[2])

        if n1 > n2:
            await message.channel.send(
                "O primeiro número tem que ser menor que o segundo!")
    else:
        n2 = int(message.content.split()[1])
        if n2 == 0:
            await message.channel.send("De 0 até 0..., eu escolho 0.")

    choosen = random.randint(n1, n2)
    await message.channel.send(f"De {n1} até {n2}...")
    await message.channel.send(
        random.choice([
            f"Acho que **{choosen}** é um número bom...",
            f"Talvez **{choosen}**?", f"E se **{choosen}** fosse o certo?",
            f"Definitivamente **{choosen}**.", f"**{choosen}**.",
            f"**{choosen}**, por favor.", f"Não sei... **{choosen}**?"
        ]))
