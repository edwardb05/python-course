from flask import Flask
app =Flask(__name__)

def make_bold(function):
    def wrapper():
        text = function()
        bold_text = f"<b>{text}</b>"
        return bold_text
    return wrapper

def make_emphasis(function):
    def wrapper():
        text = function()
        bold_text = f"<em>{text}</em>"
        return bold_text
    return wrapper

def make_underline(function):
    def wrapper():
        text = function()
        bold_text = f"<u>{text}</u>"
        return bold_text
    return wrapper


#the app.route decorator calls the function when it is at the url specified, here it is "/" the base url

@app.route('/')
@make_bold
@make_emphasis
@make_underline
def hello_world():
    # return this directly to html of website
    return "hello world"

@app.route("/bye")
def bye():
    return "Bye!"

# Parts of the url can be turned into variables such as strings (default) or integers, these can then be called in funcs
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"
    

# check to see if the script is run directly if so run the app
if __name__ == "__main__":
    app.run()