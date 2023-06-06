from django.urls import path

from .views import CreateUserView, AudioView

urlpatterns = [
    path('user/', CreateUserView.as_view(), name='createuser'),
    path('record/', AudioView.as_view(), name='audio')
]
