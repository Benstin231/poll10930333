from django.urls import path
from .views import *


urlpatterns = [
    #path('poll/', views.poll_list),
    path('', PollRedirect.as_view()),
    path('poll/', PollList.as_view()),
    path('poll/<int:pk>/', PollDetail.as_view()),
    path('option/<int:oid>/', PollVote.as_view()),
    path('poll/create/', PollCreate.as_view()),
    path('poll/<int:pk>/edit/', PollEdit.as_view()),
    path('poll/<int:pk>/delete/', PollDelete.as_view()),
    path('poll/<int:pk>/add/', OptionAdd.as_view()),
]