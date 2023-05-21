from django.urls import path

from .views import CreateUserView

urlpatterns = [
    path('createuser/', CreateUserView.as_view(), name='createuser')
]
