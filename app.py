import subprocess
import datetime
import os
import pytz
from flask import Flask, Response

app = Flask(__name__)

@app.route('/htop')
def htop():
    # 1. Your full name
    name = "Your Full Name Here"

    # 2. System username
    #    getlogin() might not always work depending on the environment, so you can also use os.environ.get("USER")
    try:
        username = os.getlogin()
    except:
        username = os.environ.get("USER", "unknown-user")

    # 3. Server Time in IST
    ist = datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%Y-%m-%d %H:%M:%S %Z")

    # 4. top output (one-shot)
    #    Note: 'htop' itself often requires an interactive terminal, so we use 'top -b -n 1'
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode()

    # Format the HTML response
    html_response = f"""
    <h1>/htop Endpoint</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist}</p>
    <pre>{top_output}</pre>
    """

    return Response(html_response, mimetype='text/html')

if __name__ == '__main__':
    # Run on port 5000, listening on all interfaces
    app.run(host='0.0.0.0', port=5000)
