from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('item/', include('item.urls' )),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('', include('Car.urls')),
    path("api/", include("api.urls"))
    # path('', views.index , name='index')
    # path('', views.index , name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# my name is asdddkmighplhfgghfty

