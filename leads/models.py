from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)

    title = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)

    phone = models.IntegerField(unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    website = models.CharField(max_length=512, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    twitter_personal = models.CharField(max_length=255, null=True, blank=True)
    twitter_brand = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)

    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)

    status = models.CharField(max_length=2,
                              choices=[('QL', 'Qualified'),
                                       ('FU', 'Follow Up')],
                              default='FU')
    relationship = models.CharField(max_length=2,
                                    choices=[('H1', 'Blind trust'),
                                             ('H2', 'Good Relationship'),
                                             ('H3', 'Good Friend'),
                                             ('C1', 'Aquaintance'),
                                             ('C2', 'Stranger')],
                                    default='C2')

    # tags = models.TextField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

    
class Timeline:

    pass
