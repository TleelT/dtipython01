# โปรแกรมคำนวณราคาสินค้าที่รับส่วนลดแล้ว โดยป้อนรหัสสินค้า ชื่อสินค้า ประเภทสินค้า ซึ่งมี 4 ประเภท คือ food(F/f), woman(W/w), man(M/m), kitchen(K/k) 
# โดยป้อนเป็นตัวย่อ  และราคาสินค้าทางแป้นพิมพ์ แล้วคำนวณราคาสินค้าที่รับส่วนลดแล้วทางหน้าจอ 
# โดยสินค้าประเภท food ลด 2% ของราคาสินค้า, woman ลด 4% ของราคาสินค้า, man ลด 6% ของราคาสินค้า, kitchen ลด 10% ของราคาสินค้า 
# หากป้อนประเภทสินค้าผิดจากที่กำหนดให้แสดงข้อความ "คุณป้อนประเภทผิด !!!"

# โปรแกรมคำนวณราคาสินค้าหลังหักส่วนลด (แบบบิล)

# รับข้อมูลสินค้า
product_code = input("กรุณาใส่รหัสสินค้า: ")
product_name = input("กรุณาใส่ชื่อสินค้า: ")
product_type = input("กรุณาใส่ประเภทสินค้า (F/f, W/w, M/m, K/k): ")
price = float(input("กรุณาใส่ราคาสินค้า: "))

# ตรวจสอบประเภทสินค้าและคำนวณส่วนลด
if product_type.upper() == "F":
    discount = 0.02
    type_name = "Food"
elif product_type.upper() == "W":
    discount = 0.04
    type_name = "Woman"
elif product_type.upper() == "M":
    discount = 0.06
    type_name = "Man"
elif product_type.upper() == "K":
    discount = 0.10
    type_name = "Kitchen"
else:
    discount = None

# แสดงผล
if discount is not None:
    discounted_price = price * (1 - discount)
    print("\n===== รายละเอียดสินค้า =====")
    print(f"รหัสสินค้า     : {product_code}")
    print(f"ชื่อสินค้า     : {product_name}")
    print(f"ประเภทสินค้า  : {type_name}")
    print(f"ราคาก่อนลด    : {price:.2f} บาท")
    print(f"ส่วนลด         : {discount*100:.0f}%")
    print(f"ราคาหลังลด    : {discounted_price:.2f} บาท")
else:
    print("คุณป้อนประเภทผิด !!!")