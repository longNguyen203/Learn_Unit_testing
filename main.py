from pay.order import LineItem, Order
from pay.payment import pay_order


# Hệ thống chính

def main():
    # Test card number: 1249190007575069
    order = Order()
    
    # line_items là một list các sản phẩm
    
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00, quantity=5))
    order.line_items.append(LineItem(name="Chocopie", price=80_00))
    
    pay_order(order)
    
    
if __name__ == "__main__":
    main()