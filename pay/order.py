from dataclasses import dataclass, field
from enum import Enum


class OrderStatus(Enum):
    OPEN = "open"
    PAID = "paid"
    
    
@dataclass # Đây cũng là một Decorator
class LineItem: # Class đại diện cho 1 sản phẩm trong đơn hàng
    name: str
    price: int
    quantity: int = 1 # Biến quantity có đối số mặc định là 1 khi không truyền đối số cho biến này thì
    # Nó sẽ có giá trị mặc định là 1
    # Ba biến này hoặc trường(field) giống với các thuộc tính trong 1 class bình thường
    
    @property
    def total(self) -> int: # Phương thức trả về số tiền cần thanh toán cho 1 sản phẩm ứng với số lượng của sản phẩm đó
        return self.price * self.quantity
    
    
@dataclass # Đây cũng là một Decorator
class Order: # class đại diện cho đơn hàng chứa nhiều sản phẩm với tên, giá, số lượng của mỗi sản phẩm
    line_items: list[LineItem] = field(default_factory=list) # Danh sách các sản phẩm trong 1 đơn hàng
    # default_factory=list được sử dụng để đặt giá trị mặc định là một list trống nếu không có giá trị được cung cấp.
    status: OrderStatus = OrderStatus.OPEN # trường trạng thái đại diện cho trạng thái đơn hàng được đặt giá trị mặc định là mở
    # Hai trường này đều được đặt giá trị mặc định
    
    @property
    def total(self) -> int: # Tính tổng giá trị các sản phẩm trong đơn hàng
        return sum(item.total for item in self.line_items)
    
    def pay(self) -> None: # Phương thức này cập nhật lại trạng thái đơn hàng
        self.status = OrderStatus.PAID