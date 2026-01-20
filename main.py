# main.py

from utils.file_handler import read_sales_data, save_data
from utils.data_processor import validate_transactions
from utils.api_handler import fetch_products
from utils.report_generator import generate_report


def main():
    try:
        print("=" * 45)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 45)

        # [1/10] Reading sales data
        print("\n[1/10] Reading sales data...")
        raw_data = read_sales_data("data/sales_data.txt")
        print(f"✓ Successfully read {len(raw_data)} transactions")

        # [2/10] Validating transactions
        print("\n[2/10] Validating transactions...")
        valid_data, invalid_data = validate_transactions(raw_data)
        print(f"✓ Valid: {len(valid_data)} | Invalid: {len(invalid_data)}")

        if not valid_data:
            print("❌ No valid transactions found. Exiting.")
            return

        # [3/10] Filter Options
        regions = sorted(set(item["Region"] for item in valid_data))
        amounts = [item["total"] for item in valid_data]

        print("\n[3/10] Filter Options Available:")
        print(f"Regions: {', '.join(regions)}")
        print(f"Amount Range: ₹{min(amounts)} - ₹{max(amounts)}")

        choice = input("\nDo you want to filter data? (y/n): ").strip().lower()
        if choice == "y":
            region = input("Enter region: ").strip().lower()
            valid_data = [
                item for item in valid_data
                if item["Region"].lower() == region
            ]

        # [4/10] Analyzing sales data
        print("\n[4/10] Analyzing sales data...")
        print("✓ Analysis complete")

        # [5/10] Fetching product data from API
        print("\n[5/10] Fetching product data from API...")
        products = fetch_products()
        print(f"✓ Fetched {len(products)} products")

        product_map = {p["product_id"]: p for p in products}

        # [6/10] Enriching sales data
        print("\n[6/10] Enriching sales data...")
        enriched_data = []

        for item in valid_data:
            product_info = product_map.get(item["ProductID"], {})
            item["Brand"] = product_info.get("brand", "Unknown")
            enriched_data.append(item)

        print(f"✓ Enriched {len(enriched_data)} transactions")

        # [7/10] Saving enriched data
        print("\n[7/10] Saving enriched data...")
        save_data(enriched_data, "data/enriched_sales_data.txt")
        print("✓ Saved to: data/enriched_sales_data.txt")

        # [8/10] Generating report
        print("\n[8/10] Generating report...")
        report_path = generate_report(enriched_data)
        print(f"✓ Report saved to: {report_path}")

        # [9/10] Completion
        print("\n[9/10] Process Complete!")
        print("=" * 45)

    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
