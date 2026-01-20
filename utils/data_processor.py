# utils/data_processor.py

def validate_transactions(data):
    valid = []
    invalid = []

    for item in data:
        try:
            quantity = int(item["Quantity"])
            unit_price = float(item["UnitPrice"])

            if quantity > 0 and unit_price > 0:
                item["Quantity"] = quantity
                item["UnitPrice"] = unit_price
                item["total"] = quantity * unit_price
                valid.append(item)
            else:
                invalid.append(item)

        except (KeyError, ValueError):
            invalid.append(item)

    return valid, invalid
