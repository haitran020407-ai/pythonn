cac_so = list(map(int, input("nhập các số nguyên cách nhau bằng dấu cách:").split()))
khong_trung = list(set(cac_so))
print("danh sách các số không trùng:", khong_trung)