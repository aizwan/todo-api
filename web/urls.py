from django.urls import include, path
from rest_framework import routers
from web import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todo', views.TodoViewset, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]