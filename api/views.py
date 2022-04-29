from datetime import datetime

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from users.models import User
from .serializers import UserSerializer

from core.models import *
from .serializers import *
from .permissions import EhSuperUser

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'codvend': user.codvend,
            'nome': user.first_name,
            'tipouser': user.tipouser,
        })

class CreateUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


### API V2

class ProdutoSearchView(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers

    def get_queryset(self):
        if self.kwargs.get('desc_pk'):
            return self.queryset.filter(descricao__icontains=self.kwargs.get('desc_pk'))|self.queryset.filter(codigo__icontains=self.kwargs.get('desc_pk'))


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializers


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class CorpoVendaViewSet(viewsets.ModelViewSet):
    queryset = Corpo_venda.objects.all()
    serializer_class = CorpoVendaSerializers

class FormaVendaViewSet(viewsets.ModelViewSet):
    queryset = Formapagamento.objects.all().filter(created_at=datetime.today())
    serializer_class = FormaVendaSerializers

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializers

    def get_queryset(self):
        if self.request.user.tipouser == 'C':
            return Venda.objects.filter(create_at=datetime.today()).order_by("-ordem")
        elif self.request.user.tipouser == 'V':
            return Venda.objects.filter(vendedor=self.request.user.codvend, create_at=datetime.today()).order_by("-ordem")
        elif self.request.user.tipouser == 'A':
            return Venda.objects.filter(status='F').order_by("-ordem")

class SaidaProdutosViewSet(viewsets.ModelViewSet):
    queryset = SaidaProdutos.objects.filter(visualizado=False)
    serializer_class = SaidaProdutosSerielizer