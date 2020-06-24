import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from punrun.api.models import Punter, Pun

class PunterType(DjangoObjectType):
  class Meta:
    model = Punter

class PunType(DjangoObjectType):
  class Meta:
    model = Pun

class Query(ObjectType):
  punter = graphene.Field(PunterType, id=graphene.Int())
  pun = graphene.Field(PunType, id=graphene.Int())
  punters = graphene.List(PunterType)
  puns = graphene.List(PunType)

  def resolve_punter(self, info, **kwargs):
    id = kwargs.get('id')

    if id is not None:
      return Punter.objects.get(pk=id)
    
    return None
  
  def resolve_pun(self, info, **kwargs):
    id = kwargs.get('id')

    if id is not None:
      return Pun.objects.get(pk=id)
    
    return None
  
  def resolve_punters(self, info, **kwargs):
    return Punter.objects.all()

  def resolve_puns(self, info, **kwargs):
    return Pun.objects.all()

schema = graphene.Schema(query=Query)