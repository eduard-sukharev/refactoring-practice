from typing import Optional

from user import UserMd5Hash, User, PasswordVerification


def load_user_from_db(login) -> PasswordVerification:
    user = UserMd5Hash()
    user.login = login

    return user


def update_password_route(user: PasswordVerification, new_password: str):
    # Сохраняем новый пароль
    try:
        user.update_password(new_password)
    except Exception:
        return 'error.403'

    return 'my_profile'



def user_login_route(user: PasswordVerification):
    # Проверить пароль
    if user.password_match('Not my value'):
        raise Exception("Invalid value")


if '__main__' == __name__:
    # берём пользователя "из базы"
    user1 = load_user_from_db('username')
    user2 = load_user_from_db('foo')

    update_password_route(user1, 'SecretPassword')
