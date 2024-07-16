from django.shortcuts import render

from theme.item_dto import ItemDTO, map_item_to_dto
from theme.models import Item


def show_base(request):
    item = ItemDTO(name="Wszsystkie aplikacje")
    children_items = [map_item_to_dto(item) for item in Item.objects.filter(parent=None)]
    context = {
        'parent': item,
        'children': children_items,
        'is_master': True,
    }
    return render(request, 'folder.html', context)


def show_items(request, ids=None):
    if ids:
        ids = [int(id) for id in ids.split('/') if id.isdigit()]
        last_id = ids[-1]
    else:
        ids = []
        last_id = None

    is_master = ("folders/" not in request.build_absolute_uri())

    item = map_item_to_dto(Item.objects.get(id=last_id))
    children_items = [map_item_to_dto(item) for item in Item.objects.filter(parent=item.id)]

    context = {
        'parent': item,
        'children': children_items,
        'is_master': is_master
    }

    return render(request, 'folder.html', context)
