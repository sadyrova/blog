"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from blog import settings
from posts.views import main_page_view, post_view, post_detail_view
from tovars.views import main_page_view, tovar_view, tovar_detail_view, tovar_create_view, review_create_view
from django.conf.urls.static import static

"""client ->/
    DJANGO: client"""



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('posts/', post_view),
    path('tovars/', tovar_view),
    path('posts/<int:id>/', post_detail_view),
    path('tovars/<int:id>/', tovar_detail_view),
    path('tovars/create/', tovar_create_view),
    path('tovars/create/', review_create_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)