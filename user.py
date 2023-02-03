import abc
from abc import abstractmethod

from hashlib import md5
from typing import List

from validator import Validator, ValidateIsAlNum, ValidateLength, ValidateNotNull


class Validation:
    validators: List[Validator]

    def validate(self, value: str):
        for validator in self.validators:
            validator.validate(value)


class PasswordVerification(abc.ABC):
    pwd_hash: str

    def update_password(self, new_password: str) -> None:
        validation = Validation()
        validation.validate(new_password)
        self.pwd_hash = self.hash(new_password)

    def password_match(self, password: str) -> bool:
        return self.pwd_hash == self.hash(password)

    @abstractmethod
    def hash(self, password: str) -> str:
        pass


class User:
    login: str


class UserWithPasswordHash(User, PasswordVerification):
    def hash(self, password: str) -> str:
        return hex(hash(password))

    def get_validators(self) -> List[Validator]:
        return [
            ValidateLength(10),
            ValidateIsAlNum(),
            ValidateNotNull(),
        ]


class UserMd5Hash(User, PasswordVerification):
    def hash(self, password: str) -> str:
        return md5(password).hexdigest()

    def get_validators(self) -> List[Validator]:
        return [
            ValidateLength(7),
            ValidateNotNull(),
        ]
