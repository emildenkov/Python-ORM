from django.core.exceptions import ValidationError


class ValidateMenuCategories:

    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if value not in ["Appetizers", "Main Course", "Desserts"]:
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.ValidateMenuCategories',
            (self.message,),
            {}
        )


def validate_menu_categories(value):
    if value not in ["Appetizers", "Main Course", "Desserts"]:
        raise ValidationError('The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')