from django.urls import path
#from .views import ItensApiView, UserApiView, InventarioApiView
from rest_framework.routers import SimpleRouter
from .api.viewsets import (
    ItensApiView, 
    UsersApiView, 
    InventariosApiView, 
    ItenApiView, 
    UserApiView, 
    InventarioApiView,

    UserViewSet,
    ItensViewSet,
    InventarioViewSet)

router = SimpleRouter()
router.register('itens', ItensViewSet)
router.register('users', UserViewSet)
router.register('inventario', InventarioViewSet)


urlpatterns = [
    path('itens/', ItensApiView.as_view(), name='itens'),
    path('users/', UsersApiView.as_view(), name='users'),
    path('inventario/', InventariosApiView.as_view(), name='inventarios'),

    path('itens/<int:pk>/', ItenApiView.as_view(), name='iten'),
    path('users/<int:pk>/', UserApiView.as_view(), name='user'),
    path('inventario/<int:pk>/', InventarioApiView.as_view(), name='inventario')
]