import random


async def randomInt(message):
    words = message.content.split()
    if len(words) == 1:
        await message.channel.send(
            "E os números, fella?\n.!random <número> <número>\nSe colocar apenas um, escolho entre 1 e tal número."
        )
    elif len(words) >= 3:
        n1 = int(message.content.split()[1])
        n2 = int(message.content.split()[2])

        if n1 > n2:
            await message.channel.send(
                "O primeiro número tem que ser menor que o segundo!")

        choosen = random.randint(n1, n2)
        await message.channel.send(f"De {n1} até {n2}...")
        await message.channel.send(
            random.choice([
                f"Acho que {choosen} é um número bom...", f"Talvez {choosen}?",
                f"E se {choosen} fosse o certo?",
                f"Definitivamente {choosen}.", f"{choosen}",
                f"{choosen}, por favor.", f"Não sei... {choosen}?"
            ]))
    else:
        n1 = int(message.content.split()[1])
        if n1 == 0:
            await message.channel.send("De 0 até 0..., eu escolho 0.")

        choosen = random.randint(1, n1)
        await message.channel.send(f"De 1 até {n1}...")
        await message.channel.send(
            random.choice([
                f"Acho que {choosen} é um número bom...", f"Talvez {choosen}?",
                f"E se {choosen} fosse o certo?",
                f"Definitivamente {choosen}.", f"{choosen}",
                f"{choosen}, por favor.", f"Não sei... {choosen}?"
            ]))
