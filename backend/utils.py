PLATFORM_FEES = {
    "X": {"rate": 0.10, "fixed": 0},
    "Y": {"rate": 0.08, "fixed": 2},
    "Z": {"rate": 0.12, "fixed": 0},
}
CONDITION_MAP = {
    "X": {"New": "New", "Good": "Good", "Scrap": "Scrap"},
    "Y": {"New": "3 stars", "Good": "2 stars", "Scrap": "1 star"},
    "Z": {"New": "New", "Good": "Good", "Scrap": "As New"},
}

def get_platform_fee(platform):
    return PLATFORM_FEES.get(platform)

def map_condition(condition, platform):
    return CONDITION_MAP.get(platform, {}).get(condition, None)

def calc_platform_price(base_price, platform, fee_info, manual_override=None):
    if manual_override and manual_override.get(platform):
        return manual_override[platform], None
    rate = fee_info["rate"]
    fixed = fee_info["fixed"]
    try:
        price = (base_price + fixed) / (1 - rate)
    except ZeroDivisionError:
        return None, "Invalid platform fee"
    if price < 0:
        return None, "Invalid price calculation"
    return round(price, 2), None
