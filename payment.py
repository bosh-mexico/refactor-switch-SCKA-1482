from enum import Enum

class PaymentMode(Enum):
    PAYPAL = 1
    GOOGLEPAY = 2
    CREDITCARD = 3

def checkout(mode: PaymentMode, amount: float):
    if not isinstance(mode, PaymentMode):
        print("Error: Invalid payment mode type!")
        return

    match mode:
        case PaymentMode.PAYPAL:
            print(f"Processing PayPal payment of ${amount:.2f}")
        case PaymentMode.GOOGLEPAY:
            print(f"Processing GooglePay payment of ${amount:.2f}")
        case PaymentMode.CREDITCARD:
            print(f"Processing Credit Card payment of ${amount:.2f}")
        case _:
            print("Invalid payment mode selected!")

def parse_payment_mode(mode_str: str) -> PaymentMode | None:
    try:
        return PaymentMode[mode_str.upper()]
    except KeyError:
        print(f"Error: Unsupported payment mode '{mode_str}'")
        return None

if __name__ == "__main__":
    amount = 150.75

    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)

    invalid_mode = parse_payment_mode("unknown")
    if invalid_mode:
        checkout(invalid_mode, amount)
