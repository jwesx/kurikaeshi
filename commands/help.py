async def helpMessage(message):
  await message.channel.send(
      f"Salve meu compatriota <@{message.author.id}>, tudo certo?" +
      
      "===================================" +
      
      "Por enquanto só tenho alguns comandos, mas vou estar adicionando mais e mais, conforme o tempo!" + 
      "Eis eles aqui:" +
      
      "**• .!help** → esse mesmo que você acabou de usar!" +
      "**• .!random** {número} <número> → escolho um número aleatório entre os dois que você escolher (se me falar só um, vou a partir de 1)!" +
      "**• .!clear** <quantidade> → limpo as mensagens do canal, com a quantidade que você quiser!" + 
      "**• .!8ball** <pergunta> → faça uma pergunta para mim, e eu te respondo!" +
      "**• .!dm** <@user> <mensagem> → envio uma mensagem direta para a pessoa." +
      "**• .!guessgame** {number} → jogue um jogo de adivinhar o número! Fique atento ao que eu mandar após sua tentativa." +

      "Para melhor compreensão desse comando, os que estiverem entre <> são obrigatórios, e entre {} é opcional."
  )
