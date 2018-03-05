from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000)
    published_date = models.DateTimeField('date published')
    country = models.CharField(max_length=200)
    link=models.TextField(validators=[URLValidator()])

    def __str__(self):
        return self.title


class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    born_at = models.DateField(null=True, blank=True)
    died_at = models.DateField('Died', null=True, blank=True)
    contact_email = models.EmailField(null=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name,self.last_name)
    