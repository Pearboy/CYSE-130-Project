import smtplib
import psutil
from email.message import EmailMessage

email = 'cyse120demo@gmail.com' # demo gmail address
app_password = 'dlqu tfuq hsrz exff' # app password for gmail

# Function to send an alert email
def send_alert(subject, body):
    
    # Set up the email message (body, subject, from, to) 
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = email

    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, app_password) # Login with email and app password
        smtp.send_message(msg)

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get Memory usage
memory_info = psutil.virtual_memory()
print(f"Memory Usage: {memory_info.percent}%\n")

# Send an alert when CPU usage is high
if cpu_usage > 90:
    send_alert('High CPU Usage Alert', f'ALERT: CPU usage is high at {cpu_usage}%. Also, memory usage is {memory_info.percent}%.')
    print("Alert email sent successfully!")
