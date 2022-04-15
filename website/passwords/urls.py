from django.urls import path

from . import views

app_name = "passwords"

urlpatterns = [
    path(
        '',
        views.PassswordHomeView.as_view(),
        name="index",
    )
]
