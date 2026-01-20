# utils/report_generator.py

def generate_report(enriched_data, output_path="output/sales_report.txt"):
    """
    Generates a sales report using available fields
    """

    total_transactions = len(enriched_data)
    total_revenue = sum(item["total"] for item in enriched_data)

    # Revenue by Region (since Category does not exist)
    region_summary = {}
    for item in enriched_data:
        region = item["Region"]
        region_summary[region] = region_summary.get(region, 0) + item["total"]

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("SALES ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total Transactions: {total_transactions}\n")
        file.write(f"Total Revenue: ₹{total_revenue:.2f}\n\n")

        file.write("Revenue by Region:\n")
        for region, revenue in region_summary.items():
            file.write(f"- {region}: ₹{revenue:.2f}\n")

    return output_path
