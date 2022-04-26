from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.CharField(required=True)
        self.fields['address'] = forms.CharField(required=True)

    def save(self, request):
        phone = self.cleaned_data.pop('phone')
        address = self.cleaned_data.pop('address')

        user = super(MyCustomSignupForm, self).save(request)
