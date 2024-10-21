from config import TEMPERATURE_THRESHOLD, ALERT_EMAIL
import smtplib
from email.mime.text import MIMEText

def check_and_alert(weather_data):
    alerts = []
    for city, data in weather_data.items():
        temp = data['main']['temp']
        if temp > TEMPERATURE_THRESHOLD:
            alert_message = f"Alert: High temperature in {city}!"
            alerts.append(alert_message)
            send_email_alert("Weather Alert", alert_message)  # Send the email alert
    return {"alerts": alerts}

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_gmail_id'  # Replace with your email
    msg['To'] = ALERT_EMAIL

    try:
        # Use Gmail's SMTP server (replace with your email provider's server if different)
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()  # Upgrade to a secure connection
            s.login('your_gmail_id', 'your_app_password')  # Use an App Password or your email password
            s.send_message(msg)
            print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email alert: {e}")


