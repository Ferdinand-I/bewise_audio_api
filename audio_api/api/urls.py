from django.urls import path

from .views import CreateUserView, AudioView

urlpatterns = [
    path('createuser/', CreateUserView.as_view(), name='createuser'),
    path('record/', AudioView.as_view(), name='audio')
]
