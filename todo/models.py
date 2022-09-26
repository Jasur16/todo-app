from django.db import models


class TodoAppModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'