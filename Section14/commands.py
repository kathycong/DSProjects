import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancels = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            self.respond("My name is pie commander")
        else:
            self.respond("My name is python commander. How are you")
        
        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1] #take off the first word and split on the first space
            self.respond("Opening " + app)
            os.system("open -a" + app + ".app") #be able to launch any app


    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell = True)


