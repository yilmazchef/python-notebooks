import time

import requests
import smtplib

from email.mime.text import MIMEText


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return self.first_name + " " + self.last_name


class Email:
    def __init__(self, sender, recipients, subject, content, attachments=None):
        self.sender = sender
        self.recipients = recipients
        self.subject = subject
        self.content = content
        self.attachments = attachments

    # You can see a record of this email in your logs: https://app.mailgun.com/app/logs.
    # You can send up to 300 emails/day from this sandbox server.
    # Next, you should add your own domain so you can send 10000 emails/month for free.
    def send_with_api(self):
        responses = {}
        for recipient in self.recipients:
            response = requests.post(
                "https://api.mailgun.net/v3/sandbox7f79f3598b5b44babe4a1a6154f6486d.mailgun.org/messages",
                auth=("api", "e916e6727e1172c0754ad3b6ce82003a-0677517f-6bc2e3c9"),
                data={
                    "from": f"{self.sender} <postmaster@sandbox7f79f3598b5b44babe4a1a6154f6486d.mailgun.org>",
                    "to": f"{recipient} <{recipient.email}>",
                    "subject": f"{self.subject}",
                    "text": f"{self.content}"})
            responses[recipient.email] = response

        return responses

    def send_with_smtp(self):
        responses = {}
        msg = MIMEText('Testing some Mailgun awesomness')
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        s = smtplib.SMTP('smtp.mailgun.org', 587)
        s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')

        for recipient in self.recipients:
            msg['To'] = recipient.email
            response = s.sendmail(msg['From'], recipient.email, msg.as_string())
            responses[recipient.email] = response

        s.quit()
        return responses


sender = User("Justin", "Bieber", "just@in.be")
recipients = [
    User("Nikola", "Tesla", "chef@mail.be"),  # we are using the same email for testing purposes.
    User("Marie", "Curie", "chef@mail.be"),  # we are using the same email for testing purposes.
    User("Albert", "Einstein", "chef@mail.be")  # we are using the same email for testing purposes.
]
email1 = Email(sender, recipients, "Hello MailGunAPI!", "This was awesome experience...!")

responses = email1.send_with_api()

for recipient, response in responses.items():
    sent = response.status_code == 200
    if sent:
        print(f"Recipient: {recipient}, status: the email is successfully sent.")
    else:
        print(f"Recipient: {recipient}, status: the email is failed to sent!")
