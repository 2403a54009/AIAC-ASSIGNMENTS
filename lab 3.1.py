"""#task1
def check_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime
  

  def calculate_data_charges(data_gb, plan_type):
    if plan_type.lower() == 'prepaid':
        return data_gb * 10  # ₹10 per GB
    elif plan_type.lower() == 'postpaid':
        return data_gb * 8   # ₹8 per GB
    else:
        raise ValueError("Invalid plan type")


def calculate_value_added_charges(services_list):
    charges = {
        'caller tune': 30,
        'ott subscription': 100,
        'roaming pack': 50
    }
    total = 0
    service_details = []
    
    for service in services_list:
        service = service.strip().lower()
        if service in charges:
            total += charges[service]
            service_details.append((service.title(), charges[service]))
        else:
            service_details.append((service.title(), 0))
    
    return total, service_details

#task2
def display_bill(plan_type, data_gb, data_charges, vc_total, vc_details, tax, total):
    print("\n--- Mobile Data Usage Bill ---")
    print(f"Plan Type: {plan_type.title()}")
    print(f"Data Used: {data_gb:.2f} GB")
    print(f"Data Charges: ₹{data_charges:.2f}")
    
    print("\nValue-Added Services:")
    for service, charge in vc_details:
        print(f" - {service}: ₹{charge}")
    print(f"Value-Added Charges: ₹{vc_total:.2f}")

    print(f"\nTax (18%): ₹{tax:.2f}")
    print(f"\nTotal Bill: ₹{total:.2f}")
    print("------------------------------\n")


def main():
    try:
        data_gb = float(input("Enter data consumed (in GB): "))
        if data_gb < 0:
            raise ValueError("Data consumed cannot be negative.")

        plan_type = input("Enter plan type (Prepaid/Postpaid): ").strip().lower()
        if plan_type not in ["prepaid", "postpaid"]:
            raise ValueError("Plan type must be 'Prepaid' or 'Postpaid'.")

        services_input = input("Enter additional services used (comma-separated): ")
        services_list = services_input.split(",") if services_input else []

        # Calculations
        data_charges = calculate_data_charges(data_gb, plan_type)
        vc_total, vc_details = calculate_value_added_charges(services_list)
        subtotal = data_charges + vc_total
        tax = 0.18 * subtotal
        total = subtotal + tax

        # Display bill
        display_bill(plan_type, data_gb, data_charges, vc_total, vc_details, tax, total)

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()"""
#task3
import random

# Price list
cylinder_prices = {
    "Domestic 14.2 kg": 905.00,
    "Domestic 5 kg": 335.50,
    "Commercial 19 kg": 1886.50,
    "Commercial 47.5 kg": 4712.00
}

def main():
    print("----- LPG Billing System -----")

    # Get cylinder type
    print("\nAvailable Cylinder Types:")
    for cyl in cylinder_prices:
        print(f"- {cyl}")
    cylinder_type = input("Enter Cylinder Type: ").strip()

    # Validate cylinder type
    if cylinder_type not in cylinder_prices:
        print("Invalid Cylinder Type. Please choose from the list.")
        return

    # Get number of cylinders
    try:
        quantity = int(input("Enter number of cylinders booked: "))
        if quantity <= 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Please enter a positive integer.")
        return

    # Get subsidy (only for domestic)
    subsidy = 0.0
    if cylinder_type.startswith("Domestic"):
        try:
            subsidy = float(input("Enter Subsidy Amount (₹): "))
            if subsidy < 0:
                raise ValueError
        except ValueError:
            print("Invalid subsidy amount.")
            return

    # Price per cylinder
    price_per_cylinder = cylinder_prices[cylinder_type]

    # Random delivery charges
    delivery_charges = random.randint(10, 50)

    # Calculate base amount and total
    base_amount = price_per_cylinder * quantity
    total_bill = base_amount - subsidy + delivery_charges

    # Display itemized bill
    print("\n----- ITEMIZED BILL -----")
    print(f"Cylinder Type     : {cylinder_type}")
    print(f"Quantity          : {quantity}")
    print(f"Price per Cylinder: ₹{price_per_cylinder:.2f}")
    print(f"Base Amount       : ₹{base_amount:.2f}")
    print(f"Subsidy           : ₹{subsidy:.2f}")
    print(f"Delivery Charges  : ₹{delivery_charges:.2f}")
    print(f"Total Bill Amount : ₹{total_bill:.2f}")
    print("--------------------------")

if __name__ == "__main__":
    main()
