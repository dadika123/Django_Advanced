from django.urls import path

from authapp.views import Login, Logout, RegisterView, ProfileEdit

app_name = 'authapp'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileEdit.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>/', RegisterView.verify, name='verify'),
]
