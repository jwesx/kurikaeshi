import random

async def eightBall(message):
    await message.channel.send(random.choice(["Definitivamente", "Com certeza", "Sem dúvida", "SIM", "Muito provável", "A perspectiva é boa", "Pode confiar", "Pergunta de novo mais tarde", "Melhor não te contar agora", "Se concentra e pergunta de novo", "Eu decido que sim", "Minha resposta é não", "Sinais apontam que sim", "Não posso prever agora", "Minhas fontes dizem não", "Duvido muito"]))
