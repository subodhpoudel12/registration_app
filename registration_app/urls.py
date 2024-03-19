from django.contrib import admin
from django.urls import path, include
from registration_app import views
# from djangoregister import settings
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.views.generic import TemplateView


schema_view = get_schema_view(
   openapi.Info(
      title="my django api",
      default_version='v1',
      description="This are the django api for plugins",
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.index_view, name='index'),

    # path('api/', include('api.urls')),
    path('organization/', OrganizationView.as_view(), name='anything'),
    # path('register_organization/', register_organization, name='register'),
    path('student/', StudentView.as_view(), name='student'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
