from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class AppUserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        return super().save(commit=commit)
