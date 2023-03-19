# Learning how to use web py
# its a web framework for python

#to install webpy use the instructions from this repo https://github.com/webpy/webpy
#python3 -m pip install web.py==0.62

import web

urls = (
    '/(.*)', 'index'
)
#this is how we instantiate
app = web.application(urls, globals())
class index:
    def GET(self, name):
        #print("Hello", name, '. How are you today?')

        #to return something use this comand
        return "<h1>Hello" + name + '. </h1> How are you today?'

if __name__ == "__main__":
    app.run()