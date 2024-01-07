from django.contrib import admin

# Register your models here.
from arkapp.models import Product,Orders,OrderUpdate

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
# admin.site.register(Contact)
# admin.site.register(Orders)
