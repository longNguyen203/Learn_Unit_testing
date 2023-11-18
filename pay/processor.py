from datetime import datetime


class PaymentProcessor:
    
    """ Xử lý thanh toán """
    
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        
    def _check_api_key(self) -> bool: # Kiểm tra xem api_key có rỗng không
        return self.api_key == ""
        
    def charge(self, card: str, month: int, year: int, amount: int) -> None: # tham số amount đại diện cho số tiền cần thanh toán
        if not self.validate_card(card, month, year): # Nếu thẻ không dùng được
            raise ValueError("Invalid card")
        if not self._check_api_key():
            raise ValueError("Invalid API key")
        print(f"charging card number {card} for ${amount/100:.2f}")
    
    def validate_card(self, card: str, month: int, year: int) -> bool:
        # Phương thức này kiểm tra sự hợp lệ của số thẻ và kiểm thẻ còn hạn hay không bằng việc lấy thời hạn của thẻ trừ đi thời điểm hiện tại
        return self.luhn_checksum(card) and datetime(year, month, 1) > datetime.now()
    
    def luhn_checksum(self, card_number: str) -> bool: # Phương thức kiểm tra sự hợp lệ cả số thẻ
        def digits_of(card_nr: str) -> list: # Phương thức này nhận vào số thẻ của thẻ thanh toán
            return [int(d) for d in card_nr] # trả về một list các số của dãy thẻ
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2] # 37235982 -> 7392
        even_digits = digits[-2::-2] # 37235982 -> 3258
        checksum = 0
        checksum += sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(str(digit * 2)))
        
        return checksum % 10 == 0

