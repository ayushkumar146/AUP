from django.urls import path
from dashboard.views import home

urlpatterns = [
    path("Dashboard/", home, name="dashboard"),
    # path("polls/<int:poll_id>/", poll_detail, name="poll-detail"),

]