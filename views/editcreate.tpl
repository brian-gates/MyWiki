<!DOCTYPE html>
<html>
  <head>
    %upcasename = str.title(pagename)
    <title>Create: {{upcasename}}</title>
    <link rel="stylesheet" type="text/css" href="/styles/dark-main.css" />
  </head>
  <body>

    <div class="sideBar" style="display:none" id="mySidebar">
      <button class="barButton"
      onclick="sideBar_close()">&times;</button>
      <a href="/wiki/main" class="sideBarItem">Home</a>
      <a href="/wiki/about" class="sideBarItem">About</a>
      <a href="#" class="sideBarItem">Contact</a>
    </div>

    <div zclass="main" id="main">

      <div class="topBar">
        <button class="topButton" onclick="sideBar_open()">&#9776;</button>
        <div class="container">
          <h1>MyWiki</h1>
        </div>
      </div>

      <div class="header">
        <div class="container">
          <h2>Create: {{upcasename}}</h2>
        </div>
      </div>


      <div class="bodytext" id="PageEntry">
        <p>
          <form action="/edit/{{pagename}}", method="POST">
            <textarea name="PageData" rows="25" cols="100" placeholder="Enter wiki text..." required></textarea>
            <input type="Submit" value="Publish" />
            <div  id="cancel-button">
              <a href="/wiki/{{pagename}}">Cancel</a>
            </div>
          </form>
        </p>
      </div>
    </div>


<!--begin footer and scripts -->

    <div class="articlefoot">
      <a href="#" class="footerbox">Delete</a>
      <a href="#" class="footerbox">Rename</a>
      <a href="#" class="footerbox">Edit</a>
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
