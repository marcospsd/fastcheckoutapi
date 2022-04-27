from django.contrib import admin
from .models import *



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
   list_display = ('codigo', 'descricao')


class CorpoInline(admin.TabularInline):
    model = Corpo_venda
    extra = 1

class FormaInline(admin.TabularInline):
    model = Formapagamento
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('ordem','create_at','total_venda', 'vendedor', )
    inlines = [CorpoInline, FormaInline]


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'telefone', 'email')


@admin.register(SaidaProdutos)
class SaidaProdutosAdmin(admin.ModelAdmin):
    list_display = ('venda', 'descri', 'visualizado')

