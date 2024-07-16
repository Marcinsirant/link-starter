from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db import models
from django.shortcuts import redirect


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def is_folder(self):
        return not self.url

    def check_for_cycle(self):
        seen_items = set()
        current_item = self
        while current_item is not None:
            if current_item.id is not None and current_item.id in seen_items:
                return True
            seen_items.add(current_item.id)
            current_item = current_item.parent
        return False

    def __str__(self):
        return self.id.__str__() + " " + self.name


class ItemAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            if obj.parent is not None and not obj.parent.is_folder():
                raise ValidationError("The parent of an Item must be a folder.")
            if obj.check_for_cycle():
                raise ValidationError("A cycle was detected in the Item hierarchy.")

            super().save_model(request, obj, form, change)
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect(request.path)


admin.site.register(Item, ItemAdmin)
