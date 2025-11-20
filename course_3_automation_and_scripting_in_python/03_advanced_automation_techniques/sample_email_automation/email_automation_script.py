import smtplib
from email.mime.text import MIMEText
import imaplib

# Setup for email connection
smtp_server = "smtp.example.com"
smtp_port = 587
imap_server = "imap.example.com"
imap_port = 993
email_user = "orders@example.com"
email_password = "Coursera1000!"


def send_confirmation_email(client_email, client_name):
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(email_user, email_password)

            # create the message to be sent
            message = MIMEText(f"Thank you for your order, {client_name}!")
            message['Subject'] = "Order Confirmation"
            message['From'] = email_user
            message['To'] = client_email

            server.send_message(message)
            print(f"Sent confirmation email to {client_name}")
    except Exception as e:
        print(f"Error sending email: {e}")


def check_new_messages(client_email, client_name):
    try:
        with imaplib.IMAP4_SSL(imap_server, imap_port) as mail:
            mail.login(email_user, email_password)
            mail.select('inbox')

            status, responses = mail.search(None, '(UNSEEN FROM "%s")' % client_email)

            if status == "OK" and responses:
                raw_response = responses[0]
                if isinstance(raw_response, list):
                    raw_response = raw_response[0]

                mail_ids = raw_response.split() if isinstance(raw_response, bytes) else []
                if mail_ids:
                    print(f"{len(mail_ids)} new unread message(s) from {client_name}")
                    for num in mail_ids:

                        if not hasattr(mail, "fetch"):
                            print(f"Simulated fetch for email ID {num.decode()} (mock environment)")
                            continue
                        status, data = mail.fetch(num, "(RFC822)")
                        if status == "OK":
                            print(f"Fetched unread email ID {num.decode()}")

                else:
                    print(f"No new unread messages from {client_name}.")
            else:
                print("Error searching for unread emails")
    except Exception as e:
        print(f"Error fetching emails: {e}")


# Example usage
client_email = "john.smith@example.com"
client_name = "John Smith"
send_confirmation_email(client_email, client_name)
check_new_messages(client_email, client_name)