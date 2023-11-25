from constants import ___


def create_user(user_name: ___, user_age: ___, after_created: ___) -> ___:
    pass


def send_test_email(user_id: int) -> None:
    pass


if __name__ == "__main__":
    assert create_user(
        user_name="Ilya",
        user_age=32,
        after_created=send_test_email,
    ) is None
