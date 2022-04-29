from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=25, null=True, blank=True)
    cpf = models.CharField(max_length=25, primary_key=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.cpf



class Produto(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descricao = models.CharField(max_length=50)
    valor_unitsis = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitpro = models.DecimalField(max_digits=10, decimal_places=2)
    grupo = models.CharField(max_length=30, null=True, blank=True)
    reposicao = models.BooleanField(default=False)


    def __str__(self):
        return str(self.codigo)

statusvenda = [
    ('P', 'Pendente'),
    ('F', 'Finalizado'),
]

class Venda(models.Model):
    ordem = models.BigAutoField(primary_key=True, auto_created=True)
    cpf = models.ForeignKey(Cliente, related_name='cpfvenda', on_delete=models.CASCADE)
    nome = models.CharField(max_length=25, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    create_at = models.DateField(auto_now=True)
    hour_at = models.TimeField(auto_now=True)
    vendedor = models.CharField(max_length=6, blank=True, null=True)
    nomevendedor = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, choices=statusvenda)
    total_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.ordem)


class Corpo_venda(models.Model):
    os = models.ForeignKey(Venda, related_name='ordem_venda', on_delete=models.CASCADE)
    codpro = models.ForeignKey(Produto, related_name='prod_venda', on_delete=models.CASCADE)
    descripro = models.CharField(max_length=50, blank=True, null=True)
    valor_unitsis = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitpro = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField()
    created_at = models.DateField(auto_now=True)
    hour_at = models.TimeField(auto_now=True)

    def __str__(self):
        return "Cadastrado"


methodos = [
    ('DH', 'Dinheiro'),
    ('CC', 'Cartão de Credito'),
    ('CD', 'Cartão de Débito'),
    ('DP', 'Deposito em Conta'),
]


class Formapagamento(models.Model):
    key = models.ForeignKey(Venda, related_name='formpag_venda', on_delete=models.CASCADE)
    forma = models.CharField(max_length=2, choices=methodos)
    parcelas = models.PositiveIntegerField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now=True)
    hour_at = models.TimeField(auto_now=True)


class SaidaProdutos(models.Model):
    venda = models.CharField(max_length=10)
    descri = models.CharField(max_length=50)
    visualizado = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
