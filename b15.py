import string 
doan_van = input("nhập một đoạn văn: ")
doan_van = doan_van.lower()
for dau in string.punctuation:
    doan_van = doan_van.replace(dau, "")
    tach_dv = doan_van.split()
    dem = {}
    for tu in tach_dv:
        if tu in dem:
            dem[tu] +=1
        else:
            dem[tu] = 1
ds_sap_xep = sorted(dem.items(), key=lambda x: x[1], reverse=True) 
print("tần suất xuất hiện của từng từ:")           
for tu, so_lan in ds_sap_xep:
    print(f"{tu}: {so_lan}")

