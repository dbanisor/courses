from twilio.rest import Client

TWILIO_SID = "AC57def140c35c777fe5706b4903c903e8"
TWILIO_AUTH_TOKEN = "116294150a8c9db20126507824ede5fb"
TWILIO_VIRTUAL_NUMBER = "+16204728973"
TWILIO_VERIFIED_NUMBER = "+40751512677"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)
