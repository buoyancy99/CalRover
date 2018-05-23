import requests

def send_simple_message(msg):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox76f82e9317734baa8a4743209850e223.mailgun.org/messages",
        auth=("api", "key-d70816f5e70ec28acf95e4bd1746ae3f"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox76f82e9317734baa8a4743209850e223.mailgun.org>",
              "to": "Boyuan Chen <mentalchen@gmail.com>",
              "subject": "New email from robot",
              "text": msg})
