from django.urls import path, include

from . import views

app_name = 'item'

urlpatterns = [
    path('', views.browse, name='browse'),
    path('<int:pk>/', views.detail, name='detail'),
    path('', include('shop.urls'))
]
