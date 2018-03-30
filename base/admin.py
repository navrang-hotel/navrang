from django.contrib import admin

# Register your models here.

from .models import MenuCategory, MenuItem, Review, ContactMessage

admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Review)
admin.site.register(ContactMessage)

admin.site.site_header = 'Navrang Administration'

