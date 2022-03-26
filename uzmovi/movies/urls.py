from django.urls import path, include
from movies.views import   movies_list, movie_detail, movie_create, movie_edit


urlpatterns = [ 
               
    path('', movies_list),         
    path('<int:movie_id>', movie_detail),
    path('create', movie_create),
    path('edit/<str:movie_id>', movie_edit), # edit/tor
    # path('<int:movie_id>', edit_movie)              
    # path('', hello_view)
]