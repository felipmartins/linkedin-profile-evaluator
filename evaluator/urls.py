from django.urls import path
from .views import (
    index,
    evaluation
)


urlpatterns = [
    path("", index, name="homepage"),
    path("evaluation/<str:uuid>", evaluation, name="evaluation")
]
