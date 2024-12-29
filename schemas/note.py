

def noteEntity(item) -> dict:
    return {
        '_id': str(item['_id']),
        'title': item['title'],
        'description': item['description'],
        'important': item.get('important', False),
    }


def notesEntity(items) -> list[dict]:
    return [noteEntity(item) for item in items]
