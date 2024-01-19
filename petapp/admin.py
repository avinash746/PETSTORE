from django.contrib import admin

# Register your models here.
from petapp.models import contact,Product,OrderUpdate,Orders
admin.site.register(contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
