from django.urls import path
from stack import views

urlpatterns=[
    path("register",views.SignupView.as_view(),name="register"),
    path("login",views.SigninView.as_view(),name="login"),
    path("home",views.IndexView.as_view(),name="index"),
    path("questions/<int:id>/aswers/add",views.AddanswerView.as_view(),name="addanswer"),
    path("answers/<int:id>/upvote/add",views.UpvoteView.as_view(),name="up_vote"),

]