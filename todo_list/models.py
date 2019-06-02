from django.db import models


class ToDoList(models.Model):
    item = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.item

    