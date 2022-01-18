from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["Post", "Get"])

def webhook():
    if request.method == "Get":
        return "h y"
    elif request.method == "Post":
        payload = request.json
        user_response = (payload['queryResult']['queryText'])
        bot_response = (payload['queryResult']['fulfillmentText'])
        if user_response or bot_response != "":
            print("User: " + user_response)
            print("Bot: " + bot_response)
        return "M R"
    else:
        print(request.data)
        return "200"

if __name__ == '__main__':
    app.run(debug=True)