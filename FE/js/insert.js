async function postHoaDon(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}

window.addEventListener("load", (event) => {
  // postHoaDon("http://127.0.0.1:8000/hoadon/", testData).then((data) => {console.log(data.msg);});
  let addBtn = document.getElementsByClassName("add-chitiet w100")[0];
  let removeBtns = document.getElementsByClassName("remove-chitiet w100");
  let addHoaDon = document.getElementById("themhoadon");

  function removeHandler(e) {
    this.parentElement.remove();
  }

  function reAddRemoveEventListener() {
    for (let i = 0; i < removeBtns.length; ++i) {
      removeBtns[i].addEventListener("click", removeHandler);
    }
  }

  reAddRemoveEventListener();

  function addHandler(e) {
    addBtn.remove();
    let formRow = document.createElement("div");
    formRow.className = "form-row mt-1 chitiet-row";
    formRow.innerHTML = `
    <div class="col">
        <input type="text" class="form-control mahd" placeholder="Mã Hoá Đơn" required>
    </div>
    <div class="col">
        <input type="text" class="form-control masp" placeholder="Mã Sản Phẩm" required>
    </div>
    <div class="col">
        <input type="text" class="form-control soluong" placeholder="Số Lượng">
    </div>
    <div class="col">
        <input type="text" class="form-control giaban" placeholder="Giá Bán">
    </div>
    <div class="col">
        <input type="text" class="form-control giagiam" placeholder="Giá Giảm">
    </div>
    <div class="col">
        <input type="text" class="form-control thanhtien" placeholder="Thành Tiền">
    </div>
    <button type="button" class="btn btn-success add-chitiet w100">Add</button>
    <button type="button" class="btn btn-danger remove-chitiet w100">Remove</button>`;
    addHoaDon.appendChild(formRow);
    addBtn = document.getElementsByClassName("add-chitiet w100")[0];
    addBtn.addEventListener("click", addHandler);
    reAddRemoveEventListener();
  }

  addBtn.addEventListener("click", addHandler);

  let themhoadonform = document.getElementById("themhoadonform");

  function clearID(id) {
    document.getElementById(id).value = "";
  }
  function clearHoaDon() {
    clearID("hdmahd");
    clearID("hdmakh");
    clearID("ngaylap");
    clearID("tongtien");
  }
  function clearClasses(cls) {
    [...document.getElementsByClassName(cls)].map((c) => (c.value = ""));
  }
  function clearChiTietHoaDon() {
    clearClasses("mahd");
    clearClasses("masp");
    clearClasses("soluong");
    clearClasses("giaban");
    clearClasses("giagiam");
    clearClasses("thanhtien");
  }

  function clearThemHoaDon() {
    clearHoaDon();
    clearChiTietHoaDon();
  }

  themhoadonform.addEventListener("submit", (e) => {
    e.preventDefault();
    let hoadon = {
      MaHD: document.getElementById("hdmahd").value,
      MaKH: document.getElementById("hdmakh").value,
      NgayLap: document.getElementById("ngaylap").value,
      TongTien: document.getElementById("tongtien").value,
    };
    let cthoadon = [];
    let mahd = [...document.getElementsByClassName("mahd")].map(
      (mh) => mh.value
    );
    let masp = [...document.getElementsByClassName("masp")].map(
      (mk) => mk.value
    );
    let soluong = [...document.getElementsByClassName("soluong")].map(
      (sl) => sl.value
    );
    let giaban = [...document.getElementsByClassName("giaban")].map(
      (gb) => gb.value
    );
    let giagiam = [...document.getElementsByClassName("giagiam")].map(
      (gg) => gg.value
    );
    let thanhtien = [...document.getElementsByClassName("thanhtien")].map(
      (tt) => tt.value
    );
    for (let i = 0; i < mahd.length; ++i) {
      cthoadon.push({
        MaHD: mahd[i],
        MaSP: masp[i],
        SoLuong: soluong[i],
        GiaBan: giaban[i],
        GiaGiam: giagiam[i],
        ThanhTien: thanhtien[i],
      });
    }
    let data = {
      hoadon: hoadon,
      cthoadon: cthoadon,
    };
    postHoaDon("http://127.0.0.1:8000/hoadon/", data).then((data) => {
      console.log(data.msg);
    });
    clearThemHoaDon();
  });
});
