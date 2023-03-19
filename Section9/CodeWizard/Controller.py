import web
urls = (
    '/', 'home'
)

app = web.application(urls, globals())

#Classes/Routes

class home:
    def GET(self):
        return render.Home()

#It Allows You to Execute Code When the File Runs as a Script, but Not When It's Imported as a Module. 
# For most practical purposes, you can think of the conditional block that you open with if __name__ == "__main__" 
# as a way to store code that should only run when your file is executed as a script. 
if __name__ == "__main__":
    app.run()