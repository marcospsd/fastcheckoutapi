from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register('produto', ProdutoViewSet)
router.register('cliente', ClienteViewSet)
router.register('venda', VendaViewSet)
router.register('corpovenda', CorpoVendaViewSet)
router.register('formavenda', FormaVendaViewSet)
router.register('create', CreateUserView)
router.register('saidaprodutos', SaidaProdutosViewSet)


urlpatterns = [
    path('produto/<desc_pk>', ProdutoSearchView.as_view(), name='desc_pk'),
]
