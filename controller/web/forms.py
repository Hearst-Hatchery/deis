from django import forms
from simplemathcaptcha.fields import MathCaptchaField


class MathCaptchaForm(forms.Form):
    captcha = MathCaptchaField()
