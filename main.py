from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import resend

load_dotenv()

app = Flask(__name__)

resend.api_key = os.getenv('RESEND_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/stayup", methods=['POST'])
def process():
    params = {
      "from": "beta@krushkrypto.xyz",
      "to": [request.form['email']],
      "subject": "Thanks!",
      "html": render_template('email.html')
    }
    resend.Emails.send(params)
    return render_template('stayup.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
