import smtplib
from email.mime.text import MIMEText

# Email details
sender_email = "thedarknessnetworktesting@gmail.com"
receiver_email = "dre.fabre@gmail.com"
password = r"Th3D@Rkn3$$!!##%%&&(("

# Create the email account
subject = "Test Email"
body = "This is a test email sent via Gmail SMTP Server"
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect to Gmail SMTP Server
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # Upgrade to a secure connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")

