from theme.models import Item


class ItemDTO:
    def __init__(self, name, id=None, url=None, description=None, image=None, parent=None, items=None, is_folder=None):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.image = image
        self.parent = parent
        self.items = items
        self.is_folder = is_folder

    def __str__(self):
        return self.name + " [" + str(self.items) + "]"


def map_item_to_dto(item: Item) -> ItemDTO:
    return ItemDTO(
        id=item.id,
        name=item.name,
        url=item.url,
        description=item.description,
        image=item.image,
        parent=item.parent,
        is_folder=item.is_folder()
    )
