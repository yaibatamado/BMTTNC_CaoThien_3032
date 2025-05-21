# SinhVien.py

class SinhVien:
    """
    Lớp SinhVien dùng để lưu trữ thông tin của một sinh viên.
    Mã sinh viên (id) sẽ tự động tăng cho mỗi đối tượng mới.
    """
    _id_counter = 0  # Biến static để theo dõi ID tự tăng

    def __init__(self, ten: str, gioi_tinh: str, chuyen_nganh: str, diem_tb: float):
        """
        Hàm khởi tạo cho lớp SinhVien.

        Args:
            ten (str): Tên của sinh viên.
            gioi_tinh (str): Giới tính của sinh viên.
            chuyen_nganh (str): Chuyên ngành của sinh viên.
            diem_tb (float): Điểm trung bình (hệ 10) của sinh viên.
        """
        SinhVien._id_counter += 1
        self._id = SinhVien._id_counter  # Mã sinh viên tự động tăng
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb
        self.hoc_luc = self._xep_loai_hoc_luc()

    @property
    def id(self) -> int:
        """Getter cho thuộc tính id (chỉ đọc)."""
        return self._id

    def _xep_loai_hoc_luc(self) -> str:
        """
        Phương thức nội bộ để xếp loại học lực dựa trên điểm trung bình.

        Returns:
            str: Xếp loại học lực (Giỏi, Khá, Trung bình, Yếu).
        """
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def cap_nhat_thong_tin(self, ten: str = None, gioi_tinh: str = None, chuyen_nganh: str = None, diem_tb: float = None):
        """
        Cập nhật thông tin cho sinh viên.
        Chỉ cập nhật các trường được cung cấp (khác None).

        Args:
            ten (str, optional): Tên mới. Defaults to None.
            gioi_tinh (str, optional): Giới tính mới. Defaults to None.
            chuyen_nganh (str, optional): Chuyên ngành mới. Defaults to None.
            diem_tb (float, optional): Điểm trung bình mới. Defaults to None.
        """
        if ten is not None:
            self.ten = ten
        if gioi_tinh is not None:
            self.gioi_tinh = gioi_tinh
        if chuyen_nganh is not None:
            self.chuyen_nganh = chuyen_nganh
        if diem_tb is not None:
            self.diem_tb = diem_tb
            self.hoc_luc = self._xep_loai_hoc_luc() # Cập nhật lại học lực nếu điểm thay đổi

    def __str__(self) -> str:
        """
        Phương thức hiển thị thông tin sinh viên dưới dạng chuỗi.

        Returns:
            str: Chuỗi biểu diễn thông tin sinh viên.
        """
        return (f"ID: {self._id}\n"
                f"  Tên: {self.ten}\n"
                f"  Giới tính: {self.gioi_tinh}\n"
                f"  Chuyên ngành: {self.chuyen_nganh}\n"
                f"  Điểm TB: {self.diem_tb}\n"
                f"  Học lực: {self.hoc_luc}")

if __name__ == '__main__':
    # Ví dụ sử dụng lớp SinhVien (chỉ để kiểm tra)
    sv1 = SinhVien("Nguyễn Văn A", "Nam", "Công nghệ Thông tin", 7.5)
    print(sv1)
    print("-" * 20)
    sv2 = SinhVien("Trần Thị B", "Nữ", "Kinh tế", 8.2)
    print(sv2)
    print("-" * 20)
    sv1.cap_nhat_thong_tin(diem_tb=8.5)
    print("Sau khi cập nhật điểm cho SV1:")
    print(sv1)
