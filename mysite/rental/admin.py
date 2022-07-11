from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User
admin.site.site_header ="ROOM ON RENT "
admin.site.index_title =" Dashboard"

admin.site.unregister(User)

admin.site.unregister(Group)
admin.site.register(Customer)
admin.site.register(putroom)
admin.site.register(Contact)
