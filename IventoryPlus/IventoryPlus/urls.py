from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('Product.urls')),
    path('notifications/', include('Notifications.urls')),
    path('reports/', include('Reports.urls')),
    path('suppliers/', include('Suppliers.urls')),
    path('categories/', include('Categories.urls')),
    path('', include('UserManager.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
