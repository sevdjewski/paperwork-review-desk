import json
from pathlib import Path

project_dir = Path(__file__).resolve().parent

with (project_dir / "order.json").open(encoding="utf-8") as file:
    order = json.load(file)

with (project_dir / "invoice.json").open(encoding="utf-8") as file:
    invoice = json.load(file)

# Unsere Beispieldateien enthalten jeweils genau eine Position.
ordered_item = order["items"][0]
invoiced_item = invoice["items"][0]

if ordered_item["sku"] != invoiced_item["sku"]:
    raise SystemExit("Die Artikelnummern stimmen nicht überein.")

quantity_difference = invoiced_item["quantity"] - ordered_item["quantity"]

ordered_total = ordered_item["quantity"] * ordered_item["unit_price_cents"]
invoiced_total = invoiced_item["quantity"] * invoiced_item["unit_price_cents"]
amount_difference = invoiced_total - ordered_total

print(f"Artikel: {ordered_item['sku']}")
print(f"Mengenabweichung: {quantity_difference:+d} Stück")
print(f"Betragsabweichung: {amount_difference:+d} Cent")

ordered_total = ordered_item["quantity"] * ordered_item["unit_price_cents"]
invoiced_total = invoiced_item["quantity"] * invoiced_item["unit_price_cents"]
amount_difference = invoiced_total - ordered_total
