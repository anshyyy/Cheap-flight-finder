from twilio.rest import Client

TWILIO_SID = "AC12a7c7332b2e85ed30413ade5535ddd3"
TWILIO_AUTH_TOKEN = "ee455bdffd162fc773fd9b3e45f8660a"
TWILIO_VIRTUAL_NUMBER = "+19842063537"
TWILIO_VERIFIED_NUMBER = "+917903553605"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)