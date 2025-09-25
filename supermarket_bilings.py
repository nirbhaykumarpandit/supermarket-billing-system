"""
Supermarket Billing System
Author : Your Name
Description :
A simple billing app for supermarket items.
Features:
 - Add multiple items
 - Discount & tax support
 - Save bills to CSV
"""

import csv
from datetime import datetime

BILL_FILE = "bills.csv"

def get_customer_items():
    """
    Collects items for the current customer.
    Returns:
        items (list): [[name, price, qty, unit, amount], ...]
        subtotal (float)
    """
    items = []
    subtotal = 0.0

    while True:
        try:
            item_name = input("Enter item name: ").strip()
            price = float(input("Enter price of item: "))
            quantity = float(input("Enter quantity: "))
            unit = input("Enter unit (kg/liter/pcs): ").strip()

            amount = price * quantity
            items.append([item_name, price, quantity, unit, amount])
            subtotal += amount
        except ValueError:
            print("❌ Please enter valid numeric value for price/quantity!")
            continue

        more = input("Add more items? (yes/no): ").strip().lower()
        if more == "no":
            break
    return items, subtotal


def print_bill(name, items, subtotal, discount, tax):
    """Prints the final bill nicely formatted."""
    tax_amt = subtotal * tax / 100
    disc_amt = subtotal * discount / 100
    total = subtotal + tax_amt - disc_amt

    print("\n" + "=" * 60)
    print("SUPER MARKET BILL".center(60))
    print("=" * 60)
    print(f"Customer Name : {name}")
    print(f"Date & Time   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    print(f"{'Item':15}{'Price':>8}{'Qty':>8}{'Unit':>8}{'Amount':>14}")
    print("-" * 60)

    for item in items:
        print(f"{item[0]:15}{item[1]:>8.2f}{item[2]:>8.2f}{item[3]:>8}{item[4]:>14.2f}")

    print("-" * 60)
    print(f"{'Sub Total:':>48} {subtotal:>10.2f}")
    print(f"{'Tax ('+str(tax)+'%):':>48} {tax_amt:>10.2f}")
    print(f"{'Discount ('+str(discount)+'%):':>48} -{disc_amt:>9.2f}")
    print("-" * 60)
    print(f"{'Grand Total:':>48} {total:>10.2f}")
    print("=" * 60)
    print("******* Thank You! Happy Shopping ********")
    print("=" * 60 + "\n")

    return total


def save_bill_to_csv(name, items, total):
    """Appends the bill to a CSV file for record keeping."""
    with open(BILL_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for item in items:
            writer.writerow([date_time, name, item[0], item[1], item[2], item[3], item[4], total])


def main():
    print("=" * 60)
    print("WELCOME TO SUPER MARKET BILLING SYSTEM".center(60))
    print("=" * 60)
    print("Press Enter to start billing or type 'q' to quit.")
    start = input("> ").strip().lower()
    if start == "q":
        print("Goodbye 👋")
        return

    while True:
        customer_name = input("\nEnter customer's name: ").strip()
        items, subtotal = get_customer_items()

        try:
            discount = float(input("Enter discount (%) [0 for none]: ") or 0)
            tax = float(input("Enter tax/GST (%) [0 for none]: ") or 0)
        except ValueError:
            discount, tax = 0, 0

        grand_total = print_bill(customer_name, items, subtotal, discount, tax)
        save_bill_to_csv(customer_name, items, grand_total)

        repeat = input("Do you want to bill next customer? (yes/no): ").strip().lower()
        if repeat == "no":
            print("\nThank you for using Supermarket Billing System! Goodbye 👋")
            break


if __name__ == "__main__":
    main()
