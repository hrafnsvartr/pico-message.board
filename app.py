from flask import Flask, request

app = Flask(__name__)

latest_message = "Hello from Pico!"

@app.route("/")
def home():
    return f"""
    <html>
    <head><title>Pico Board</title></head>
    <body style="font-family: Arial; max-width:600px; margin:40px auto;">
        <h2>Pico Message Board</h2>

        <form action="/set">
            <input name="msg" style="width:100%; font-size:20px;" placeholder="Type message here">
            <br><br>
            <button style="font-size:20px;">Send</button>
        </form>

        <h3>Current message:</h3>
        <p style="font-size:24px;">{latest_message}</p>
    </body>
    </html>
    """

@app.route("/set")
def set_message():
    global latest_message
    msg = request.args.get("msg", "")
    latest_message = msg
    print("New message:", msg)
    return "OK - updated"

@app.route("/message")
def get_message():
    return latest_message

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
