from django.contrib import admin
from django.urls import path
from custom_registration import views

urlpatterns = [
path('loginuser/', views.login_user, name="loginuser"),
    # path('homepage/', views.HomePage, name="homepage"),
    path('logout/', views.logout_user, name="logout"),
    # path('clicklogin/', views.clicklogin, name="clicklogin"),
    path('register_user/', views.register_user, name="register_user"),
    # path('click_user/', views.ClickRegister, name="click_user"),
    path('organizations/', views.organizations_list, name="organizations_list"),  # Endpoint for listing organizations
    path('organizations/<int:organization_id>/', views.organization_detail, name="organization_detail"),  # Endpoint for individual organization details
    path('', views.register_user, name=""),
    path('admin/', admin.site.urls),
]
