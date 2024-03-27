from django import forms


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='E-mail')


class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Nova senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar nova senha', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")