from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyodbc
import json

@csrf_exempt
def gethoadon(request, page):
  page = int(page)
  hoadonperpage = 10
  conn=pyodbc.connect("Driver={SQL Server Native Client 11.0};"
    "Server=OLDLAP;"
    "Database=QLHoaDon;"
    "Trusted_Connection=yes;")
  cursor=conn.cursor()
  cursor.execute(f"select top({hoadonperpage}) * from HoaDon where MaHD not in (select top({page * hoadonperpage}) MaHD from HoaDon order by MaHD) order by MaHD")
  columns = [column[0] for column in cursor.description]
  results = []
  for row in cursor.fetchall():
     results.append(dict(zip(columns, row)))
  return JsonResponse({'hoadons': results})

@csrf_exempt
def posthoadon(request):
  print('Raw Data: "%s"' % request.body)
  return JsonResponse({"msg":"OK"})