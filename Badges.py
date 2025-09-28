import csv
from datetime import datetime
from xml.dom import pulldom
from collections import defaultdict
import sys

def parse_and_count_badges(xml_file, output_csv, year, month):
   
    user_badges = defaultdict(lambda: {"gold": 0, "silver": 0, "bronze": 0})
    events = pulldom.parse(xml_file)

    for event, node in events:
        if event == pulldom.START_ELEMENT and node.tagName == "row":
            events.expandNode(node)

            user_id = node.getAttribute("UserId")
            badge_class = node.getAttribute("Class")
            creation_date = datetime.strptime(node.getAttribute("Date"), "%Y-%m-%dT%H:%M:%S.%f")

            if creation_date.year == int(year) and creation_date.month == int(month):
                badge_map = {"1": "gold", "2": "silver", "3": "bronze"}
                badge_type = badge_map.get(badge_class)
                user_badges[user_id][badge_type] += 1

    year_month = f"{year}-{str(month).zfill(2)}"
    rows = [
        (user_id, year_month, badges["gold"], badges["silver"], badges["bronze"])
        for user_id, badges in user_badges.items()
    ]

    # Save results to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["User ID", "Year/Month", "#Gold", "#Silver", "#Bronze"])
        writer.writerows(rows)

    print(f"Results saved to {output_csv} (Total Users: {len(user_badges)})")

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python badges.py <xml_file> <output_file> <year> <month>")
        sys.exit(1)

    xml_file = sys.argv[1]
    output_file = sys.argv[2]
    year = sys.argv[3]
    month = sys.argv[4]

    parse_and_count_badges(xml_file, output_file, year, month)
