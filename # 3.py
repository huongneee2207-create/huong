# 3. Tính lợi nhuận sau 12 tháng

so_tien_ban_dau = float(input("Nhập số tiền ban đầu: "))
lai_suat = float(input("Nhập lãi suất mỗi tháng (%): "))

so_tien = so_tien_ban_dau

for i in range(12):
    so_tien += so_tien * (lai_suat / 100)

loi_nhuan = so_tien - so_tien_ban_dau

print("Số tiền sau 12 tháng là:", so_tien)
print("Lợi nhuận là:", loi_nhuan)
