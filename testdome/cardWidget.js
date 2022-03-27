// React is loaded and is available as React and ReactDOM
// imports should NOT be used
const Cards = (props) => {
  const handleClick = (e) => {
    if (e.target.innerHTML === "down") {
      for (let i = 0; i < props.amount; i++) {
        let tableData = document.getElementsByTagName("td")[i];
        if (tableData.innerHTML === "up") {
          tableData.innerHTML = "down";
        }
      }
      e.target.innerHTML = "up";
    }
  };

  const root = document.querySelector("#root");
  const table = document.createElement("table");
  const tbody = document.createElement("tbody");
  const tr = document.createElement("tr");

  for (let i = 0; i < props.amount; i++) {
    let td = document.createElement("td");
    td.innerHTML = "down";
    td.addEventListener("click", handleClick);
    tr.appendChild(td);
  }

  tbody.appendChild(tr);
  table.appendChild(tbody);
  root.appendChild(table);

  return null;
};

document.body.innerHTML = "<div id='root'> </div>";

const rootElement = document.getElementById("root");
ReactDOM.render(<Cards amount={4} />, rootElement);

let row = document.getElementById("root").getElementsByTagName("tr")[0];
if (row) {
  let cell = row.getElementsByTagName("td")[1];
  if (cell) {
    cell.click();
  }
}
setTimeout(() => console.log(document.getElementById("root").innerHTML));
