class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, courses=[]):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.courses = courses

    def dangKyKhoaHoc(self, khoaHoc):
        print('khoaHoc: ', khoaHoc)

    def hienThiKhoaHoc(self):
        print(f'Các khoá đã đăng ký')
        print(self.courses)


class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        print(f"""
            Thông tin khoá:
            ID: {self.maKhoaHoc}
            Tên: {self.tenKhoaHoc}
            Hình thức: {self.hinhThuc}
            Học phí: {self.hocPhi}
        """)


# Init values
hocVien1 = HocVien(1, "Nguyen Van A", "23/2/2020")
hocVien1 = HocVien(2, "Den Thi Giau", "2/11/1923")

khoaHoc1 = KhoaHoc(1, "Làm bánh", "offline", 1000)
khoaHoc2 = KhoaHoc(2, "Lái xe", "online", 8000)

khoaHoc1.thongTinKhoaHoc()
khoaHoc2.thongTinKhoaHoc()

# features
hocVien1.dangKyKhoaHoc([khoaHoc1])
