from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import ContactMessage
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label=_("Please verify you're not a robot "))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))


# نمایش همه کاربران
users = User.objects.all()

# نمایش نام‌های کاربران
for user in users:
    print(user.username)
