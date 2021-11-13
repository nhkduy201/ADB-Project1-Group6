--Nội dung: Thành tiền của một chi tiết hóa đơn phải tuân theo công thức: SoLuong * (GiaBan - GiaGiam)
--Phạm vi: CT_HoaDon
--Bảng tầm ảnh hưởng
-------------------------------------------------------------
--|   Bảng    |   Thêm   |   Xóa   |      Sửa                |   
-------------------------------------------------------------
--| CT_HoaDon |    +     |    -    | + (SoLuong, GiaBan      |
--|           |          |         |	GiaGiam, ThanhTien)  |
-------------------------------------------------------------

use QLHoaDon
go

create trigger trg_ct_hoadon_thanhtien on CT_HoaDon
for insert, update
as
begin
	if exists (select * from inserted I where SoLuong*(GiaBan-GiaGiam) <> ThanhTien)
	begin
		raiserror('Du lieu them vao khong hop le',16,1)
		Rollback transaction
	end
end
go

--INSERT [dbo].[CT_HoaDon] ([MaHD], [MaSP], [SoLuong], [GiaBan], [GiaGiam], [ThanhTien]) VALUES (N'HD000001', N'SP01345', 2, 23275000, 2327500, 20947500)

--UPDATE CT_HoaDon
--SET SoLuong = 2
--WHERE MaHD = 'HD000001' and MaSP = 'SP01344';

--UPDATE CT_HoaDon
--SET SoLuong = 3, ThanhTien = 62842500
--WHERE MaHD = 'HD000001' and MaSP = 'SP01344';
