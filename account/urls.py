from django.urls import path
from .views import RegisterView, ActivationView,  ActivateCourierView, RegisterCourierView, GetUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('userlist/', GetUserView.as_view()),
    path('courier/register/', RegisterCourierView.as_view()),
    path('courier/activate/', ActivateCourierView.as_view())

]

# urlpatterns = [
#     path('register/', RegisterView.as_view()),
#     path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('refresh/', TokenRefreshView.as_view(), name='token_refresh')]