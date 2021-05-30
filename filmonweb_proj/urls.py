"""filmonweb_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from filmonweb_app.views import (movies, movie_add, movie_edit, movie_detail,
                                 persons, person_add, person_edit, index,
                                 DeletePerson, SearchView, MovieDelete)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='filmonweb-main'),
    path('index/', index, name='filmonweb-index'),

    path('movies/', movies, name='filmonweb-movies-list'),
    path('movie-add/', movie_add, name='filmonweb-movie-add'),
    path('movie-delete/<int:movie_id>/', MovieDelete.as_view(),
         name='filmonweb-movie-del'),
    path('movie-details/<int:movie_id>/', movie_detail,
         name='filmonweb-movie-details'),
    path('movie-edit/<int:movie_id>/', movie_edit,
         name='filmonweb-movie-edit'),

    path('persons/', persons, name='filmonweb-persons-list'),
    path('person-add/', person_add, name='filmonweb-person-add'),
    path('person-delete/<int:person_id>/', DeletePerson.as_view(),
         name='filmonweb-person-del'),
    path('person-edit/<int:person_id>/', person_edit,
         name='filmonweb-person-edit'),
    path('search-movie/', SearchView.as_view(), name="fow-movie-search"),
]
