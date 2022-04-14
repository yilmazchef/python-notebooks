# Het bruik van Mail APIs om emails te sturen

## MailGun

Om MailGun APIs te gebruiken moet u eerst naar mailgun.com inschrijven. Volg alle stappen om een API key te hebben zowel een email te sturen.

1. Schrijv u in naar het website
2. Activeer uw account via email link: Check your inbox for a "Please verify your Mailgun account" email, click the link, and you're done!
3. Start met email te sturen: To SMTP or API? That is the question. This guide can help you decide.
4. Ontvang better kwaliteit emails: Enhance your reputation by sending from a dedicated IP and use Mailgun's email validation service to make sure you have real email addresses from real people on your list.



```python
import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7f79f3598b5b44babe4a1a6154f6486d.mailgun.org/messages",
        auth=("api", "YOUR_MAIL_GUN_API_HERE"),
        data={"from": "Mailgun Sandbox <AUTO_GENERATED_SANDBOX_EMAIL_HERE>",
              "to": "Yilmaz Mustafa <chef@mail.be>",
              "subject": "Hello Yilmaz Mustafa",
              "text": "Congratulations Yilmaz Mustafa, you just sent an email with Mailgun!  You are truly awesome!"})

# You can see a record of this email in your logs: https://app.mailgun.com/app/logs.

# You can send up to 300 emails/day from this sandbox server.
# Next, you should add your own domain, so you can send 10000 emails/month for free.
```
