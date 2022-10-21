from django.contrib.auth.forms import UserCreationForm

from .models import Account

class CustomaccountFrom(UserCreationForm):

    class Meta:
        model = Account
        fields=('email','username')

