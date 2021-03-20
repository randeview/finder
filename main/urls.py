from django.urls import path
from .views import EventCreateView, EventsGetView

urlpatterns = [
    path("create", EventCreateView.as_view()),
    path("get-event", EventsGetView.as_view())
]
