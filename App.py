def tinh_thue_tncn(thu_nhap_thang, so_nguoi_phu_thuoc):
    # Giảm trừ gia cảnh
    giam_tru_ban_than = 15_500_000
    giam_tru_phu_thuoc = so_nguoi_phu_thuoc * 6_200_000

    # Thu nhập tính thuế
    thu_nhap_tinh_thue = (
        thu_nhap_thang
        - giam_tru_ban_than
        - giam_tru_phu_thuoc
    )

    if thu_nhap_tinh_thue <= 0:
        return 0, thu_nhap_tinh_thue

    # Biểu thuế lũy tiến từng phần
    bac_thue = [
        (5_000_000, 0.05),
        (5_000_000, 0.10),
        (8_000_000, 0.15),
        (14_000_000, 0.20),
        (20_000_000, 0.25),
        (28_000_000, 0.30),
        (float("inf"), 0.35),
    ]

    thue = 0
    con_lai = thu_nhap_tinh_thue

    for muc, ty_le in bac_thue:
        if con_lai <= 0:
            break

        phan_chiu_thue = min(con_lai, muc)
        thue += phan_chiu_thue * ty_le
        con_lai -= phan_chiu_thue

    return thue, thu_nhap_tinh_thue


# Chương trình chính
print("=== ỨNG DỤNG TÍNH THUẾ THU NHẬP CÁ NHÂN ===")

thu_nhap = float(input("Nhập thu nhập tháng (VNĐ): "))
nguoi_phu_thuoc = int(input("Nhập số người phụ thuộc: "))

thue, tn_tinh_thue = tinh_thue_tncn(
    thu_nhap,
    nguoi_phu_thuoc
)

print("\nKẾT QUẢ")
print(f"Thu nhập tính thuế: {tn_tinh_thue:,.0f} VNĐ")
print(f"Thuế TNCN phải nộp: {thue:,.0f} VNĐ")
print(f"Thu nhập sau thuế: {thu_nhap - thue:,.0f} VNĐ")
