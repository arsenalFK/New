from django import forms
from django.conf import settings

from .models import PlayerRequest, Player, News


class PlayerRequestForm(forms.ModelForm):
    class Meta:

        model = PlayerRequest
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlayerRequestForm, self).__init__(*args, **kwargs)

        self.fields['player_request_age'].widget = forms.widgets.Select(
        choices=[[None, '----']] + [[x, x] for x in range(14, 61)]
        )

class AddPlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ('player_img',)






class AddNForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'news_image']
