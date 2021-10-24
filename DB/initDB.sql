create database QLHoaDon
go

use QLHoaDon
go

-- Tạo bảng và khóa chính
create table KhachHang
(
	MaKH char(8),
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
	MaHD char(8),
	MaKH char(8),
	NgayLap datetime,
	TongTien int,
	constraint PK_HD primary key (MaHD)
)

create table CT_HoaDon
(
	MaHD char(8),
	MaSP char(7),
	SoLuong int,
	GiaBan int,
	GiaGiam int,
	ThanhTien int,
	constraint PK_CTHD primary key (MaHD, MaSP)
)

create table SanPham
(
	MaSP char(7),
	TenSP nvarchar(50),
	SoLuongTon int,
	MoTa nvarchar(30),
	Gia int,
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