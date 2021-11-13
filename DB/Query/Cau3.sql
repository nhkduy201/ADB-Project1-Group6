use QLHoaDon
go

--a. Cho danh sách các hoá đơn lập trong năm 2020
select HD.MaHD, HD.MaKH
from HoaDon HD
where YEAR(HD.NgayLap) = 2020

--b. Cho danh sách các khách hàng ở TPHCM
select KH.MaKH, KH.Ho, KH.Ten
from KhachHang KH
where KH.ThanhPho = 'TP.HCM'

--c. Cho danh sách các sản phẩm có giá trong khoảng từ 10tr đến 25tr
select SP.MaSP, SP.TenSP
from SanPham SP
where SP.Gia between 10000000 and 25000000

--d. Cho danh sách các sản phẩm có số lượng tồn <100
select sp.MaSP,sp.TenSP
from SanPham sp
where sp.SoLuongTon < 100

--e. Cho danh sách các sản phẩm bán chạy nhất (số lượng bán nhiều nhất)
select ct.MaSP,(select sp.TenSP 
				from SanPham sp 
				where sp.MaSP = ct.MaSP) as TenSP , SUM(ct.SoLuong) as SLBan
from CT_HoaDon ct
group by ct.MaSP
having SUM(ct.SoLuong) = ( select MAX(Temp.SLBan)
							from (select SUM(SoLuong) as SLBan 
									from CT_HoaDon 
									group by MaSP ) as Temp )

--f. Cho danh sách các sản phẩm có doanh thu cao nhất
select ct.MaSP,(select sp.TenSP 
				from SanPham sp 
				where sp.MaSP = ct.MaSP) as TenSP , SUM(CAST(ct.ThanhTien as bigint)) as DoanhThu
from CT_HoaDon ct
group by ct.MaSP
having SUM(CAST(ct.ThanhTien as bigint)) = ( select MAX(Temp.DoanhThu)
											from (select SUM(CAST(ThanhTien as bigint)) as DoanhThu 
													from CT_HoaDon ct 
													group by MaSP ) as Temp)
