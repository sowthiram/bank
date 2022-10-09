from django.contrib import admin

# Register your models here.
from persons.models import City, District, Person, Account

admin.site.register(City)
admin.site.register(District)
admin.site.register(Person)
admin.site.register(Account)