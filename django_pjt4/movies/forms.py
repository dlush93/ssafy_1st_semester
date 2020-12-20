from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    title = forms.CharField(
            label='제목',
            help_text='',
            widget=forms.TextInput(
                    attrs={
                        'class': 'w-100 ',
                        'placeholder': '제목 입력'
                    }
                )
        )
    # poster = forms.CharField(
    #         label='poster',
    #         help_text='',
    #         widget=forms.TextInput(
    #                 attrs={
    #                     'class': 'w-100 ',
    #                     'placeholder': 'url을 입력해주세요'
    #                 }
    #             )
    #     )
    class Meta:
        model = Movie
        fields = ['title']


