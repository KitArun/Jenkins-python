# main.py

def calculate_total(price, quantity):
    """คำนวณราคารวมสินค้า"""
    if price < 0 or quantity < 0:
        raise ValueError("ราคาสินค้าและจำนวนต้องไม่ติดลบ")
    return price * quantity

def apply_discount(total, discount_code):
    """คำนวณส่วนลดตามโค้ด"""
    if discount_code == "WELCOME10":
        return total * 0.9  # ลด 10%
    elif discount_code == "SUPER50":
        return total * 0.5  # ลด 50%
    return total

def is_valid_username(username):
    """ตรวจสอบชื่อผู้ใช้ (ต้องยาวกว่า 3 ตัวอักษร)"""
    return len(username) > 3

if __name__ == "__main__":
    # จำลองการทำงาน
    price_item = 100
    qty = 2
    total = calculate_total(price_item, qty)
    final_price = apply_discount(total, "WELCOME10")
    
    print(f"--- Shopping System ---")
    print(f"Total: {total} THB")
    print(f"Final Price after discount: {final_price} THB")