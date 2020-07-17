from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

# create a chatbot
chatbot = ChatBot('N4ruto')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

while True:
    query = str(input(">> "))
    print(chatbot.get_response(query))
    if "exit" in query:
        break

