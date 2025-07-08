"""
URL configuration for my_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# mainapp/urls.py (assuming 'mainapp' is the name of your project's root directory)

from django.contrib import admin
from django.urls import path, include  # <-- You need to import 'include' here

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add this line to include your app's URLs:
    path('', include('myapp.urls')),  # This tells Django to look for URLs in 'myapp/urls.py'
                                     # The empty string '' means it will handle the root URL
                                     # (e.g., http://127.0.0.1:8000/)
]
