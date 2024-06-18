from django.urls import path

from network import views

urlpatterns = [
    path("register/", views.SignUpView.as_view(), name="signup"),

    path("", views.SignInView.as_view(), name="signin"),

    path("logout/", views.SignOutView.as_view(), name="signout"),

    path("home/", views.HomeView.as_view(), name="home"),

    path("profile/", views.ProfileView.as_view(), name="profile"),

    path("profile/update/", views.UpdateUserProfileView.as_view(), name="profile-update"),
    
    path("uploadpost/", views.PostUploadView.as_view(), name="post-upload"),

    path("postlike/<int:pk>/",views.LikeCountUpdateView.as_view(),name="like-count"),

    path("postdetail/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),

    path("postupdate/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),

    path("postdelete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),

    path("postcomment/<int:pk>", views.CommentCreateView.as_view(), name="comment"),

    path("comment/all/<int:pk>/",views.CommentListView.as_view(),name="comment-list")

      
]
