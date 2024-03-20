from django.urls import path
from .views import RegisterView, ProductView, Filter


urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('product/',ProductView.as_view()),
    path('filter/<character:company_name>/',Filter.as_view())
]