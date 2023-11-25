from constants import ___


def compose_full_name(first_name: ___, last_name: ___, middle_name: ___) -> ___:
    pass


if __name__ == "__main__":
    assert compose_full_name(first_name="John", last_name="Doe", middle_name=None) == "Doe John"
    assert compose_full_name(first_name="Ilya", last_name="Lebedev", middle_name="Alexeyevich") == "Lebedev Ilya Alexeyevich"
