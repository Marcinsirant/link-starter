from django.shortcuts import render
from djangoProject.models import Item


class ItemDTO:
    def __init__(self, id, name, url, description, image, parent, items, is_folder):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.image = image
        self.parent = parent
        self.items = items
        self.is_folder = is_folder

    def add_child(self, item):
        self.items.add(item)

    def __str__(self):
        return self.name + " [" + str(self.items) + "]"


def map_item_to_dto(item):
    return ItemDTO(
        id=item.id,
        name=item.name,
        url=item.url,
        description=item.description,
        image=item.image,
        parent=item.parent,
        items=set(),
        is_folder=item.is_folder()
    )


def convert_items_to_item_dtos(items):
    item_dtos = {}
    for item in items:
        item_dtos[item.id] = map_item_to_dto(item)

    for item in items:
        if item.parent is not None:
            parent_dto = item_dtos.get(item.parent.id)
            if parent_dto is not None:
                parent_dto.items.add(item_dtos[item.id])

    return {id: dto for id, dto in item_dtos.items() if dto.parent is None}


def show_base(request):
    items = Item.objects.all()
    dtos = convert_items_to_item_dtos(items)
    return render(request, 'base.html', {'items': dtos.values()})
