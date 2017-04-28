<!DOCTYPE html>
<html>
<head>
%upcasename = str.title(pagename)
<title>{{upcasename}}</title>
<link rel="stylesheet" type="text/css" href="/styles/dark-main.css" />
</head>
<body>

<div class="sideBar" style="display:none" id="mySidebar">
  <button class="barButton"
  onclick="sideBar_close()">&times;</button>
  <a href="/wiki/main" class="sideBarItem">Home</a>
  <a href="#" class="sideBarItem">About</a>
  <a href="#" class="sideBarItem">Contact</a>
</div>

<div zclass="main" id="main">

  <div class="topBar">
    <button class="topButton" onclick="sideBar_open()">&#9776;</button>
    <div class="container">
      <h1>{{upcasename}}</h1>
    </div>
  </div>


  <div class="bodytext" id="PageEntry">
      {{!bodytext}}
  </div>

</div>

<script>
function sideBar_open() {
  document.getElementById("main").style.marginLeft = "15%";
  document.getElementById("mySidebar").style.width = "15%";
  document.getElementById("mySidebar").style.display = "block";
}
function sideBar_close() {
  document.getElementById("main").style.marginLeft = "0%";
  document.getElementById("mySidebar").style.display = "none";
}
</script>

</body>
</html>
