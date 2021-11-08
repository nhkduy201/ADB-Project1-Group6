import pyodbc


def read(conn, table_name, top=10):
    print("read begin")
    cursor = conn.cursor()
    cursor.execute(f"select top(10)* from {table_name}")
    for row in cursor:
        print(row)
    print("read end")


def create(conn, tab_col_name, values):
    print("create begin")
    cursor = conn.cursor()
    num_col = len(list(values[0]))
    que_marks = ((num_col - 1) * "?,") + "?"
    cursor.executemany(
        f"insert into {tab_col_name} values({que_marks});", values)
    conn.commit()
    print("create end")


def update(conn, table_name, column, condition, value):
    print("update begin")
    cursor = conn.cursor()
    cursor.execute(
        f"update {table_name} set {column} = ? where {condition};", value)
    conn.commit()
    print("update end")


def delete(conn, table_name, condition):
    print("delete begin")
    cursor = conn.cursor()
    cursor.execute(f"delete from {table_name} where {condition}")
    conn.commit()
    print("delete end")


conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-3SBUU7T;"  # replace with your server name
    "Database=QLHoaDon;"
    "Trusted_Connection=yes;"
)

read(conn, "KhachHang")


# INSERT
hoa_don = [
    ("HD500001", "KH54321", "2021-10-31 15:28:10.000", 23290000),
    ("HD500002", "KH12345", "2021-10-31 15:28:11.000", 23300000)
]
create(conn, "HoaDon", hoa_don)


update(conn, "CT_HoaDon", "SoLuong", "MaHD = 'HD000001'", "1234")


delete(conn, "HoaDon", "MaHD = 'HD500001' and MaKH = 'KH54321'")


conn.close()
