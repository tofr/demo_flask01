from flask import Flask

app = Flask(__name__) #create Flask object

@app.route("/") #assigns fxn to run when root route requested
def hello_world():
    return "No hablo queso!"

    
if __name__ == "__main__": #true if run as script (not imported as module)
    app.debug = True #security risk!!! set to False if going live...
    app.run()
