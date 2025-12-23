let students = JSON.parse(localStorage.getItem("students")) || [];

function render() {
  const list = document.getElementById("list");
  list.innerHTML = "";
  students.forEach((s, i) => {
    list.innerHTML += `
      <li>${s.name} - ${s.roll}
      <button onclick="remove(${i})">❌</button></li>`;
  });
}

function addStudent() {
  const name = document.getElementById("name").value;
  const roll = document.getElementById("roll").value;
  students.push({ name, roll });
  localStorage.setItem("students", JSON.stringify(students));
  render();
}

function remove(i) {
  students.splice(i, 1);
  localStorage.setItem("students", JSON.stringify(students));
  render();
}

render();
