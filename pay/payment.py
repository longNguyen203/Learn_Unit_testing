from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order) -> None: # Tham số đầu vào là một đơn hàng
    if order.total == 0: # Nếu đơn hàng có tổng số tiền bằng 0
        raise ValueError("Can't pay an order with total 0.")
    card = input("please enter your card number: ")
    month = int(input("please enter the card expiry month: "))
    year = int(input("please enter the card expiry year: "))
    payment_processor = PaymentProcessor("6cfb67f3-6281-4031-b893-ea85db0dce20") # PaymentProcessor nhận vào api key
    payment_processor.charge(card, month, year, amount=order.total) # kiểm tra và in ra số tiền cần thanh toán
    order.pay() # Cập nhật lại trạng thái đơn hàng
