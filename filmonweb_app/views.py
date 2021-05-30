from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from .forms import PersonForm, SearchForm, TmpMovie
from .models import Genre, Movie, Person, PersonMovie


# Create your views here.


class LikeDict:
    def dict_arrt(self):
        return self.__dict__

    def __call__(self):
        return self.__dict__


def index(request):
    html = LikeDict()
    html.title = 'Strona główna'
    html.pages = [
        ('Lista filmów', 'filmonweb-movies-list'),
        ('Lista osób', 'filmonweb-persons-list'),
        ('Szukaj filmu', 'fow-movie-search')
    ]
    return render(request, 'FilmOnWeb/index.html', context=html())


def movies(request):
    html = LikeDict()
    html.title = "Lista filmów"
    default_order = 'year'
    sort_by_get = request.GET.get('order_by')
    sort_by_session = request.session.get('sorted')
    if sort_by_get:
        request.session['sorted'] = sort_by_get
        field = sort_by_get
    else:
        if sort_by_session:
            field = sort_by_session
        else:
            field = default_order
    html.movies = Movie.objects.all().order_by(field)
    return render(request, 'FilmOnWeb/movies.html', context=html())


def movie_detail(request, movie_id):
    html = LikeDict()
    movie = Movie.objects.get(pk=movie_id)
    html.genres = Genre.objects.filter(movie=movie)
    html.actors = PersonMovie.objects.filter(movie=movie)
    html.title = f"Szczegóły filmu {movie.title}"
    html.movie = movie
    return render(request, 'FilmOnWeb/movie_detail.html', context=html())


def movie_edit(request, movie_id):
    html = LikeDict()
    movie = Movie.objects.get(pk=movie_id)
    html.title = f"Edycja filmu {movie.title}"
    html.form = TmpMovie(instance=movie)
    html.id = movie.id
    # TODO need to remember changed fields of forms when is added a new person
    #  maybe sessions will be good?
    if request.method == "POST":
        form = TmpMovie(request.POST)
        if form.is_valid():
            updated_movie = form.save(commit=False)
            updated_movie.id = movie.id
            updated_movie.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('filmonweb-movies-list'))
    return render(request, 'FilmOnWeb/movie_edit.html', context=html())


def movie_add(request):
    html = LikeDict()
    html.title = "Nowy film"
    html.form = TmpMovie()
    if request.method == "POST":
        form = TmpMovie(request.POST)
        if form.is_valid():
            new_movie = form.save(commit=False)
            new_movie.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('filmonweb-movies-list'))
    return render(request, 'FilmOnWeb/movie_edit.html', context=html())


class MovieDelete(View):
    def __init__(self):
        super(MovieDelete, self).__init__()

    def get(self, request, movie_id):
        html = LikeDict()
        movie = get_object_or_404(Movie, pk=movie_id)
        try:
            movie.delete()
        except Exception as e:
            html.title = 'ERROR!'
            html.error = e
            return render(request, 'FilmOnWeb/error.html', context=html())
        return HttpResponseRedirect(reverse('filmonweb-movies-list'))


def persons(request):
    html = LikeDict()
    html.title = "Lista osób"
    html.persons = Person.objects.all().order_by('last_name')
    return render(request, 'FilmOnWeb/persons.html', context=html())


def person_edit(request, person_id):
    html = LikeDict()
    html.title = "Nowy użytkownik"
    person = Person.objects.get(pk=person_id)
    # TODO needed to add a handling error bad user
    html.title = "Zmiana danych"
    html.form = PersonForm(instance=person)
    html.state = "edit"
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            updated_person = form.save(commit=False)
            updated_person.id = person.id
            updated_person.save()
            return HttpResponseRedirect(reverse('filmonweb-persons-list'))
    return render(request, 'FilmOnWeb/manage_person.html', context=html())


def person_add(request):
    html = LikeDict()
    html.state = "new_user"
    html.title = "Nowy użytkownik"
    html.form = PersonForm()
    if request.method == "POST":
        movie_id = request.GET.get('edit')
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            if movie_id:
                return HttpResponseRedirect(reverse('filmonweb-movie-edit',
                                                    args=(movie_id,)))
            return HttpResponseRedirect(reverse('filmonweb-persons-list'))
    return render(request, 'FilmOnWeb/manage_person.html', context=html())


class DeletePerson(View):
    def __init__(self, *args, **kwargs):
        super(DeletePerson, self).__init__(*args, **kwargs)

    def get(self, request, person_id):
        html = LikeDict()
        person = get_object_or_404(Person, pk=person_id)
        try:
            person.delete()
        except Exception as e:
            html.title = 'ERROR!'
            html.error = e
            return render(request, 'FilmOnWeb/error.html', context=html())
        return HttpResponseRedirect(reverse('filmonweb-persons-list'))


class SearchView(View):
    def __init__(self):
        self.html = LikeDict()
        self.html.title = "Wyszukiwarka filmów"

    def get(self, request):
        self.html.form = SearchForm()
        return render(request, 'FilmOnWeb/fow_search.html',
                      context=self.html())

    def post(self, request):
        r = request.POST
        # NOTICE: person_query & result != result & person_query !!!
        empty = SearchForm({})  # it's needed to know if form is empty
        empty = SearchForm(request.POST)
        if not empty.has_changed():
            # The form was empty, prints all movies
            self.html.result = Movie.objects.all()
            self.html.form = SearchForm()
            self.html.sth = 'All movies'
            return render(request, 'FilmOnWeb/fow_search.html',
                          context=self.html())

        title = r.get('title').replace(" ", "")
        first_name = r.get('first_name')
        last_name = r.get('last_name')
        year_from = r.get('year_from')
        year_to = r.get('year_to')
        rating_from = r.get('rating_from')
        rating_to = r.get('rating_to')
        genries = r.get('genre')
        result = set()

        if title:
            title_query = Movie.objects.filter(Q(title__icontains=title))
            result = set(title_query)

        if year_to or year_from or rating_to or rating_from:
            year_from = int(year_from) if year_from else 1880
            year_to = int(year_to) if year_to else 2022
            rating_from = float(rating_from) if rating_from else 0.0
            rating_to = float(rating_to) if rating_to else 10.0
            # TODO I know, that constraint by defaul gets all movies.
            scope_query = Movie.objects.filter(
                Q(year__range=(year_from, year_to)) &
                Q(rating__range=(rating_from, rating_to))
            )
            scope_query = set(scope_query)
            if scope_query:
                if result:
                    result &= scope_query
                else:
                    result = scope_query

        if genries:
            g = Genre.objects.none()
            genries = genries.replace(" ", "")
            for genry in genries.split(','):
                g |= Genre.objects.filter(name__icontains=genry)
            genre_query = set(Movie.objects.filter(Q(genre__in=g)))
            if not result:
                result = genre_query
            else:
                result &= genre_query

        if first_name or last_name:
            movie_persons = set(Movie.objects.filter(
                (Q(director__last_name__icontains=last_name) &
                 Q(director__first_name__icontains=first_name)) |
                (Q(screenplay__last_name__icontains=last_name) &
                 Q(screenplay__first_name__icontains=first_name))))
            movie_actors = set(Movie.objects.filter(
                Q(personmovie__person__first_name__icontains=first_name) &
                Q(personmovie__person__last_name__icontains=last_name)))
            person_query = movie_actors | movie_persons
            if not result:
                result = person_query
            else:
                result &= person_query

        self.html.form = SearchForm(request.POST)
        self.html.result = result
        return render(request, 'FilmOnWeb/fow_search.html',
                      context=self.html())
