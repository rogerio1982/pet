# model


from django.db import models


# teste github !!!

class Cliente(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Pet(models.Model):
    title = models.CharField(max_length=100)
    cliente = models.ForeignKey('cliente', on_delete=models.CASCADE, related_name='cliente')
    def __str__(self):
        return self.title

class Produtos(models.Model):

    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Vendas(models.Model):
    MY_CHOICES = (
        ('aguardando', 'aguardando'),
        ('realizado', 'realizado'),
    )
    status = models.CharField(max_length=100, choices=MY_CHOICES)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE, related_name='Pet')



class Servico(models.Model):

    #produtos = models.CharField(max_length=100)
    title = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    #produtos = models.CharField(max_length=100)
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)



