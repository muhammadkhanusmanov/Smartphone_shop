from django.db import models
from django.contrib.auth.models import User

class SmartPhone(models.Model):
    price = models.FloatField()
    img_url = models.CharField(max_length=120)
    color = models.CharField(max_length=30)
    ram = models.CharField(max_length=10)
    memory = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    add_date=models.DateTimeField(auto_now_add=True)
    up_date=models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    
    def to_dict(self):
        returned = {
            'id': self.id,
            'price': self.price,
            'img_url':self.img_url,
            'color':self.color,
            'ram':self.ram,
            'memory':self.memory,
            'name':self.name,
            'model':self.model,
            'add_date':self.add_date,
            'update_date':self.up_date
        }
        return returned

class Cart(models.Model):
    phone_id=models.IntegerField()
    phone_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,models.CASCADE)

    def __str__(self) -> str:
        return self.phone_name