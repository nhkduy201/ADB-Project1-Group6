use QLHoaDon
go

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