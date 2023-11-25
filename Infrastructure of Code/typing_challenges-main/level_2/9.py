import datetime

from constants import ___


def parse_receipt(raw_receipt: ___) -> ___:
    pass


if __name__ == "__main__":
    assert parse_receipt(
        raw_receipt="Кассовый чек 12 Продажа Позиции: ...",
    ) == (12, datetime.date(2022, 6, 12), [("Молоко", 1, 32.2)])
