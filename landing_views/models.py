from django.db import models

# Create your models here.

class PriceView(models.Model):
    __view_name='Блок Прайсов'

    title = models.TextField(max_length=256)
    description = models.TextField(max_length=512, blank=True, null=True)

    def __str__(self):
        return str(f'{self.title} {self.__view_name}')
