from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from callisto.users_app.models import Profile

UserModel = get_user_model()


class AppUserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        return super().save(commit=commit)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel
        fields = ['email', ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'