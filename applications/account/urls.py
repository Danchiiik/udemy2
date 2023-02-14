from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from applications.account.views import ( 
        ChangePasswordApiView, ForgotPasswordFinishApiview, ForgotRasswordApiView, 
        MentorActivationApiView, MentorRegisterApiView, ProfileViewSet, UserRegisterApiView, UserActivationApiView
)

router = DefaultRouter()
router.register('', ProfileViewSet)


urlpatterns = [
    path('register/', UserRegisterApiView.as_view()),
    path('register/mentor/', MentorRegisterApiView.as_view()),
    path('activate/<uuid:activation_code>/', UserActivationApiView.as_view()),
    path('mentor/activate/<uuid:activation_code>/', MentorActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('change_password/', ChangePasswordApiView.as_view()),
    path('forgot_password/', ForgotRasswordApiView.as_view()),
    path('forgot_password_finish/', ForgotPasswordFinishApiview.as_view()), 
    path('profile/', include(router.urls))
]