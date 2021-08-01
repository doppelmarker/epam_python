def check_power_of_2(a: int) -> bool:
    return not (bool(a & (a - 1))) if a != 0 else False
