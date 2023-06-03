from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('<str:username>/',
         views.HistoryView.as_view(),
         name='history'),
    path('host/', views.HostView.as_view(), name='host'),
    path('url/', views.URLView.as_view(), name='url'),
    path('user/', views.UserView.as_view(), name='user'),
    path('', include(router.urls)),
]
