import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def store_user_data(filename, name, email, password):
    hashed_pw = hash_password(password)
    with open(filename, 'a') as f:
        f.write(f"{name},{email},{hashed_pw}\n")

def main():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    store_user_data("users.txt", name, email, password)
    print("User data stored securely.")

if __name__ == "__main__":
    main()

#task3
def is_armstrong_number(number):
    
    Check if a number is an Armstrong number.
    An Armstrong number is an n-digit number that is equal to the sum of its own digits
    each raised to the power of n.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
    
    # Convert the number to a string to easily iterate over digits
    digits = str(number)
    # Find the number of digits (n)
    num_digits = len(digits)
    # Calculate the sum of each digit raised to the power of n
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    # Compare the sum to the original number
    return armstrong_sum == number

# Explanation:
# 1. The function takes an integer 'number' as input.
# 2. It converts the number to a string to access each digit.
# 3. It calculates how many digits are in the number.
# 4. It computes the sum of each digit raised to the power of the number of digits.
# 5. It returns True if this sum equals the original number (Armstrong number), else False.

# Example usage:
# print(is_armstrong_number(153))  # Output: True
# print(is_armstrong_number(123))  # Output: False

#task4
def bubble_sort(arr):
    
    Bubble Sort Algorithm:
    - Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    - This process is repeated until the list is sorted.
    - Time Complexity: O(n^2) in the worst and average case.
    
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quick_sort(arr):
    
    QuickSort Algorithm:
    - Selects a 'pivot' element and partitions the array into two sub-arrays:
      elements less than the pivot and elements greater than the pivot.
    - Recursively applies the same logic to the sub-arrays.
    - Time Complexity: O(n log n) on average, but O(n^2) in the worst case.
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choose the first element as pivot
        less = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
        greater = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
        # Recursively sort sub-arrays and combine
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Comparison:
# - Bubble Sort is simple but inefficient for large lists (O(n^2)), as it repeatedly compares and swaps adjacent elements.
# - QuickSort is more efficient on average (O(n log n)), using divide-and-conquer to sort sublists around a pivot.
# - Bubble Sort sorts in-place, while this QuickSort implementation returns a new sorted list.
# - QuickSort is generally preferred for performance, except for very small or nearly sorted datasets.

#task5
def recommend_products(user_preferences, products):
    
    Recommend products based on user preferences and provide explanations.

    Args:
        user_preferences (dict): User's preferences, e.g., {'category': 'laptop', 'brand': 'Dell'}
        products (list): List of product dicts, each with keys like 'name', 'category', 'brand', 'price'

    Returns:
        list of tuples: (product, explanation)
    
    recommendations = []
    for product in products:
        reasons = []
        if 'category' in user_preferences and product.get('category') == user_preferences['category']:
            reasons.append(f"Matches your preferred category: {user_preferences['category']}")
        if 'brand' in user_preferences and product.get('brand') == user_preferences['brand']:
            reasons.append(f"Matches your preferred brand: {user_preferences['brand']}")
        if 'max_price' in user_preferences and product.get('price', float('inf')) <= user_preferences['max_price']:
            reasons.append(f"Within your budget: {user_preferences['max_price']}")
        if reasons:
            explanation = "; ".join(reasons)
            recommendations.append((product, explanation))
    return recommendations

# Example usage:
products = [
    {'name': 'Dell Inspiron', 'category': 'laptop', 'brand': 'Dell', 'price': 700},
    {'name': 'HP Pavilion', 'category': 'laptop', 'brand': 'HP', 'price': 650},
    {'name': 'Apple MacBook Air', 'category': 'laptop', 'brand': 'Apple', 'price': 1200},
    {'name': 'Dell Monitor', 'category': 'monitor', 'brand': 'Dell', 'price': 200},
]

user_preferences = {'category': 'laptop', 'brand': 'Dell', 'max_price': 800}

recommendations = recommend_products(user_preferences, products)
for product, explanation in recommendations:
    print(f"Recommended: {product['name']} - Reason: {explanation}")

# Evaluation:
# The explanations are understandable as they directly reference the user's stated preferences,
# such as category, brand, and price. Each recommendation is accompanied by clear reasons.

#task6
def factorial(n):

    
    Calculate the factorial of a non-negative integer n using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.

    The function works as follows:
    - If n is 0 or 1, return 1 (base case).
    - Otherwise, return n multiplied by the factorial of (n-1) (recursive case).
    
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Summary:
# The function calls itself with a decremented value of n until it reaches the base case (n == 0 or n == 1).
# Each recursive call multiplies n by the factorial of (n-1), building up the result as the call stack unwinds.

#task7
def generate_support_message(name, issue, title=None):
    """
    Generate a neutral, user-friendly support message.

    Args:
        name (str): The user's name.
        issue (str): The issue the user is facing.
        title (str, optional): Preferred title (e.g., "Dr.", "Mx.", "Ms.", "Mr."). Defaults to None.

    Returns:
        str: A support message.
    """
    salutation = f"Dear {title + ' ' if title else ''}{name},"
    message = (
        f"{salutation}\n\n"
        "Thank you for reaching out to our support team. "
        f"We have received your request regarding: \"{issue}\".\n"
        "Our team will review your inquiry and get back to you as soon as possible.\n\n"
        "Best regards,\nCustomer Support"
    )
    return message

# Example usage:
# print(generate_support_message("Alex", "Unable to reset password"))
# print(generate_support_message("Jordan", "Billing issue", title="Mx."))