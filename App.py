def tinh_thue_tncn(thu_nhap_thang, so_nguoi_phu_thuoc):
    # Giảm trừ gia cảnh
    giam_tru_ban_than = 11000000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 4400000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = thu_nhap_thang - giam_tru_ban_than - giam_tru_phu_thuoc

    if thu_nhap_tinh_thue <= 0:
        return 0

    bac_thue = [
        (5000000, 0.05),
        (5000000, 0.10),
        (8000000, 0.15),
        (14000000, 0.20),
        (20000000, 0.25),
        (28000000, 0.30),
        (float('inf'), 0.35)
    ]

    thue = 0
    con_lai = thu_nhap_tinh_thue

    for muc, ty_le in bac_thue:
        if con_lai > 0:
            phan_chiu_thue = min(con_lai, muc)
            thue += phan_chiu_thue * ty_le
            con_lai -= phan_chiu_thue
        else:
            break

    return thue


# Chương trình chính
print("=== TÍNH THUẾ THU NHẬP CÁ NHÂN ===")

thu_nhap = float(input("Nhập thu nhập tháng (VNĐ): "))
phu_thuoc = int(input("Nhập số người phụ thuộc: "))

thue = tinh_thue_tncn(thu_nhap, phu_thuoc)

print(f"\nThuế TNCN phải nộp: {thue:,.0f} VNĐ")
print(f"Thu nhập sau thuế: {thu_nhap - thue:,.0f} VNĐ")
