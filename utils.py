from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('3554712B354B3541466C66617A5A6B6A5337523474704178767050397A324F6748634A4C654461637546453D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code}کد تایید شما: '
        }
        response = api.sms_send( params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)

class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

