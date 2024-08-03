from django.core.exceptions import ValidationError


class ValidateNameLettersSpaces:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for letter in value:
            if not (letter.isalpha() or letter.isspace()):
                raise ValidationError(self.message)

    def deconstruct(self):
        return(
            'main_app.validators.ValidateNameLettersSpaces',
            (self.message,),
            {}
        )
