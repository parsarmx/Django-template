import random

from settings import OTP_CODE_LENGTH, UNDER_DEVELOPMENT


def generate_otp(skip=UNDER_DEVELOPMENT):
    random.seed(a=None, version=2)
    if skip:
        return "123456"
    return "".join(random.choices("0123456789", k=OTP_CODE_LENGTH))
