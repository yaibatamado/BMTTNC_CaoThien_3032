# Main.py
from SinhVien import SinhVien
from QuanLySinhVien import QuanLySinhVien

def hien_thi_menu():
    """Hiển thị menu các chức năng cho người dùng."""
    print("\n--- CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN ---")
    print("1. Thêm sinh viên")
    print("2. Cập nhật thông tin sinh viên theo ID")
    print("3. Xóa sinh viên theo ID")
    print("4. Tìm kiếm sinh viên theo tên")
    print("5. Sắp xếp danh sách sinh viên theo điểm trung bình (Giảm dần)")
    print("6. Sắp xếp danh sách sinh viên theo tên chuyên ngành (A-Z)")
    print("7. Sắp xếp danh sách sinh viên theo tên (A-Z)")
    print("8. Hiển thị danh sách sinh viên")
    print("0. Thoát chương trình")
    print("------------------------------------")

def main():
    """Hàm chính chạy chương trình quản lý sinh viên."""
    qlsv = QuanLySinhVien()

    # Thêm một vài sinh viên mẫu (có thể xóa đi nếu không muốn)
    qlsv.them_sinh_vien(SinhVien("Nguyễn Hoàng Anh", "Nam", "Công nghệ Thông tin", 8.5))
    qlsv.them_sinh_vien(SinhVien("Trần Bảo Ngọc", "Nữ", "Kế toán", 7.0))
    qlsv.them_sinh_vien(SinhVien("Lê Minh Đức", "Nam", "Marketing", 6.2))
    qlsv.them_sinh_vien(SinhVien("Phạm Thu Trang", "Nữ", "Công nghệ Thông tin", 9.1))
    qlsv.them_sinh_vien(SinhVien("Vũ Gia Huy", "Nam", "Kỹ thuật Phần mềm", 7.8))


    while True:
        hien_thi_menu()
        try:
            lua_chon = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ. Vui lòng nhập một số.")
            continue

        if lua_chon == 1:
            print("\n--- Thêm sinh viên mới ---")
            try:
                ten = input("Nhập tên sinh viên: ")
                if not ten.strip(): # Kiểm tra tên không được để trống
                    print("Tên không được để trống.")
                    continue
                gioi_tinh = input("Nhập giới tính (Nam/Nữ/Khác): ")
                chuyen_nganh = input("Nhập chuyên ngành: ")
                diem_tb_str = input("Nhập điểm trung bình (0.0 - 10.0): ")
                diem_tb = float(diem_tb_str)
                if not (0.0 <= diem_tb <= 10.0):
                    print("Điểm trung bình không hợp lệ. Vui lòng nhập giá trị từ 0.0 đến 10.0.")
                    continue
                sv_moi = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_tb)
                qlsv.them_sinh_vien(sv_moi)
            except ValueError:
                print("Điểm trung bình không hợp lệ. Vui lòng nhập số.")
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")

        elif lua_chon == 2:
            print("\n--- Cập nhật thông tin sinh viên ---")
            try:
                sv_id_str = input("Nhập ID sinh viên cần cập nhật: ")
                sv_id = int(sv_id_str)
                sv_can_cap_nhat = qlsv.tim_sinh_vien_theo_id(sv_id)
                if sv_can_cap_nhat:
                    print(f"Thông tin hiện tại của sinh viên ID {sv_id}:")
                    print(sv_can_cap_nhat)
                    
                    ten_moi = input(f"Nhập tên mới (hiện tại: {sv_can_cap_nhat.ten}, bỏ trống nếu không đổi): ")
                    gioi_tinh_moi = input(f"Nhập giới tính mới (hiện tại: {sv_can_cap_nhat.gioi_tinh}, bỏ trống nếu không đổi): ")
                    chuyen_nganh_moi = input(f"Nhập chuyên ngành mới (hiện tại: {sv_can_cap_nhat.chuyen_nganh}, bỏ trống nếu không đổi): ")
                    diem_tb_moi_str = input(f"Nhập điểm TB mới (hiện tại: {sv_can_cap_nhat.diem_tb}, bỏ trống nếu không đổi): ")

                    # Chỉ cập nhật nếu người dùng nhập giá trị mới
                    ten_final = ten_moi if ten_moi.strip() else None
                    gioi_tinh_final = gioi_tinh_moi if gioi_tinh_moi.strip() else None
                    chuyen_nganh_final = chuyen_nganh_moi if chuyen_nganh_moi.strip() else None
                    diem_tb_final = None
                    if diem_tb_moi_str.strip():
                        try:
                            diem_tb_final = float(diem_tb_moi_str)
                            if not (0.0 <= diem_tb_final <= 10.0):
                                print("Điểm trung bình không hợp lệ. Sẽ không cập nhật điểm.")
                                diem_tb_final = None # Reset nếu không hợp lệ
                        except ValueError:
                            print("Định dạng điểm không hợp lệ. Sẽ không cập nhật điểm.")
                            diem_tb_final = None
                    
                    if any([ten_final, gioi_tinh_final, chuyen_nganh_final, diem_tb_final is not None]):
                         qlsv.cap_nhat_sinh_vien(sv_id, ten_final, gioi_tinh_final, chuyen_nganh_final, diem_tb_final)
                    else:
                        print("Không có thông tin nào được thay đổi.")
                else:
                    print(f"Không tìm thấy sinh viên có ID {sv_id}.")
            except ValueError:
                print("ID sinh viên không hợp lệ. Vui lòng nhập số.")
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")


        elif lua_chon == 3:
            print("\n--- Xóa sinh viên ---")
            try:
                sv_id_str = input("Nhập ID sinh viên cần xóa: ")
                sv_id = int(sv_id_str)
                qlsv.xoa_sinh_vien(sv_id)
            except ValueError:
                print("ID sinh viên không hợp lệ. Vui lòng nhập số.")
            except Exception as e:
                print(f"Có lỗi xảy ra: {e}")

        elif lua_chon == 4:
            print("\n--- Tìm kiếm sinh viên theo tên ---")
            ten_tk = input("Nhập tên sinh viên cần tìm: ")
            ket_qua_tk = qlsv.tim_kiem_sinh_vien_theo_ten(ten_tk)
            if ket_qua_tk:
                print(f"Tìm thấy {len(ket_qua_tk)} sinh viên:")
                for sv in ket_qua_tk:
                    print(sv)
                    print("-" * 10)
            else:
                print(f"Không tìm thấy sinh viên nào có tên chứa '{ten_tk}'.")

        elif lua_chon == 5:
            qlsv.sap_xep_theo_diem_tb()
            qlsv.hien_thi_danh_sach()

        elif lua_chon == 6:
            qlsv.sap_xep_theo_chuyen_nganh()
            qlsv.hien_thi_danh_sach()
            
        elif lua_chon == 7:
            qlsv.sap_xep_theo_ten()
            qlsv.hien_thi_danh_sach()

        elif lua_chon == 8:
            qlsv.hien_thi_danh_sach()

        elif lua_chon == 0:
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
