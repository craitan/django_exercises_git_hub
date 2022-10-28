from django import forms
from django.forms import widgets

from games_app.web.models import Profile, Game


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class ProfileEditeForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disable_fields()

    def save(self, commit=True):
        if commit:
            Game.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_disable_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class BaseGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class GameCreateForm(BaseGameForm):
    pass


class GameEditForm(BaseGameForm):
    pass


class GameDeleteForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disable_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
