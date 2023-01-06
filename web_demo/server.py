from flask import Flask, render_template, request
import database

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/users")
def users():
    result = database.list_users()
    return result

@app.route("/register")
def register():
    username = request.args["username"]
    password = request.args["password"]

    sucess = database.register_user(username, password)

    return f'{sucess[0]} has been registered'

@app.route("/price")
def price():
    # name = request.args["name"]
    item = request.args["item"]

    # if name == "justin" or name == "tim" or name == "bob":
    #     if item == "ham":
    #         return "Ham is $5. VIP Discount"
    #     elif item == "turkey":
    #         return "Turkey is $7. VIP Discount"
    # else:
    #     if item == "ham":
    #         return "Ham is $10."
    #     elif item == "turkey":
    #         return "Turkey is $14"



    # if item == "ham":
    #     return "Ham is $10."
    # elif item == "turkey":
    #     return "Turkey is $14"

    # return f'{item} not found'

    result = database.item_search(item)

    print(result)

    # return result

    return f'{result[0]} is {result[1]}'

app.run(port=3300, host="0.0.0.0", debug=True)