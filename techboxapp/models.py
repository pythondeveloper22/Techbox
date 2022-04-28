from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    mobile = models.CharField(max_length=50, help_text='mobile number')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ItemAssigment(models.Model):
    name = models.ForeignKey('Employee', on_delete=models.CASCADE, help_text='select name of employee')
    item = models.ManyToManyField(Item, help_text=' you can select multiple items')

    def get_item(self):
        return ','.join([str(i)for i in self.item.all()])





