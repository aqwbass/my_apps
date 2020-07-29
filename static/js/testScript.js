// Single line comment
//***** file testScript.js ถูก test-script.html import ไปใช้ *******
/* This multi lines comment
you can comment many lines as you want*/

var a = 10; //number
var b = 20;
var result = a + b;
var newA = "10"; //string
var newB = "20";
var newResult = newA + newB;
console.log("Total1", result);
console.log("Total2", newResult);

// Loop
for (let i = 1; i <= 10; i++) {
  console.log("i =", i);
}

// Create a funtion
function getNum() {
  var var1 = 10;
  var var2 = 20;
  var result = var1 + var2;
  console.log("result is: ", result);// console.log()เป็นการแสดง debug สามรถดูได้ใน f12 ในหน้าเว็บ

}

//Call function
getNum();

function myFunc1() {
  document.getElementById("id1").innerHTML = "change to stack python";
  /* document.getElementById("ชื่อid").innerHTML = ตามด้วย variable ต่างๆ
  / document.getElementById("ชื่อid").innerHTML เป็นฟังชั่นที่ทำให้ tag ที่เราตั้ง id นั้นไว้
  แสดงข้อความตามที่เรากรอกหลัง 
  เช่น 
  document.getElementById("id1").innerHTML = "change to stack python"
  ก็จะแสดงข้อความ change to stack python ตรง tag id นั้น ใน html
  */
}
function myFunc2() {
  document.getElementById("id2").style.fontSize = "100px";
  /* document.getElementById("id2").style.fontSize = "100px"; เป็นการเปลี่ยน ขนาดข้อความ
  ของ id นั้น เป็น 100 px  */
}
// Conditional statement and function
function myFunc3() {
  var msg;
  if (confirm("You must click to continue")) {/* confirm("{ข้อความ}") เป็นการสร้าง pop up แจ้งเตือน มีข้อความแสดง มี 
  มีปุ่ม ok กับ cancel
  */
    msg = "You pressed OK";
  } 
  else {
    msg = "You pressed CANCEL";
  }
  document.getElementById("id3").innerHTML = msg;
}
