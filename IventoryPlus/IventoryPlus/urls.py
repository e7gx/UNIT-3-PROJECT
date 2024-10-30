from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from . import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),
    path('notifications/', include('Notifications.urls')),
    path('reports/', include('Reports.urls')),
    path('suppliers/', include('Suppliers.urls')),
    path('categories/', include('Categories.urls')),
    path('reg/', include('UserManager.urls')),
    path('api/', include('rest_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
