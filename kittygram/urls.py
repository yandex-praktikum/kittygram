# API function view lesson
from cats.views import cat_list
from django.urls import include, path

urlpatterns = [
   path('cats/', cat_list),
]


