class CategoryNotFoundException(Exception):

    def __init__(self, category_id):
        super().__init__(f"Category with id '{category_id}' not found.")


class DuplicateCategoryException(Exception):

    def __init__(self, title):
        super().__init__(f"Category '{title}' is already present in the system.")
