from django import forms
from . import models, parser_anilibria

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('anilibria.tv', 'anilibria.tv'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'anilibria.tv':
            anilibria_schedule = parser_anilibria.parsing_anilibria()
            for item in anilibria_schedule:
                models.AnilibriaModel.objects.create(**item)
