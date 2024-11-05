import os
from flask import Flask, render_template, request, flash

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

PASSWORD = "admin123"

def is_running_on_pythonanywhere():
    """Check if the app is running on PythonAnywhere."""
    return 'PYTHONANYWHERE_DOMAIN' in os.environ

def is_blocking_enabled():
    """Check if blocking is currently enabled by reading the hosts file."""
    if not is_running_on_pythonanywhere():
        try:
            with open(HOSTS_FILE_PATH, "r") as file:
                content = file.read()
                return any(site in content for site in BLOCKED_SITES)
        except Exception as e:
            print(f"Error reading hosts file: {e}")
            return False
    # For restricted environments, just return False or mock the output
    return False

def toggle_blocking(enable=True):
    """Toggle blocking of the specified websites."""
    if not is_running_on_pythonanywhere():
        try:
            if enable:
                print("Attempting to block sites...")
                with open(HOSTS_FILE_PATH, "a") as file:
                    for site in BLOCKED_SITES:
                        file.write(f"{REDIRECT_IP} {site}\n")
                flash("Blocking enabled", "success")  # Flash success message
                print("Sites blocked successfully.")
            else:
                print("Attempting to unblock sites...")
                with open(HOSTS_FILE_PATH, "r+") as file:
                    lines = file.readlines()
                    file.seek(0)
                    for line in lines:
                        if not any(site in line for site in BLOCKED_SITES):
                            file.write(line)
                    file.truncate()
                flash("Blocking disabled", "success")  # Flash success message
                print("Sites unblocked successfully.")
        except PermissionError:
            flash("Permission denied: unable to modify the hosts file. Please run as Administrator.", "error")
        except Exception as e:
            flash(f"Error modifying hosts file: {e}", "error")
    else:
        # Simulated blocking for restricted environments
        if enable:
            flash("Simulated blocking enabled - not modifying hosts file", "info")
        else:
            flash("Simulated blocking disabled - not modifying hosts file", "info")

@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page and handle form submissions."""
    if request.method == "POST":
        action = request.form.get("action")
        password = request.form.get("password")
        if password == PASSWORD:
            if action == "block":
                toggle_blocking(True)
            elif action == "unblock":
                toggle_blocking(False)
        else:
            flash("Incorrect password", "error")
    return render_template("index.html", is_blocking=is_blocking_enabled())

if __name__ == "__main__":
    app.run(debug=True)
