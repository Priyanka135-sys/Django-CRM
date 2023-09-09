from django.db import models
class Record(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    address=models.TextField(max_length=100)
    city=models.TextField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=6)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")
    
# Create your models here.
