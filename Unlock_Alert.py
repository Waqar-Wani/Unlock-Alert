from flask import Flask, request
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'waqarmaqbool@vasista.in'
app.config['MAIL_PASSWORD'] = 'waqar@786'  # Replace with your actual email password
app.config['MAIL_DEFAULT_SENDER'] = 'waqarmaqbool@vasista.in'
app.config['MAIL_SUPPRESS_SEND'] = False

mail = Mail(app)

@app.route('/', methods=['POST'])
def handle_lock_unlock_event():
    # Your logic to send emails or perform actions on lock/unlock event
    send_email()
    return 'Lock/Unlock event handled successfully!'

def send_email():
    subject = 'Unlock Event Notification'
    recipient = 'vickywaqar111@gmail.com '
    
    unlock_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    message_body = f'Hello,\n\nYour Android device was unlocked at Zalowa Char-i-Shareef at {unlock_time}.\n\nThis is a notification from Waqar phone.'
    
    msg = Message(subject=subject, recipients=[recipient], body=message_body)
    
    try:
        mail.send(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
