--Nội dung: TongTien của HoaDon phải bằng tổng tất cả ThanhTien của tất cả các CT_HoaDon
--Phạm vi: HoaDon, CT_HoaDon
--Bảng tầm ảnh hưởng
-------------------------------------------------
--|   Bảng   |   Thêm   |   Xóa   |      Sửa      |   
-------------------------------------------------
--|  HoaDon  |    +     |    -    | + (TongTien)  |
-------------------------------------------------
--| CT_HoaDon|    +     |    +    | + (MaHD,      |
--|          |          |         |	ThanhTien)  |
-------------------------------------------------

use QLHoaDon
go

create trigger trg_hoadon_tongtien on HoaDon
for insert, update
as
begin
	if not exists (
		select * from Inserted I where
		I.TongTien = (select isnull(sum(ThanhTien), 0) from CT_HoaDon CHD where CHD.MaHD = I.MaHD)
	)
	begin
		raiserror('Tong tien thay doi khong hop le',16,1)
		Rollback transaction
	end
end

go

create trigger trg_ct_hoadon on CT_HoaDon
for insert, delete, update
as
begin
	update HoaDon 
	set TongTien = (select isnull(sum(ThanhTien), 0) from CT_HoaDon CHD where CHD.MaHD = HoaDon.MaHD)
	where MaHD in ((select distinct MaHD from inserted) union (select distinct MaHD from deleted))
end

-----------------------------------------------------------------------------------

--go
---- drop table TMP_HoaDon
--select top(100) * into TMP_HoaDon from HoaDon
--alter table TMP_HoaDon
--add constraint PK_TMP_HoaDon primary key (MaHD)
---- drop table TMP_CT_HoaDon
--select CHD.* into TMP_CT_HoaDon from TMP_HoaDon TH join CT_HoaDon CHD on TH.MaHD = CHD.MaHD
--alter table TMP_CT_HoaDon
--add constraint PK_TMP_CT_HoaDon primary key (MaHD, MaSP)
--alter table TMP_CT_HoaDon
--add constraint FK_TMP_CT_HoaDon foreign key (MaHD) references TMP_HoaDon(MaHD)
--go
--drop trigger trg_ct_tmp_hoadon 
--go
--create trigger trg_ct_tmp_hoadon on TMP_CT_HoaDon
--for insert, delete, update
--as
--begin
--	update TMP_HoaDon 
--	set TongTien = (select sum(ThanhTien) from TMP_CT_HoaDon where MaHD = TMP_HoaDon.MaHD)
--	where MaHD in ((select distinct MaHD from inserted) union (select distinct MaHD from deleted))
--end

--create table tmp_mahd1(MaHD char(8));
--insert into tmp_mahd1 (MaHD)
--values
--	('HD000001'),
--	('HD000002'),
--	('HD000003'),
--	('HD000004'),
--	('HD000005');

--create table tmp_mahd2(MaHD char(8))

--insert into tmp_mahd2 (MaHD)
--values
--	('HD000006'),
--	('HD000007'),
--	('HD000008'),
--	('HD000009'),
--	('HD000010');

--update TMP_HoaDon
--set TongTien = 0

--update TMP_HoaDon 
--set TongTien = (select sum(ThanhTien) from TMP_CT_HoaDon where MaHD = TMP_HoaDon.MaHD)
--where MaHD in ((select distinct MaHD from tmp_mahd1) union (select distinct MaHD from tmp_mahd2))

--insert into TMP_CT_HoaDon(MaHD, MaSP, SoLuong, GiaBan, GiaGiam, ThanhTien)
--values
--	('HD000002','SP05084',6,1160000,116000,6264000);

--delete from TMP_CT_HoaDon
--where MaHD = 'HD000002' and MaSP = 'SP05084'