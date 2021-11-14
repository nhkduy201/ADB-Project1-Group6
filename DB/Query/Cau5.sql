use QLHoaDon
go

--a
select *
from HoaDon hd join CT_HoaDon ct on hd.MaHD = ct.MaHD join SanPham sp on ct.MaSP = sp.MaSP

select * 
from HoaDon hd, CT_HoaDon ct, SanPham sp
where hd.MaHD = ct.MaHD and ct.MaSP = sp.MaSP

--b
select *
from SanPham SP join CT_HoaDon CT
on SP.MaSP = CT.MaSP

select *
from CT_HoaDon CT join SanPham SP
on CT.MaSP = SP.MaSP
