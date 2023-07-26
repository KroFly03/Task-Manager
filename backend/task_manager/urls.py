from django.contrib import admin
from django.urls import path, include

from swagger import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls'))
]
