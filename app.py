from flask import Flask

app = Flask(__name__) #create Flask object

@app.route("/") #assigns fxn to run when root route requested
def hello_world():
    return "No hablo queso!"

    
if __name__ == "__main__":
    app.debug = True
    app.run()
