# Android Unlock Event Notification with Flask-Mail and MacroDroid

## Overview

This project, authored by Er. Waqar Wani (Vickywaqar111@gmail.com), demonstrates how to set up an Android device to send email notifications whenever the device is unlocked. It uses Flask-Mail as the email-sending component on a Flask server and MacroDroid for Android automation to trigger the email notification.

## Components

- Flask server with Flask-Mail for email sending.
- MacroDroid app for Android automation.

## Prerequisites

1. Python installed on your computer.
2. Flask and Flask-Mail Python packages installed.
3. MacroDroid app installed on your Android device.
4. Ngrok or a similar service for exposing your Flask server to the internet.

## Flask Server Setup

### 1. Install Required Python Packages

Open a terminal and install the required Python packages:

```bash
pip install Flask Flask-Mail
```

### 2. Set Up Flask-Mail Configuration

In your Flask server script (`app.py`), configure Flask-Mail with your Gmail account details:

```python
# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'
app.config['MAIL_SUPPRESS_SEND'] = False
```

### 3. Set Up Flask Route for Lock/Unlock Events

Add a route in your Flask script to handle lock/unlock events:

```python
from flask import Flask, request
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)
mail = Mail(app)

@app.route('/', methods=['POST'])
def handle_lock_unlock_event():
    send_email()
    return 'Lock/Unlock event handled successfully!'

def send_email():
    subject = 'Unlock Event Notification'
    recipient = 'recipient_email@gmail.com'
    
    unlock_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    message_body = f'Hello,\n\nYour Android device was unlocked at {unlock_time}.\n\nThis is a notification from Flask-Mail.'
    
    msg = Message(subject=subject, recipients=[recipient], body=message_body)
    
    try:
        mail.send(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 4. Run Flask Server

Run your Flask server:

```bash
python app.py
```

## MacroDroid Setup

### 1. Create Macro in MacroDroid

1. Open the MacroDroid app on your Android device.
2. Tap on the "+" button to create a new macro.
3. Add a "Screen Unlocked" trigger.
4. Add an "HTTP Request" action:
   - Set the Server URL to your ngrok or public Flask server URL.
   - Set the Method to "POST."
   - Set the Content Type to "application/x-www-form-urlencoded."
5. Save the macro.

### 2. Test the Setup

1. Lock and unlock your Android device.
2. Check the Flask server logs for successful handling of the lock/unlock event.
3. Check the recipient email for the unlock event notification.

## Conclusion

You have successfully set up an Android device to send email notifications using Flask-Mail and MacroDroid. This project can be expanded or customized based on your specific requirements.

---