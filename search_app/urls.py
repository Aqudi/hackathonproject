from django.urls import path 
from . import views
from search_app.views import searchResult
app_name ='search_app'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),


]