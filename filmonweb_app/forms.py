from datetime import datetime
from django import forms

from .models import Person, Movie, Genre


class PersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {'class': "form-control"}
        self.fields['last_name'].widget.attrs = {'class': "form-control"}

    class Meta:
        model = Person
        fields = ('first_name', 'last_name',)
        labels = {'first_name': "Imię", 'last_name': "Nazwisko"}


class TmpMovie(forms.ModelForm):

    m2m_field = 'starring'

    def __init__(self, *args, **kwargs):
        super(TmpMovie, self).__init__(*args, **kwargs)
        self.fields['genre'].widget.attrs = {'class': 'form-check-input'}
        self.fields['starring'].widget.attrs = {'class': 'form-select'}
        self.fields['director'].widget.attrs = {'class': 'form-select'}
        self.fields['screenplay'].widget.attrs = {'class': 'form-select'}
        self.fields['year'].widget.attrs = {'class': 'form-control'}
        self.fields['rating'].widget.attrs = {'class': 'form-control',
                                              'step': '0.1'}
        self.fields['title'].widget.attrs = {'class': 'form-control'}

    class Meta:
        model = Movie
        fields = ('title', 'year', 'rating', 'genre', 'starring',
                  'director', 'screenplay')
        labels = {'genre': 'kategoria', 'title': 'tytuł', 'year': 'rok',
                  'rating': 'ocena',  'director': 'reżyser',
                  'screenplay': 'scenariusz'}

    class CustomStarring(forms.ModelMultipleChoiceField):
        def label_from_instance(self, member):
            return (f"{member.first_name} "
                    f"{member.last_name}")

    class CustomGenre(forms.ModelMultipleChoiceField):
        def label_from_instance(self, member):
            return f"{member.name}"

    class CustomPerson(forms.ModelChoiceField):
        def label_from_instance(self, member):
            return f"{member.first_name} {member.last_name}"

    genre = CustomGenre(queryset=Genre.objects.all(),
                        widget=forms.CheckboxSelectMultiple,
                        label="Kategoria")

    starring = CustomStarring(queryset=Person.objects.all().order_by('last_name'),
                              widget=forms.SelectMultiple,
                              label="Występują")

    director = CustomPerson(queryset=Person.objects.all(),
                            label="Reżyseria")

    screenplay = CustomPerson(queryset=Person.objects.all(),
                              label="Scenariusz")


class SearchForm(forms.Form):
    current_year = datetime.today().year
    title = forms.CharField(
        label="Tytuł", max_length=255, required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    first_name = forms.CharField(
        label="Imię", max_length=255, required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    last_name = forms.CharField(
        label="Nazwisko", max_length=255, required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    year_from = forms.IntegerField(
        label="Rok od", min_value=1880, max_value=current_year,
        required=False,
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    year_to = forms.IntegerField(
        label="Rok do", min_value=1880, max_value=current_year,
        required=False,
        widget=forms.NumberInput(attrs={'class': "form-control"})
    )
    genre = forms.CharField(
        label="Kategoria", max_length=255, required=False,
        widget=forms.TextInput(attrs={'class': "form-control"})
    )
    rating_from = forms.FloatField(
        label="Ocena od", min_value=0, max_value=10, required=False,
        widget=forms.NumberInput(attrs={'step': "0.01",
                                        'class': "form-control"})
    )
    rating_to = forms.FloatField(
        label="Ocena do", min_value=0, max_value=10, required=False,
        widget=forms.NumberInput(attrs={'step': "0.01",
                                        'class': "form-control"})
    )
