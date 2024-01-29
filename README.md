# simple-chatbot
A chat bot made in Python that uses your own data.

# Libraries used
difflib, json, random

# Example usage:
- Edit the file named `chatbot_data.json` according to your own data.
- Crate an object `chatbot = ChatBot("chatbot_data.json", 0.6)`
  (chatbot_data.json is default data file path, 0.6 is default threshold for comparing words)
- Get the response by 0.6 threshold: `response = chatbot.getResponse("do u prefer cooking or eating out")`
