# Description: This file contains the URL patterns for the Savanna project.
from django.contrib import admin
from django.urls import path, include
from customers import views
from rest_framework import routers
from rest_framework.authtoken import views as auth_views


router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token),
    path('api/', include('customers.urls')),
    path('api/', include('orders.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]