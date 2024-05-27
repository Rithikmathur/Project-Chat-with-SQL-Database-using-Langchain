from flask import Flask, jsonify
from chat_with_sql_script import ChatWithSQL

app = Flask(__name__)
obj = ChatWithSQL("root", "12345", "localhost", "ahi_database")

@app.route('/send-message', methods=['GET'])
def send_message():
    # message = "Hello, this is a message from the Flask API!"
    message = obj.message("How many tables do we have?")
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(debug=True)