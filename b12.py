ds = [1, 1, 2, 2, 2, 3, 3, 4, 4]
max_dem = 0 
so_nhieu_nhat = None
for so in ds:
    dem = ds.count(so)
    if dem > max_dem:
        max_dem= dem
        so_nhieu_nhat = so
print("số xuất hiện nhiều nhất:", so_nhieu_nhat)
print("số lần xuất hiện", max_dem)