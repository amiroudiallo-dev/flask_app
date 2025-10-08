from django.urls import path, include # type: ignore
from accounts import admin
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    path("language/", view=views.list_create_language, name="create_language"),
    path("language/<int:pk>/detail/", views.ret_upate_del_LanguageView, name="update_language"),

    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]