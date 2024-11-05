# Website Blocker Flask App

A simple Flask application that allows users to block specific websites by modifying the system's hosts file. The application provides a user interface to enable or disable website blocking with password protection.

## Features

- Block or unblock specific websites (e.g., Facebook, YouTube).
- Password protection for enabling/disabling blocking.
- User-friendly web interface built with Flask and Tailwind CSS.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Python**: Programming language used to build the application.
- **HTML/CSS**: For creating the user interface, styled using Tailwind CSS.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jewkeynoh/website-blocker.git
   cd website-blocker
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:

   On Windows:
   ```bash
   ./venv/Scripts/activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. Install the required packages:
   ```bash
   pip install Flask
   ```

## Usage

1. Run the Flask application: Make sure to run the terminal as an administrator (required to modify the hosts file).
   ```bash
   python app.py
   ```
2. Open your browser: Navigate to http://127.0.0.1:5000 to access the application.

3. Block or Unblock Websites:
   - Enter the password to enable or disable website blocking.
   - The application will modify the hosts file to block or unblock specified websites.

## Configuration
You can modify the list of blocked websites by updating the BLOCKED_SITES variable in app.py.
Change the PASSWORD variable to set your desired password for enabling/disabling blocking.

## Important Notes
- The application modifies the system's hosts file, which requires administrative privileges. Make sure to run the Flask application in an environment that allows this.
- This application is meant for educational purposes and personal use. Use responsibly.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Thanks to the Flask community for their resources and documentation.
- Tailwind CSS for styling the application interface.

### Customization
- Replace `https://github.com/jewkeynoh/website-blocker` with the actual URL of your repository.
- Update the **Installation**, **Usage**, and **Configuration** sections as necessary to match your app's specifics.
- You can add more sections like **Contributing**, **Known Issues**, or **Contact Information** if relevant.

This `README.md` will provide users with a clear understanding of your application, how to set it up, and how to use it. Let me know if you need any further modifications or additional sections!
