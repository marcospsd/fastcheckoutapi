from dataclasses import fields
import re
from typing import Counter

from rest_framework import serializers

from core.models import *
from users.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Sum, Count



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'password', 'codvend', 'tipouser']

    def save(self):
        conta = User(
            username=self.validated_data['username'],
            codvend=self.validated_data['codvend'],
            first_name=self.validated_data['first_name'],
            tipouser=self.validated_data['tipouser'],
        )
        senha = self.validated_data['password']
        conta.set_password(senha)
        conta.save()
        return print(conta)




class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'cpf',
            'nome',
            'email',
            'telefone',
        ]

    def create(self, validated_data):
        cpf = validated_data.pop('cpf')
        telefone = validated_data.pop('telefone')
        print(validated_data)
        if not cpf.isnumeric():
            user = Cliente.objects.create(cpf=re.sub(r'[^\w\s]', '', cpf), telefone=re.sub(r'[^\w\s]', '', telefone), **validated_data)
        else:
            user = Cliente.objects.create(cpf=cpf, telefone=telefone, **validated_data)
        return user


class ProdutoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            'codigo',
            'descricao',
            'valor_unitsis',
            'valor_unitpro',
        ]


class CorpoVendaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Corpo_venda
        fields = ['id','os', 'codpro','descripro', 'quantidade', 'valor_unitsis', 'valor_unitpro']
        read_only_fields = ['os']


class FormaVendaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Formapagamento
        fields = ['key', 'id', 'forma', 'parcelas', 'valor']
        read_only_fields = ['key']

class VendaSerializers(serializers.ModelSerializer):
    corpovenda = CorpoVendaSerializers(source='ordem_venda', many=True)
    formavenda = FormaVendaSerializers(source='formpag_venda', many=True)

    class Meta:
        model = Venda
        fields = '__all__'

    def create(self, validated_data):
        data1 = validated_data.pop('ordem_venda')
        data2 = validated_data.pop('formpag_venda')
        user = Venda.objects.create(**validated_data)
        for data1 in data1:
            Corpo_venda.objects.create(os=user, **data1)
            name = data1['codpro']
            data = Produto.objects.filter(codigo=name).values('codigo','descricao','reposicao')
            newdata = data[0]
            if newdata['reposicao'] is True:
                SaidaProdutos.objects.create(venda=str(user), descri=data1['descripro'])
        for data2 in data2:
            Formapagamento.objects.create(key=user, **data2)
        return user

    def update(self, instance, validated_data):
        data1 = validated_data.pop('ordem_venda')
        data2 = validated_data.pop('formpag_venda')
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.email = validated_data.get('email', instance.email)
        instance.vendedor = validated_data.get('vendedor', instance.vendedor)
        instance.nomevendedor = validated_data.get('nomevendedor', instance.nomevendedor)
        instance.status = validated_data.get('status', instance.status)
        instance.total_venda = validated_data.get('total_venda', instance.total_venda)
        instance.save()
        Corpo_venda.objects.filter(os=instance).delete()
        Formapagamento.objects.filter(key=instance).delete()
        for data in data1:
            Corpo_venda.objects.create(os=instance, **data)
            try:
                name = data1['codpro']
                data = Produto.objects.filter(codigo=name).values('codigo','descricao','reposicao')
                newdata = data[0]
                if newdata['reposicao'] is True:
                    SaidaProdutos.objects.create(venda=str(user), descri=data1['descripro'])
            except:
                pass

        for data in data2:
            Formapagamento.objects.create(key=instance, **data)

    
        return instance




class SaidaProdutosSerielizer(serializers.ModelSerializer):

    class Meta:
        model = SaidaProdutos
        fields = '__all__'

class ChartsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Venda
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ChartsSerializer, self).to_representation(instance)
        result_data = {"status": 200, "message": "Cartegory List"}
        result_data["total_venda"] = Venda.objects.filter(status='F').aggregate(Sum('total_venda'))
        result_data['count_venda'] = Venda.objects.filter(status='F').aggregate(Count('pk'))
        return result_data
