from pay.processor import PaymentProcessor
import pytest


API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"

def test_api_key_invalid() -> None: # Kỳ vọng nó sẽ gây ra lỗi giá trị (ValueError)
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2024, 100)
        
    
def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2024, 100)
    
    
def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 2015, 100)
    

def test_card_number_invalid_luhn() -> None:
    payment_processor = PaymentProcessor(API_KEY)
    assert not payment_processor.luhn_checksum("1249190007575068")
    
    
def test_card_number_valid_luhn() -> None: 
    payment_processor = PaymentProcessor(API_KEY)
    assert payment_processor.luhn_checksum("1249190007575069")
    
    
def test_charge_card_valid() -> None:
    payment_processor = PaymentProcessor(API_KEY)
    payment_processor.charge("1249190007575069", 12, 2024, 100)
    
    
def test_charge_card_invalid() -> None:
    with pytest.raises(ValueError):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("1249190007575068", 12, 2024, 100)