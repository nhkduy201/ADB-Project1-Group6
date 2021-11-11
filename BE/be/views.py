from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyodbc
import json


def get_conn_cursor():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=OLDLAP;"
                          "Database=QLHoaDon;"
                          "Trusted_Connection=yes;")
    return (conn, conn.cursor())


@csrf_exempt
def gethoadon(request, page):
    page = int(page)
    hoadonperpage = 10
    cursor = get_conn_cursor()[1]
    cursor.execute(
        f"select top({hoadonperpage}) * from HoaDon where MaHD not in (select top({page * hoadonperpage}) MaHD from HoaDon order by MaHD) order by MaHD"
    )
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return JsonResponse({'hoadons': results})


@csrf_exempt
def posthoadon(request):
    data = json.loads(request.body)
    hoadon = data['hoadon']
    chitiets = data['cthoadon']
    conn, cursor = get_conn_cursor()
    cursor.execute(
        f"insert into HoaDon(MaHD, MaKH, NgayLap, TongTien) values ('{hoadon['MaHD']}','{hoadon['MaKH']}','{hoadon['NgayLap']}', {int(hoadon['TongTien'])})"
    )
    for i in range(len(chitiets)):
        cursor.execute(
            f"insert into CT_HoaDon(MaHD,MaSP,SoLuong,GiaBan,GiaGiam,ThanhTien) values ('{chitiets[i]['MaHD']}','{chitiets[i]['MaSP']}',{chitiets[i]['SoLuong']}, {chitiets[i]['GiaBan']},{chitiets[i]['GiaGiam']},{chitiets[i]['ThanhTien']})"
        )
    conn.commit()
    return JsonResponse({"msg": "OK"})
