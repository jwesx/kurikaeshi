async def helpMessage(message):
    await message.channel.send(
        f"Salve meu compatriota <@{message.author.id}>, tudo certo?\n\n" +
        "===================================\n\n" +
        "Por enquanto só tenho alguns comandos, mas vou estar adicionando mais e mais, conforme o tempo!\n"
        + "Eis eles aqui:\n\n" +
        "**• .!help** → esse mesmo que você acabou de usar!\n" +
        "**• .!random** {número} <número> → escolho um número aleatório entre os dois que você escolher (se me falar só um, vou a partir de 1)!\n"
        +
        "**• .!clear** <quantidade> → limpo as mensagens do canal, com a quantidade que você quiser!\n"
        +
        "**• .!8ball** <pergunta> → faça uma pergunta para mim, e eu te respondo!\n"
        +
        "**• .!dm** <@user> <mensagem> → envio uma mensagem direta para a pessoa.\n"
        +
        "**• .!guessnumber** {number} → jogue um jogo de adivinhar o número! Fique atento ao que eu mandar após sua tentativa.\n"
        +
        "**• .!giverole** <@user> <@role> → dá um cargo para a pessoa (mas não ta funcionando 😭)\n\n"
        +
        "Para melhor compreensão desse comando, os que estiverem entre <> são obrigatórios, e entre {} é opcional."
    )
