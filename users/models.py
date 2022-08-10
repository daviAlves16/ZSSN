from django.db import models

class User(models.Model):
    id_users =  models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    latitude = models.IntegerField(null=False, blank=False)
    longitude = models.IntegerField(null=False, blank=False)
    contaminacao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Itens(models.Model):
    id_itens = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    pontos = models.IntegerField(null=False, blank=False)

    def __str__(self):
          return self.nome


class Inventario(models.Model):
    user = models.ForeignKey(User, related_name='inventario', on_delete=models.CASCADE)
    item = models.ForeignKey(Itens, related_name='item', on_delete=models.CASCADE)
    quantidade = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "user={}, item={}, quantidade={}".format(self.user, self.item, self.quantidade)