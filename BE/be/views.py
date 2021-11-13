from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyodbc
import json

server_name = 'DESKTOP-C8FG3V2\SQLEXPRESS'#'OLDLAP'  


def get_conn_cursor():
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          f"Server={server_name};"
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


@csrf_exempt
def getRequest(request):
    results = request.GET.get('month_year')
    parse = results.split('/')
    month = int(parse[0])
    year = int(parse[1])
    cursor = get_conn_cursor()[1]
    cursor.execute(
        f"select * from HoaDon where Month(NgayLap) = {month} and Year(NgayLap) = {year}"
    )
    dictionary = {
        'mahd': '',
        'makh': '',
        'ngaylap': '',
        'tongtien': '',
        'tongdoanhthu': 0
    }
    count = 1
    for row in cursor:
        # dictionary[f'mahd{count}'] = row.MaHD
        # dictionary[f'makh{count}'] = row.MaKH
        # dictionary[f'ngaylap{count}'] = row.NgayLap
        # dictionary[f'tongtien{count}'] = row.TongTien
        dictionary['mahd'] += row.MaHD + " "
        dictionary['makh'] += row.MaKH + " "
        dictionary['ngaylap'] += row.NgayLap.strftime(
            "%Y/%m/%d, %H:%M:%S") + "; "
        dictionary['tongtien'] += str(row.TongTien) + " "
        dictionary['tongdoanhthu'] += row.TongTien
        count += 1
    dictionary['soluong'] = count - 1
    return render(request, 'statistic_detail.html', dictionary)