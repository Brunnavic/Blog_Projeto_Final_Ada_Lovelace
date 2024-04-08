from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls', namespace='home')),
    path("user_profile/", views.user_profile, name="user_profile"),
    path('Profile/', views.Profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('search/', views.search, name='search'),
    path('add_blogs/', views.add_blogs, name='add_blogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)