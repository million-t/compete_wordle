from api.repositories.word_repository import bulk_create

def bulk_create_usecase(word_objects):
    
    created = bulk_create(word_objects)
    if created is None:
        raise ValueError("Failed to create words")

    return created