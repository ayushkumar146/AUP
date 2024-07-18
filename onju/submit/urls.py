from django.urls import path
from submit.views import submit,code_view

urlpatterns = [
    path("code/<int:user_id>/", submit, name="submit"),
     path('code/<int:user_id>/', code_view, name='code-view'),
     path('submit/<int:user_id>/', submit, name='submit'),
]