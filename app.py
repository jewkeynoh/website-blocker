import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"

# List of sites to block
BLOCKED_SITES = ["www.facebook.com", "www.youtube.com"]
REDIRECT_IP = "127.0.0.1"

# Determine the host file path based on the operating system
if os.name == 'nt':  # Windows
    HOSTS_FILE_PATH = r"C:\Windows\System32\drivers\etc\hosts"
else:  # Assume Unix-like (Linux or macOS)
    HOSTS_FILE_PATH = "/etc/hosts"

PASSWORD = "your_password"

def is_blocking_enabled():
    with open(HOSTS_FILE_PATH, "r") as file:
        content = file.read()
        return any(site in content for site in BLOCKED_SITES)

def toggle_blocking(enable=True):
    if enable:
        with open(HOSTS_FILE_PATH, "a") as file:
            for site in BLOCKED_SITES:
                file.write(f"{REDIRECT_IP} {site}\n")
    else:
        with open(HOSTS_FILE_PATH, "r+") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(site in line for site in BLOCKED_SITES):
                    file.write(line)
            file.truncate()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        action = request.form.get("action")
        password = request.form.get("password")
        if password == PASSWORD:
            if action == "block":
                toggle_blocking(True)
                flash("Blocking enabled", "success")
            elif action == "unblock":
                toggle_blocking(False)
                flash("Blocking disabled", "success")
        else:
            flash("Incorrect password", "error")
    return render_template("index.html", is_blocking=is_blocking_enabled())

if __name__ == "__main__":
    app.run(debug=True)
