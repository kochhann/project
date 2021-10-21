from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created_date = models.DateField('Criação', auto_now_add=True)
    modified_date = models.DateField('Modificação', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'Engine'),
        ('lni-stats-up', 'Chart'),
        ('lni-users', 'User'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Rocket'),
    )
    service = models.CharField('Serviço', max_length=100)
    description = models.TextField('Descrição', max_length=200)
    icon = models.CharField('Ícone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.service


class Position(Base):
    position = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.position


class Employee(Base):
    name = models.CharField('Nome', max_length=100)
    position = models.ForeignKey(Position, verbose_name='Cargo', on_delete=models.PROTECT)
    bio = models.TextField('Biografia', max_length=300)
    image = StdImageField('Imagem,', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

        def __str__(self):
            return self.name
