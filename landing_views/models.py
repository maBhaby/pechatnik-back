from django.db import models

# Create your models here.

from enum import Enum
class VIEW_STATUS(Enum):
    ACTIVE = 1
    

class PriceView(models.Model):
    __view_name='Блок Прайсов'

    isActive = models.BooleanField(default=False)
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=512, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        self.locator_field = 'PriceView'
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(f'{self.title}: {self.__view_name}')
    


class ContactView(models.Model):
    __view_name='Блок контактов'

    isActive = models.BooleanField(default=False)
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=512, blank=True, null=True)
    phone = models.TextField(max_length=22, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    whats_app_link = models.URLField()
    instagram_app_link = models.URLField()

    def __init__(self, *args, **kwargs):
        self.locator_field = 'ContactsView'
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(f'{self.title}: {self.__view_name}')
