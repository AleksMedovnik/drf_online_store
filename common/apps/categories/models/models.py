from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'categories'