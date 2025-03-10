from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import logout_view  # Import the logout view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('logout/', logout_view, name='logout'),  # Add the logout URL
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
