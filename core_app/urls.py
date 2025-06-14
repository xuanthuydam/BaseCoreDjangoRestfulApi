"""
URL configuration for core_app project.

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

from django.contrib import admin
from django.urls import path, include
from doc import swagger

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "swagger/",
        swagger.schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        swagger.schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("simple_app/", include("simple_app.urls"), name="simple_app"),
    path("patterns/", include("patterns.urls"), name="patterns"),
]
