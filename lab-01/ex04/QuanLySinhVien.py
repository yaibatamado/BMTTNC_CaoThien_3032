# QuanLySinhVien.py
from typing import List, Optional
from SinhVien import SinhVien # Import lớp SinhVien từ file SinhVien.py

class QuanLySinhVien:
    """
    Lớp QuanLySinhVien dùng để quản lý danh sách các sinh viên.
    Bao gồm các chức năng: thêm, cập nhật, xóa, tìm kiếm, sắp xếp và hiển thị.
    """

    def __init__(self):
        """Hàm khởi tạo, tạo một danh sách rỗng để lưu trữ sinh viên."""
        self._danh_sach_sv: List[SinhVien] = []

    def them_sinh_vien(self, sv: SinhVien) -> None:
        """
        Thêm một đối tượng SinhVien vào danh sách.

        Args:
            sv (SinhVien): Đối tượng sinh viên cần thêm.
        """
        self._danh_sach_sv.append(sv)
        print(f"Đã thêm sinh viên '{sv.ten}' (ID: {sv.id}) thành công.")

    def tim_sinh_vien_theo_id(self, sv_id: int) -> Optional[SinhVien]:
        """
        Tìm kiếm sinh viên trong danh sách dựa trên ID.

        Args:
            sv_id (int): ID của sinh viên cần tìm.

        Returns:
            Optional[SinhVien]: Đối tượng SinhVien nếu tìm thấy, None nếu không.
        """
        for sv in self._danh_sach_sv:
            if sv.id == sv_id:
                return sv
        return None

    def cap_nhat_sinh_vien(self, sv_id: int, ten: str = None, gioi_tinh: str = None, chuyen_nganh: str = None, diem_tb: float = None) -> bool:
        """
        Cập nhật thông tin cho sinh viên dựa trên ID.

        Args:
            sv_id (int): ID của sinh viên cần cập nhật.
            ten (str, optional): Tên mới.
            gioi_tinh (str, optional): Giới tính mới.
            chuyen_nganh (str, optional): Chuyên ngành mới.
            diem_tb (float, optional): Điểm trung bình mới.

        Returns:
            bool: True nếu cập nhật thành công, False nếu không tìm thấy sinh viên.
        """
        sv = self.tim_sinh_vien_theo_id(sv_id)
        if sv:
            sv.cap_nhat_thong_tin(ten, gioi_tinh, chuyen_nganh, diem_tb)
            print(f"Đã cập nhật thông tin cho sinh viên ID {sv_id}.")
            return True
        else:
            print(f"Không tìm thấy sinh viên có ID {sv_id} để cập nhật.")
            return False

    def xoa_sinh_vien(self, sv_id: int) -> bool:
        """
        Xóa sinh viên khỏi danh sách dựa trên ID.

        Args:
            sv_id (int): ID của sinh viên cần xóa.

        Returns:
            bool: True nếu xóa thành công, False nếu không tìm thấy sinh viên.
        """
        sv = self.tim_sinh_vien_theo_id(sv_id)
        if sv:
            self._danh_sach_sv.remove(sv)
            print(f"Đã xóa sinh viên '{sv.ten}' (ID: {sv_id}) khỏi danh sách.")
            return True
        else:
            print(f"Không tìm thấy sinh viên có ID {sv_id} để xóa.")
            return False

    def tim_kiem_sinh_vien_theo_ten(self, ten_tk: str) -> List[SinhVien]:
        """
        Tìm kiếm sinh viên trong danh sách dựa trên tên (không phân biệt hoa thường, tìm kiếm gần đúng).

        Args:
            ten_tk (str): Tên sinh viên cần tìm kiếm.

        Returns:
            List[SinhVien]: Danh sách các sinh viên phù hợp với tên tìm kiếm.
        """
        ket_qua = []
        ten_tk_lower = ten_tk.lower()
        for sv in self._danh_sach_sv:
            if ten_tk_lower in sv.ten.lower():
                ket_qua.append(sv)
        return ket_qua

    def sap_xep_theo_diem_tb(self, giam_dan: bool = True) -> None:
        """
        Sắp xếp danh sách sinh viên theo điểm trung bình.

        Args:
            giam_dan (bool, optional): True để sắp xếp giảm dần, False để tăng dần. Defaults to True.
        """
        self._danh_sach_sv.sort(key=lambda sv: sv.diem_tb, reverse=giam_dan)
        print("Đã sắp xếp danh sách sinh viên theo điểm trung bình.")

    def sap_xep_theo_chuyen_nganh(self, giam_dan: bool = False) -> None:
        """
        Sắp xếp danh sách sinh viên theo tên chuyên ngành (alphabetical).

        Args:
            giam_dan (bool, optional): True để sắp xếp Z-A, False để A-Z. Defaults to False.
        """
        self._danh_sach_sv.sort(key=lambda sv: sv.chuyen_nganh.lower(), reverse=giam_dan)
        print("Đã sắp xếp danh sách sinh viên theo tên chuyên ngành.")
        
    def sap_xep_theo_ten(self, giam_dan: bool = False) -> None:
        """
        Sắp xếp danh sách sinh viên theo tên (alphabetical).

        Args:
            giam_dan (bool, optional): True để sắp xếp Z-A, False để A-Z. Defaults to False.
        """
        self._danh_sach_sv.sort(key=lambda sv: sv.ten.lower(), reverse=giam_dan)
        print("Đã sắp xếp danh sách sinh viên theo tên.")


    def hien_thi_danh_sach(self) -> None:
        """Hiển thị thông tin của tất cả sinh viên trong danh sách."""
        if not self._danh_sach_sv:
            print("Danh sách sinh viên hiện đang trống.")
            return
        print("\n--- DANH SÁCH SINH VIÊN ---")
        for sv in self._danh_sach_sv:
            print(sv)
            print("-" * 20)
            
    @property
    def danh_sach_sv(self) -> List[SinhVien]:
        """Getter cho danh sách sinh viên (chỉ đọc, trả về một bản sao)."""
        return list(self._danh_sach_sv)


