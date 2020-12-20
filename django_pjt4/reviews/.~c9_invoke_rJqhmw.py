from django import forms
from .models import Review,Comment
from dal import autocomplete
from movies.models import Movie

class ReviewForm(forms.ModelForm):
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
    content = forms.CharField(
            label='내용',
            help_text='자유롭게 작성해주세요.',
            widget=forms.Textarea(
                    attrs={
                        'class':'w-100',
                    }
                )
        )
    movie = forms.ModelChoiceField(
        queryset = Movie.objects.all(),
        widget = autocomplete.ModelSelect2(url='reviews:movie-autocomp')

        )
    class Meta:
        model = Review
        fields = ['title','content','movie']

class CommentForm(forms.ModelForm):
    content = forms.CharField(
            label='내용',
            help_text='자유롭게 작성해주세요.',
            widget=forms.Textarea(
                    attrs={
                        'class':'w-100',
                        'style':'height: 50px',
                    }
                )
        )
    class Meta:
        model = Comment
        fields = ['content']