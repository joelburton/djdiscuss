from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from discuss.models import Discussion


class Cat(models.Model):

    # use default int ID as pk
    name = models.CharField(max_length=50)

    # This is optional; everything works even if this isn't added.
    #
    # This just provide a convenient API for getting the discussion for the object.
    # You can always use the utility method `discuss.util.get_discussion(obj)` instead.

    discussion = GenericRelation(Discussion)

    def __str__(self):
        return self.name


class Dog(models.Model):

    # use str name as PK

    name = models.CharField(max_length=50, primary_key=True)

    discussion = GenericRelation(Discussion)

    def __str__(self):
        return self.name