if __name__ == '__main__':
    # Ví dụ sử dụng lớp QuanLySinhVien (chỉ để kiểm tra)
    qlsv = QuanLySinhVien()

    # Thêm sinh viên
    sv1 = SinhVien("Lê Văn C", "Nam", "Cơ khí", 6.8)
    sv2 = SinhVien("Phạm Thị D", "Nữ", "Quản trị Kinh doanh", 9.0)
    sv3 = SinhVien("Hoàng Văn E", "Nam", "Công nghệ Thông tin", 7.9)
    
    qlsv.them_sinh_vien(sv1)
    qlsv.them_sinh_vien(sv2)
    qlsv.them_sinh_vien(sv3)

    qlsv.hien_thi_danh_sach()

    # Cập nhật
    qlsv.cap_nhat_sinh_vien(sv_id=1, diem_tb=7.2, chuyen_nganh="Cơ điện tử")
    qlsv.hien_thi_danh_sach()

    # Tìm kiếm theo tên
    print("\n--- KẾT QUẢ TÌM KIẾM THEO TÊN 'Văn' ---")
    ket_qua_tk = qlsv.tim_kiem_sinh_vien_theo_ten("Văn")
    if ket_qua_tk:
        for sv in ket_qua_tk:
            print(sv)
            print("-" * 10)
    else:
        print("Không tìm thấy sinh viên nào.")

    # Sắp xếp theo điểm TB
    qlsv.sap_xep_theo_diem_tb()
    qlsv.hien_thi_danh_sach()

    # Sắp xếp theo chuyên ngành
    qlsv.sap_xep_theo_chuyen_nganh()
    qlsv.hien_thi_danh_sach()
    
    # Sắp xếp theo tên
    qlsv.sap_xep_theo_ten()
    qlsv.hien_thi_danh_sach()

    # Xóa sinh viên
    qlsv.xoa_sinh_vien(2) # Xóa sinh viên có ID là 2 (Phạm Thị D)
    qlsv.hien_thi_danh_sach()
    
    qlsv.xoa_sinh_vien(10) # Thử xóa ID không tồn tại
