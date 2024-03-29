from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_projects')

    @property
    def total(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

class Pledge(models.Model):
	amount = models.IntegerField()
	comment = models.CharField(max_length=200)
	anonymous = models.BooleanField()
	project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
	supporter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='supporter_pledges')
