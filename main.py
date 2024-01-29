from chatbot import ChatBot

chatbot = ChatBot("chatbot_data.json", 0.6)

response = chatbot.getResponse("do u prefer cooking or eating out")
print(response)