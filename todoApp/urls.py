from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todoApp', views.TodoViewSet, basename='todo')

urlpatterns = [
    
]

urlpatterns += router.urls
