from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order) -> None:
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("please enter your card number: ")
    month = int(input("please enter the card expiry month: "))
    year = int(input("please enter the card expiry year: "))
    payment_processor = PaymentProcessor("")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()
