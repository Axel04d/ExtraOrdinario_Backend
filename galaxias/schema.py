# galaxias/schema.py
import graphene
from graphene_django import DjangoObjectType
from .models import Galaxia

class GalaxiaType(DjangoObjectType):
    class Meta:
        model = Galaxia

class Query(graphene.ObjectType):
    galaxias = graphene.List(GalaxiaType)

    def resolve_galaxias(self, info, **kwargs):
        return Galaxia.objects.all()

class CreateGalaxia(graphene.Mutation):
    id = graphene.Int()
    nombre = graphene.String()
    descripcion = graphene.String()
    ubicacion = graphene.String()

    class Arguments:
        nombre = graphene.String()
        descripcion = graphene.String()
        ubicacion = graphene.String()

    def mutate(self, info, nombre, descripcion, ubicacion):
        galaxia = Galaxia(nombre=nombre, descripcion=descripcion, ubicacion=ubicacion)
        galaxia.save()
        return CreateGalaxia(
            id=galaxia.id,
            nombre=galaxia.nombre,
            descripcion=galaxia.descripcion,
            ubicacion=galaxia.ubicacion,
        )

class Mutation(graphene.ObjectType):
    create_galaxia = CreateGalaxia.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
