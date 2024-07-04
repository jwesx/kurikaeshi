import random

async def randomInt(n1, n2):
    choosen = [random.randint(n1, n2)]
    await message.channel.send(f"{random.choice[
        f"Acho que {choosen} é um número bom...",
        f"Talvez {choosen}?",
        f"E se {choosen} fosse o certo?",
        f"Definitivamente {choosen}.",
        f"{choosen}",
        f"{choosen}, por favor.",
        f"Não sei... {choosen}?"
    ]}")