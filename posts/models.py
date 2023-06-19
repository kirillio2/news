from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return f'/сategory/{self.name}/'

    def __str__(self):
        return f"Наименование: {self.name}"
