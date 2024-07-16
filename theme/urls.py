from django.urls import path

from theme.views import show_base, show_items

urlpatterns = [
    path('', show_base, name='base'),
    path('folders/<path:ids>/', show_items, name='folders'),

]
