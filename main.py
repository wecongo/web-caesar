from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG']=True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">{0}</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>

"""

@app.route("/", methods=['POST'])
def webEncrypt():

    toEncrypt = request.form['text']
    numRot= int(request.form['rot'])
    newMessage = encrypt(toEncrypt, numRot)
  
    return form.format(newMessage)

@app.route("/")
def index():
    return form

app.run()