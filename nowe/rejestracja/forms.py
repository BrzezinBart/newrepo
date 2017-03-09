from django import forms
import django.contrib.auth.models
import django.contrib.auth.forms


class reje(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "Podane hasła różnią się od siebie, proszę spróbować ponownie."
    }
    password1 = forms.CharField(label="Hasło",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Potwierdzenie",
                                widget=forms.PasswordInput,
                                help_text="Proszę wpisać ponownie hasło, w celu weryfikacji.")

    class Meta:
        model = django.contrib.auth.models.User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
