from django.db import models


class Restaurant(models.Model):

    name = models.CharField(max_length=55, unique=True)
    address = models.CharField(max_length=255)
    # TODO: establish a many-to-many relationship with User through the join model

    # TODO: Add a `favorite` custom property. Remember each JSON representation of a restaurant should have a `favorite` property. Not just the ones where the value is `true`.
