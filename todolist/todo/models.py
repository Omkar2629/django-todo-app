from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    due_datetime = models.DateTimeField(null=True, blank=True
                                        )
    def __str__(self):
        return self.name


class Task(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    due_datetime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title