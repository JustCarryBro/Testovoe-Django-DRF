from django.urls import path, include
from .views import task_list,TaskApi
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskApi)

urlpatterns = [
    path('', task_list, name='main'),
    path('api/', include(router.urls)),

]