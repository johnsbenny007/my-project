from django.db import models

# Create your models here.
class Search(models.Model):
    search=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now=True)#teme stamp when it is created

    def __str__(self):
        return'{}'.format(self.search)  #making the objects in the database to have the name as it as the search

    class Meta:
        verbose_name_plural='searches'  #to make the things in correct plural (actully without this class it will appear as  searchs
