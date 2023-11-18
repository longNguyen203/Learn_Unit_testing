from pay.order import LineItem

""" Để pytest có thể tìm được chính xác các file, các hàm kiểm thử thì các file kiểm thử phải nằm trong thư
mục test và tên các hàm kiểm thử phải bắt đầu bằng "test_" để pytest có thể tìm thấy và nhận ra """

def test_line_item_default() -> None:
    line_item = LineItem("Test", 500)
    assert line_item.total == 500
    
def test_line_item() -> None:
    line_item = LineItem("Test", 200, 5)
    assert line_item.total == 1000