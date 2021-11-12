let page = 0;
const min_page = 0;
const max_page = 49999;

function getRowEle(mahd, makh, nl, tt) {
  let row = document.createElement("tr");
  row.className = "row100 body";
  row.innerHTML = `<td class="cell100 column1">${mahd}</td>
  <td class="cell100 column2">${makh}</td>
  <td class="cell100 column3">${nl}</td>
  <td class="cell100 column4">${tt}</td>`;
  return row;
}
function getHoaDon() {
  let tableContent = document.querySelector(
    "body > div.container-table100 > div > div > div.table100-body.js-pscroll > table > tbody"
  );
  fetch("http://127.0.0.1:8000/hoadon/" + page)
    .then((response) => response.json())
    .then((data) => {
      tableContent.innerHTML = "";
      for (let i = 0; i < data.hoadons.length; ++i) {
        let record = data.hoadons[i];
        tableContent.appendChild(
          getRowEle(record.MaHD, record.MaKH, record.NgayLap, record.TongTien)
        );
      }
    });
}

window.addEventListener("load", (event) => {
  getHoaDon();
  let prevBtn = document.getElementsByClassName("prev-btn")[0];
  let nextBtn = document.getElementsByClassName("next-btn")[0];
  prevBtn.addEventListener("click", () => {
    page -= 1;
    if (page < min_page) page = min_page;
    getHoaDon();
  });
  nextBtn.addEventListener("click", () => {
    page += 1;
    if (page > max_page) page = max_page;
    getHoaDon();
  });
});
