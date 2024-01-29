# simple-chatbot
Simple ChatBot made with Python

# Libraries used
difflib, json, random

# Example usage:
- Edit `chatbot_data.json` by your own choices.
- Crate an object: `chatbot = ChatBot("chatbot_data.json", 0.6)` (chatbot_data.json is default data file path, 0.6 is default threshold for comparing words)
- Get the response by 0.6 threshold: `response = chatbot.getResponse("do u prefer cooking or eating out")`
