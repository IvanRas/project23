from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUserCreationForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUserCreationForm
        fields = ('email', 'password1', 'password2')

