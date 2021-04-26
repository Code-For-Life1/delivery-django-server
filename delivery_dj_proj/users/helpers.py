from .models import User, UnauthDriver
from .models import generateOTP
import environ
from twilio.rest import Client




env = environ.Env()
environ.Env.read_env()
twilio_client = Client(env('TWILIO_ACCOUNT_SID'), env('TWILIO_AUTH_TOKEN'))

def get_user_by_phone(phone_number):
    return User.objects.get(phone_number=phone_number)



def resendSMS(unauth_driver): # helper function to resend sms
    newToken = generateOTP()
    UnauthDriver.objects.filter(phone_number=unauth_driver.phone_number)\
        .update(token=newToken)
    unauth_driver.token = newToken
    sendSMS(unauth_driver)



def check_unauthdriver(phone_nb): # helper function to find if unauth driver exists
    unauthdriver = UnauthDriver.objects.filter(phone_number=phone_nb)
    if unauthdriver.exists():
        return True
    else:
        return False        



def check_authdriver(phone_nb): # helper function to find if auth driver exists
    authdriver = User.objects.filter(phone_number=phone_nb, is_driver=1)
    if authdriver.exists():
        return True
    else:
        return False 



def sendSMS(unauth_driver): # helper function to send sms
    message = twilio_client.messages \
            .create(
                body="\nHello " + unauth_driver.first_name + " " + unauth_driver.last_name + \
                ", here is your sign up token: " + unauth_driver.token,
                from_="+12244343836",
                to="+961" + unauth_driver.phone_number
            )


def is_valid_token(token): #helper function to use in checking the token and authenticating the driver
    unauth_driver = UnauthDriver.objects.get(pk=token)
    return unauth_driver