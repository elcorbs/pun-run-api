from django.db import models

class Run(models.Model):
  theme = models.CharField('Theme of the Pun Run', max_length=100)
  date_from = models.DateTimeField()
  date_to = models.DateTimeField()
  def __str__(self):
    return self.theme
  
  class Meta:
    ordering = ('date_from', )

class Punter(models.Model):
  name = models.CharField('Name of Punter', max_length=100)

  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ('name',)

class Pun(models.Model):
  pun = models.CharField('The Pun', max_length=400)
  run = models.ForeignKey(Run, on_delete=models.CASCADE, verbose_name='Pun Run')
  punter = models.ForeignKey(Punter, on_delete=models.SET_NULL, verbose_name='Punter', default=None, blank=True, null=True)
  timestamp = models.DateTimeField()

  def __str__(self):
    return self.pun
  
  class Meta:
    ordering = ('timestamp',)