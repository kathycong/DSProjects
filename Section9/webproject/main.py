# Learning how to use web py
# its a web framework for python

#to install webpy use the instructions from this repo https://github.com/webpy/webpy
#python3 -m pip install web.py==0.62

import web

urls = (
    '/(.*)/(.*)', 'index'
)

#telling python where to find our template

render = web.template.render("resources/")
#this is how we instantiate
app = web.application(urls, globals())
class index:
    def GET(self, name, age):
        #to return something use this comand
        return render.main(name, age)

if __name__ == "__main__":
    app.run()