"""Python Basic Functions Practice Module"""

################################################################################
# Advantages of Functions
################################################################################
# 1. Code Reusability: Functions allow you to reuse code without repeating it.
#    This promotes the DRY (Don't Repeat Yourself) principle.
#    And, demotes the WET (Write Everything Twice) principle.
# 2. Modularity: Functions help break down complex problems into smaller,
#    manageable parts.
# 3. Abstraction: Functions provide a way to hide implementation details and
#    expose only the necessary parts.
# 4. Testing and Debugging: Functions can be tested individually, making it
#    easier to identify and fix issues.
# 5. Improved Readability: Well-named functions can make code more readable
#    and self-documenting.
# 6. Enhanced Maintainability: Functions make it easier to update and maintain
#    code over time.
################################################################################


################################################################################
# Defining Functions
# def function_name(
#     positional_arguments,
#     *variable_arguments,
#     **keyword_arguments,
# ):
#     function_body
################################################################################
def send_notification(name, *notifications):
    print(f"Sending notification to {name}:")

    if not notifications:
        print("  - No new notifications!")
        return

    for msg in notifications:
        print(f"  - {msg}")


def send_email_notification(name, email_address, *notifications):
    print(f"Sending email to {name} ({email_address}):")

    if not notifications:
        print("  - No new notifications!")
        return

    for msg in notifications:
        print(f"  - {msg}")


def send_sms_notification(name, phone_number, *notifications):
    print(f"Sending SMS to {name} ({phone_number}):")

    if not notifications:
        print("  - No new notifications!")
        return

    for msg in notifications:
        print(f"  - {msg}")


def notify(name, *args, **kwargs):
    notification_type = kwargs.get("notification_type") if kwargs else None
    email_address = kwargs.get("email_address") if kwargs else None
    phone_number = kwargs.get("phone_number") if kwargs else None

    if notification_type == "email" and email_address:
        return send_email_notification(name, email_address, *args)
    elif notification_type == "sms" and phone_number:
        return send_sms_notification(name, phone_number, *args)
    else:
        return send_notification(name, *args)


notify(
    name="Alice",
    address="123 Main St",
)
notify(
    "Bob",
    "Your order has been shipped.",
    "Tracking number is 123456789",
)
notify(
    "Charlie",
    "Your package is out for delivery.",
    "Estimated delivery time is between 2 PM - 4 PM",
    notification_type="email",
    email_address="charlie@example.com",
)
notify(
    "David",
    "Your appointment is tomorrow at 10 AM.",
    "Please arrive 15 minutes early.",
    notification_type="sms",
    phone_number="+1234567890",
)
