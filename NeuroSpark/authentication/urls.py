
from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',login_page,name='login_page'),
    path('register',register_page,name="register_page"),
    path('logout',logout_page,name="logout_page"),
    path('reset_password_page',auth_views.PasswordResetView.as_view(template_name="password_reset_forms/password_reset.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_forms/reset_password_link_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_forms/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_forms/password_reset_complete.html"),name="password_reset_complete"),
]