import difflib
import json
import random



class ChatBot:
    dataFile = None
    dataFilePath = "chatbot_data.json"
    cutoffValue = 0.6

    def __init__(self, dataFilePath, cutoffValue):
        self.dataFilePath = dataFilePath
        temp = open(dataFilePath)
        self.dataFile = json.load(temp)
        self.cutoffValue = cutoffValue

    def getResponse(self, questionText):
        for data in self.dataFile:
            if len(difflib.get_close_matches(questionText, data["questions"], 1, self.cutoffValue)) > 0:
                return data["answers"][random.randint(0, len(data["answers"]) - 1)]
        else:
            return "Sorry, I can not understand."
