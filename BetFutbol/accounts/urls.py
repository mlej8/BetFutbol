from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

# set accounts application's namespace to differentiate between different django applications
app_name= 'accounts'
urlpatterns = [
    path('profile/', views.profile_view, name="profile"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name = "accounts/password_change_form.html", success_url = reverse_lazy('accounts:password_change_done')), name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name = "accounts/password_change_done.html"), name='password_change_done'), # add a return to home page button to the template here
    path("password_reset/", auth_views.PasswordResetView.as_view(success_url = reverse_lazy('accounts:password_reset_done'), email_template_name = "accounts/password_reset_email.html", template_name = "accounts/password_reset_form.html"), name='password_reset'), # redirects to the password_reset_done view
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_done.html"), name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html", success_url = reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path("reset/done/",  auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"),name='password_reset_complete'),
] 

'''
Password reset implementation:
1 - Submit email form where to send reset link      PasswordResetView.as_view()
2 - Email sent success message                      PasswordResetDoneView.as_view()
3 - Link to password reset form in email            PasswordResetConfirmView.as_view()
4 - Password successfully changed message           PasswordResetCompleteView.as_view()
'''