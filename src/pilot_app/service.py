from pilot_app.calculator import add


def total(values: list[int]) -> int:
    return sum(add(value, 0) for value in values)
