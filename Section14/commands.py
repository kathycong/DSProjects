import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancels = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond("My name is pie commander")
        else:
            self.respond("My name is python commander. How are you")

    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell = True)


