# -*- coding: utf-8 -*-
from django.db import models
from rest_framework import serializers
from ...cadastros.models.planta import Planta, PlantaSerializer

class Endereco(models.Model):
    """
    Model do cadastro de enderecos
    """
    planta = models.ForeignKey(Planta, verbose_name='Planta', blank=True, null=True, on_delete=models.PROTECT)
    codigo = models.CharField(verbose_name='Código', max_length=15, blank=False, null=False, default='')

    def __unicode__(self):
        return self.codigo

    class Meta:
        app_label = 'estoque'

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializador
    """
    planta = PlantaSerializer()

    class Meta:
        model = Endereco
        fields = ('planta', 'codigo', )