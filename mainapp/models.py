from django.db import models

class Groups(models.Model):

    parrent_group = models.ForeignKey('self', related_name='subgroups', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родительская группа')
    image = models.ImageField(upload_to='Groups_img', verbose_name='Иконка')
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(max_length=512, blank=True, null=True, verbose_name='Описание')

    @property
    def name_group(self):
        try:
            return self.parrent_group.name
        except:
            return '0'

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'


class Elements(models.Model):

    parrent_group = models.ForeignKey(Groups, related_name='subgroupselement', on_delete=models.CASCADE, verbose_name='Родительская группа')
    image = models.ImageField(upload_to='Elements_img', verbose_name='Иконка')
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.TextField(max_length=512, blank=True, null=True, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    moderated = models.NullBooleanField(default=None, verbose_name='Проверен модератором')

    @property
    def name_group(self):
        return self.parrent_group.name

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'

