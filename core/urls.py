from django.contrib import admin
from django.urls import path, include
from compiler import views as compiler_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend views
    path('', compiler_views.home, name='home'),
    path('', include('compiler.urls')),

    # API views
    path('api/', include('compiler.urls')),
]
