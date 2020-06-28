import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from punrun.api.models import Punter, Pun, Run
from datetime import datetime

class PunterType(DjangoObjectType):
  class Meta:
    model = Punter

class PunType(DjangoObjectType):
  class Meta:
    model = Pun

class RunType(DjangoObjectType):
  class Meta:
    model = Run

class PunterInput(graphene.InputObjectType):
  name = graphene.String()

class PunInput(graphene.InputObjectType):
  pun = graphene.String()
  punterId = graphene.Int(required=False, default=None)
  runId = graphene.Int()

class RunInput(graphene.InputObjectType):
  runTheme = graphene.String()
  deadline = graphene.String()

class CreatePunter(graphene.Mutation):
  class Arguments:
    input = PunterInput(required=True)

  ok = graphene.Boolean()
  punter = graphene.Field(PunterType)

  @staticmethod
  def mutate(root, info, input=None):
    ok = True
    new_punter = Punter(name=input.name)
    new_punter.save()
    return CreatePunter(ok=ok, punter=new_punter)

class AddPun(graphene.Mutation):
  class Arguments:
    input = PunInput(required=True)

  ok = graphene.Boolean()
  pun = graphene.Field(PunType)

  @staticmethod
  def mutate(root, info, input=None):
    ok = True
    punter = None
    if input.punterId is not None:
      punter = Punter.objects.get(pk=input.punterId)
    run = Run.objects.get(pk=input.runId)
    new_pun = Pun(pun=input.pun, punter=punter, timestamp=datetime.now(), run=run)
    new_pun.save()
    return AddPun(ok=ok, pun=new_pun)

class StartRun(graphene.Mutation):
  class Arguments:
    input = RunInput(required=True)

  ok = graphene.Boolean()
  run = graphene.Field(RunType)

  @staticmethod
  def mutate(root, info, input=None):
    ok = True
    new_run = Run(theme=input.runTheme, date_to=datetime.fromisoformat(input.deadline), date_from=datetime.now())
    new_run.save()
    return StartRun(ok=ok, run=new_run)

class Query(ObjectType):
  punter = graphene.Field(PunterType, id=graphene.Int())
  pun = graphene.Field(PunType, id=graphene.Int())
  punters = graphene.List(PunterType)
  puns = graphene.List(PunType)
  current_run = graphene.Field(RunType)
  run = graphene.Field(RunType, id=graphene.Int())
  runs = graphene.List(RunType)

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
  
  def resolve_runs(self, info, **kwargs):
    return Run.objects.all()
  
  def resolve_run(self, info, **kwargs):
    id = kwargs.get('id')

    if id is not None:
      return Run.objects.get(pk=id)
 
    return None
  
  def resolve_current_run(self, info, **kwargs):
    try:
      return Run.objects.filter(date_from__lte=datetime.now()).filter(date_to__gte=datetime.now()).order_by('-date_from')[0]
    except IndexError:
      return None
      

class Mutation(graphene.ObjectType):
  create_punter = CreatePunter.Field()
  add_pun = AddPun.Field()
  start_run = StartRun.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)