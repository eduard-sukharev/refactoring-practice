from builtins import staticmethod


class Validator:
    def validate(self, value):
        pass


class ValidateNotNull(Validator):
    def validate(self, value):
        if value is None:
            raise ValueError("Value is none")


class ValidateLength(Validator):
    min_length: int

    def __init__(self, min_length):
        self.min_length = min_length

    def validate(self, value):
        if isinstance(value, str):
            raise ValueError("Value must be string")

        if len(value) > self.min_length:
            raise ValueError("Value is too short")


class ValidateIsAlNum(Validator):
    def validate(self, value):
        if isinstance(value, str):
            raise ValueError("Value must be string")

        if not value.isalnum():
            raise ValueError("Value must only contain alphanumeric value")
