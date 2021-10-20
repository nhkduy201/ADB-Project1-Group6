create database QLHoaDon

use QLHoaDon

go

-- Tạo bảng và khóa chính
create table KhachHang
(
	MaKH char(6),
	Ho nvarchar(10),
	Ten nvarchar(50),
	NgSinh datetime,
	SoNha nvarchar(30),
	Duong nvarchar(30),
	Phuong nvarchar(30),
	Quan nvarchar(30),
	ThanhPho nvarchar(30),
	DienThoai char(10), 
	constraint PK_KH primary key (MaKH)
)

create table HoaDon
(
	MaHD char(6),
	MaKH char(6),
	NgayLap datetime,
	TongTien float,
	constraint PK_HD primary key (MaHD)
)

create table CT_HoaDon
(
	MaHD char(6),
	MaSP char(5),
	SoLuong int,
	GiaBan float,
	GiaGiam float,
	ThanhTien float,
	constraint PK_CTHD primary key (MaHD, MaSP)
)

create table SanPham
(
	MaSP char(5),
	TenSP nvarchar(50),
	SoLuongTon int,
	MoTa nvarchar(30),
	Gia float,
	constraint PK_SP primary key (MaSP)
)

-- Tạo khóa ngoại
alter table HoaDon
add constraint FK_HD_KH
foreign key (MaKH)
references KhachHang(MaKH)

alter table CT_HoaDon
add constraint FK_CTHD_HD
foreign key (MaHD)
references HoaDon(MaHD)

alter table CT_HoaDon
add constraint FK_CTHD_SP
foreign key (MaSP)
references SanPham(MaSP)