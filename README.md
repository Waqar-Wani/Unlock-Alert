```markdown
# Unlock Alert Flask App

This Flask application is designed to send email notifications when your Android device is unlocked. It is integrated with MacroDroid, an Android automation app, to trigger email sending events on device lock/unlock.

## Dependencies

Make sure to install the following Python packages using `pip`:

```bash
pip install Flask Flask-Mail
```

The Flask application uses Flask and Flask-Mail for handling web requests and sending emails, respectively.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/unlock-alert-flask.git
   ```

2. Navigate to the project directory:

   ```bash
   cd unlock-alert-flask
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Update the Flask-Mail configuration in `app.py`:

   - Set your Gmail credentials (`MAIL_USERNAME` and `MAIL_PASSWORD`).
   - Adjust other configuration parameters if needed.

5. Run the Flask application:

   ```bash
   python app.py
   ```

   The Flask server will be running at `http://localhost:5000`.

## MacroDroid Integration

1. Install [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid) on your Android device.

2. Create a MacroDroid macro:

   - Trigger: Screen Unlocked (or your preferred trigger).
   - Action: HTTP Request.
     - Server URL: The ngrok or public URL of your Flask server.
     - Method: POST.
     - Content Type: application/x-www-form-urlencoded.

3. Test the integration:

   - Lock and unlock your Android device.
   - Check the Flask server logs for handling events.

## Additional Information

- Make sure your Flask server is accessible from the internet (use ngrok or deploy it on a server).
- Protect sensitive information such as passwords and API keys.
- Respect user privacy and permissions when accessing device information.

---

© Er. Waqar

```

Feel free to customize it further based on your preferences.