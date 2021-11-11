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
  let addBtn = document.getElementsByClassName("add-chitiet")[0];
  let removeBtns = document.getElementsByClassName("remove-chitiet");
  let addHoaDon = document.getElementById("themhoadon");
  let lastAddBtn = document.querySelector("#last-add-chitiet");
  lastAddBtn.addEventListener("click", (e) => {
    lastAddBtn.classList.add("invisible");
    addAction();
  });
  function removeHandler(e) {
    let curRevBtn = document.getElementsByClassName("remove-chitiet");
    if (curRevBtn.length == 1) {
      lastAddBtn.classList.remove("invisible");
      this.parentElement.remove();
      return;
    }
    if (this.previousElementSibling.classList.contains("add-chitiet")) {
      let lastInputs = this.parentElement.querySelectorAll("input");
      let prevLastInputs =
        this.parentElement.previousElementSibling.querySelectorAll("input");
      for (let i = 0; i < lastInputs.length; ++i) {
        lastInputs[i].value = prevLastInputs[i].value;
      }
      this.parentElement.previousElementSibling.remove();
    } else {
      this.parentElement.remove();
    }
  }

  function reAddRemoveEventListener() {
    for (let i = 0; i < removeBtns.length; ++i) {
      removeBtns[i].addEventListener("click", removeHandler);
    }
  }

  reAddRemoveEventListener();
  function addAction() {
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
    <!-- <div class="col">
        <input type="text" class="form-control thanhtien" placeholder="Thành Tiền">
    </div> -->
    <button type="button" class="btn btn-success add-chitiet"><i class="fas fa-plus"></i></button>
    <button type="button" class="btn btn-danger remove-chitiet"><i class="fas fa-minus"></i></button>`;
    addHoaDon.appendChild(formRow);
    addBtn = document.getElementsByClassName("add-chitiet")[0];
    let curRevBtn = document.getElementsByClassName("remove-chitiet");
    if (curRevBtn.length == 2) {
      curRevBtn[0].style.display = "block";
      curRevBtn[0].style.width = "100px";
      addBtn.style.width = "47.5px";
      addBtn.style.marginRight = "5px";
    }
    addBtn.addEventListener("click", addHandler);
    reAddRemoveEventListener();
  }
  function addHandler(e) {
    this.remove();
    addAction();
  }

  addBtn.addEventListener("click", addHandler);

  let themhoadonform = document.getElementById("themhoadonform");

  function clearThemHoaDon() {
    [...document.querySelectorAll("#themhoadon input")].map(
      (inp) => (inp.value = "")
    );
  }

  function getHoaDon() {
    return {
      MaHD: document.getElementById("hdmahd").value,
      MaKH: document.getElementById("hdmakh").value,
      NgayLap: document.getElementById("ngaylap").value,
      TongTien: 0,
      // TongTien: document.getElementById("tongtien").value,
    };
  }

  function getThanhTien(soluong, giaban, giagiam) {
    let thanhtien = [];
    for (let i = 0; i < soluong.length; ++i) {
      thanhtien.push(soluong[i] * (giaban[i] - giagiam[i]));
    }
    return thanhtien;
  }

  function getChiTiet() {
    let cthoadon = [];
    let mahd = [...document.getElementsByClassName("mahd")].map(
      (mh) => mh.value
    );
    let masp = [...document.getElementsByClassName("masp")].map(
      (mk) => mk.value
    );
    let soluong = [...document.getElementsByClassName("soluong")].map((sl) =>
      parseInt(sl.value)
    );
    let giaban = [...document.getElementsByClassName("giaban")].map((gb) =>
      parseInt(gb.value)
    );
    let giagiam = [...document.getElementsByClassName("giagiam")].map((gg) =>
      parseInt(gg.value)
    );
    // let thanhtien = [...document.getElementsByClassName("thanhtien")].map(
    //   (tt) => tt.value
    // );
    let thanhtien = getThanhTien(soluong, giaban, giagiam);
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
    return cthoadon;
  }

  themhoadonform.addEventListener("submit", (e) => {
    e.preventDefault();
    let hoadon = getHoaDon();
    let cthoadon = getChiTiet();
    postHoaDon("http://127.0.0.1:8000/hoadon/", {
      hoadon: hoadon,
      cthoadon: cthoadon,
    }).then((res) => {
      console.log(res.msg);
    });
    clearThemHoaDon();
  });
});
