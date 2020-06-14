from django.db import models

class Punter(models.Model):
  name = models.CharField('Name of Punter', max_length=100)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ('name',)

class Pun(models.Model):
  pun = models.CharField('The Pun', max_length=400)
  punter = models.ForeignKey(Punter, on_delete=models.CASCADE, verbose_name='Punter')
  timestamp = models.DateTimeField()

  def __str__(self):
    return self.pun
  
  class Meta:
    ordering = ('timestamp',)