from django.db import models


class Groups(models.Model):

    parrent_group = models.ForeignKey('self', related_name='subgroups', on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name='Родительская группа')
    image = models.ImageField(upload_to='Groups_img', verbose_name='Иконка', null=False)
    name = models.CharField(max_length=64, verbose_name='Название', null=False)
    description = models.TextField(max_length=512, blank=True, null=False, verbose_name='Описание',)

    @property
    def name_group(self):
        try:
            def __str__(self):
                return self.parrent_group.name

            return __str__(self)
        except:
            return '0'

    @property
    def count_subgroups(self):
        return self.subgroups.count()

    # @property
    # def count_subelements(self):
    #     print(Elements.objects.filter(moderated=True).filter(parrent_group=self.parrent_group))
    #     try:
    #         print(self.parrent_group.name)
    #         return Elements.objects.filter(moderated=True).filter(subgroupselement=self.parrent_group).count()
    #     except:
    #         return '--'

    # @property
    # def name_subgroup(self):
    #     return self.subgroups.name

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'


class Elements(models.Model):

    parrent_group = models.ForeignKey(Groups, related_name='subgroupselement', on_delete=models.CASCADE, null=False,
                                      verbose_name='Родительская группа')
    image = models.ImageField(upload_to='Elements_img', null=False, verbose_name='Иконка')
    name = models.CharField(max_length=64, null=False, verbose_name='Название')
    description = models.TextField(max_length=512, blank=True, null=False, verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Дата создания')
    moderated = models.NullBooleanField(default=None, null=False, verbose_name='Проверен модератором')

    @property
    def name_group(self):
        def __str__(self):
            return self.parrent_group.name

        return __str__(self)

    class Meta:
        verbose_name = 'Элементы'
        verbose_name_plural = 'Элементы'

