# utils/file_handler.py

def read_sales_data(file_path):
    """
    Reads pipe-separated sales data and returns list of dictionaries
    """
    data = []

    with open(file_path, "r", encoding="utf-8") as file:
        headers = file.readline().strip().split("|")

        for line in file:
            values = line.strip().split("|")

            if len(values) != len(headers):
                continue

            record = dict(zip(headers, values))
            data.append(record)

    return data


def save_data(data, file_path):
    """
    Saves enriched sales data as pipe-separated file
    """
    if not data:
        return

    headers = list(data[0].keys())

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("|".join(headers) + "\n")

        for item in data:
            row = [str(item[h]) for h in headers]
            file.write("|".join(row) + "\n")
