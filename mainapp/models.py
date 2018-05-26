from django.db import models

class Groups(models.Model):

    parrent_group = models.ForeignKey('self', related_name='subgroups', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='Groups_img')
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True, null=True)

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'


class Elements(models.Model):

    parrent_group = models.ForeignKey(Groups, related_name='subgroupselement', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Elements_img')
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    moderated = models.NullBooleanField(default=None)

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'

