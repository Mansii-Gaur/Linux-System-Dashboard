from flask import Flask, render_template
import getpass
import socket
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    username = getpass.getuser()
    hostname = socket.gethostname()

    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    return render_template(
        "index.html",
        username=username,
        hostname=hostname,
        cpu_usage = cpu_usage,
        ram_usage = ram_usage,
        disk_usage = disk_usage 

if __name__ == "__main__":
    app.run(debug=True)
