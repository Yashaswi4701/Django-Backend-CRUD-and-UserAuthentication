from django.db import models


#Never deploy a site into production with DEBUG turned on

# Create your models here.
class Members(models.Model):
    
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    description=models.TextField()
    date=models.DateTimeField(null=True)
    image=models.ImageField(upload_to='media/')
    
    def __str__(self):
        return f"{self.name}"
    
    
