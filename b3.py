chuoi = input("nhập một chuỗi ")
chuoi = chuoi.lower()
nguyen_am = "aeiou"
so_nguyen_am = 0 
so_phu_am = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():
        if ky_tu in nguyen_am:
            so_nguyen_am += 1
        else:
            so_phu_am += 1
print("số nguyên âm:", so_nguyen_am)
print("số phụ âm:", so_phu_am)