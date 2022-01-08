from django.contrib import admin
from .models import User,Customer,Product,Cart,OrderPlaced

# Register your models here.
# class Userform(forms.FormModel):
#     class Meta:
#         model = User
#         fields=""

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display =['id','title','selling_price','discount_price','description','brand','category','product_img']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']