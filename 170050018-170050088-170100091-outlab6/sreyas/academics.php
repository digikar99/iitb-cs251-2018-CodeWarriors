<!doctype html>
<html lang="en">
  <head>
    <link rel="icon" href="webicon.jpeg">
    <title>Academics</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="custom.css">


    <style>
    body {font-family: Arial;
          background-image: url("book_1.jpg");}
  .main-nav
  {
    color: white;
    font-size:15px;
    margin-top: 30px;
    text-align: center;
  }
  .main-nav li
{
  color: white;
  display: inline-block;
}

.main-nav li.active a
{
    border: 1px solid white;
    background-color: darkorange;
    
}
.main-nav li a:hover
{
    border: 1px solid white;
}

.main-nav li a
{
    color: white;
    text-decoration: none;
    padding: 5px 20px;
    font-family: "Roboto", sans-serif;
    font-size: 15px;
}

.container
{
  color: white;
}


    .accordion {
        background-color:darkorange;
        color: #444;
        cursor: pointer;
        padding: 5px;
        width: 100%;
        text-align: left;
        border: none;
        outline: none;
        transition: 0.4s;
    }

    /* Add a background color to the button if it is clicked on (add the .active class with JS), and when you move the mouse over it (hover) */
    .active, .accordion:hover {
        background-color:red;
    }

    /* Style the accordion panel. Note: hidden by default */
    .panel {
        margin-bottom:5px;
        margin-top: 5px;
        background: rgba(204, 204, 204, 0.5);
        display: none;
        overflow: hidden;
        color: white;
    }
    thead, th{
      background-color:#111;
      color:#fff;
    }
    table{
      margin-top:20px;
      text-align:center;
    }
  </style>
    
  </head>
  <body>


    <ul class="main-nav">
    <li><a href="index.php"> HOME </a></li> 
    <li><a href="interests.html"> INTERESTS </a></li>
    <li><a href="project.html"> PROJECTS </a></li>
    <li><a href="https://www.cse.iitb.ac.in/~sbayare/cs251.php"> TEAM </a></li>
    <li ><a href="contact.html"> CONTACTS </a></li>
    <li class="active"><a href="academics.php"> ACADEMICS </a></li>
    <li><a href="comment.html"> COMMENT </a></li>
    <li><a href="view_comments.php"> COLLECTION </a></li>
    </ul>


    <!-- The whole page - START-->
    <div class="container-fluid">
      <div class="row">

          <div class="col-md-2"></div>

         <!-- Sidebar | Navbar - Start -->
         <div id="nav-placeholder"></div>
         <!-- Sidebar | Navbar - End -->
         
          <div class="col-sm-8 col-md-6 col-xs-12 tall-pg" id="main">

            <div class="visible-xs" style="text-align:center; color:#bbb;">Screen space left for tall devices, for ease of one hand usage.</div>
            <button class="accordion"><h4>Semester 3</h4></button>
            <div class="panel">
              <ul>
                <li>Discrete Mathematics</li>
                <li>Data Structure And Algorithms</li>
                <li>Data Structure and Algorithms (Lab)</li>
                <li>Data Analysis and Interpretation</li>
                <li>System Software Lab</li>
                <li>Introduction of Electrical and Electronic Circuits</li>
              </ul>
            </div>

            <button class="accordion"><h4>Semester 2</h4></button>
            <div class="panel">
              <ul>
                <li>Linear Algebra</li>
                <li>Differential Equations</li>
                <li>Basics of Electircity and Magnetism</li>
                <li>Biology</li>
                <li>Chemistry Lab</li>
                <li>Engineering Graphics and Drawing</li>
                <li>Abstractions and Paradigms in Programming</li>
                <li>Absreactions and Paradigms in Programming (Lab)</li>
              </ul>
            </div>

            <button class="accordion"><h4>Semester 1</h4></button>
            <div class="panel">
              <ul>
                <li>Computer Programming and Utilization</li>
                <li>Calculus</li>
                <li>Quantum Physics and Applications</li>
                <li>Physics Lab</li>
                <li>Mechanical Workshop</li>
                <li>Organic and Inorganic Chemistry</li>
              </ul>
            </div>
            <br>
            <br>
            <h3 style="color:white;">Current Time Table</h3>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Time</th>
                  <th scope="col">Mon</th>
                  <th scope="col">Tue</th>
                  <th scope="col">Wed</th>
                  <th scope="col">Thu</th>
                  <th scope="col">Fri</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">0830</th>
                  <td rowspan="2">CS 207</td>
                  <td rowspan="2">EE 101</td>
                </tr>
                <tr>
                  <th scope="row">0900</th>
                </tr>
                <tr>
                  <th scope="row">0930</th>
                  <td></td>
                  <td rowspan="2">CS 207</td>
                  <td></td>
                  <td rowspan="2">EE 101</td>
                </tr>
                <tr>
                  <th scope="row">0930</th>
                </tr>
                <tr>
                  <th scope="row">1000</th>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td rowspan="2">CS 207</td>
                </tr>
                <tr>
                  <th scope="row">1030</th>
                </tr>
                <tr>
                  <th scope="row">1100</th>
                  <td></td>
                  <td></td>
                  <td rowspan="3">CS 215</td>
                  <td></td>
                  <td rowspan="3">CS 215</td>
                </tr>
                <tr>
                  <th scope="row">1130</th>
                  <td rowspan="2">EE 101</td>
                </tr>
                <tr>
                  <th scope="row">1200</th>
                </tr>
                <tr>
                  <th scope="row">1230</th>
                  <td colspan="5" style="background-color:#111; color:#fff;">LUNCH BREAK</td>
                </tr>
                <tr>
                  <th scope="row">1400</th>
                  <td></td>
                  <td rowspan="4">CS 251</td>
                  <td></td>
                  <td></td>
                  <td rowspan="2">CS 293</td>
                </tr>
                <tr>
                  <th scope="row">1530</th>
                  <td>CS 213</td>
                  <td></td>
                  <td>CS 213</td>
                </tr>
                <tr>
                  <th scope="row">1700</th>
                </tr>
                <tr>
                  <th scope="row">1730</th>
                  <td></td>
                  <td></td>
                  <td></td>
                  <td rowspan="3">EE 101</td>
                </tr>
                <tr>
                  <th scope="row">1800</th>
                </tr><tr>
                  <th scope="row">1830</th>
                </tr>
              </tbody>
            </table>
          </div>
      </div>
    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="js/nav.js"> </script>
    <script>
      var acc = document.getElementsByClassName("accordion");
      var i;

      for (i = 0; i < acc.length; i++) {
          acc[i].addEventListener("click", function() {
              /* Toggle between adding and removing the "active" class,
              to highlight the button that controls the panel */
              this.classList.toggle("active");

              /* Toggle between hiding and showing the active panel */
              var panel = this.nextElementSibling;
              if (panel.style.display === "block") {
                  panel.style.display = "none";
              } else {
                  panel.style.display = "block";
              }
          });
      }

      var cells = document.getElementsByTagName("td")
      for(i = 0; i < cells.length; i++){
        if (cells[i].innerHTML == "CS 207"){
          cells[i].style.backgroundColor = "#ffe6e6";
        }else if(cells[i].innerHTML == "EE 101"){
          cells[i].style.backgroundColor = "#ac7339";
          cells[i].style.color = "#fff";
        }else if(cells[i].innerHTML == "CS 251"){
          cells[i].style.backgroundColor = "#00e673";
        }else if(cells[i].innerHTML == "CS 215"){
          cells[i].style.backgroundColor = "#6600ff";
          cells[i].style.color = "#fff";
        }else if(cells[i].innerHTML == "CS 213" || cells[i].innerHTML == "CS 293"){
          cells[i].style.backgroundColor = "#cc3300";
          cells[i].style.color = "#fff";
        }
        cells[i].style.verticalAlign = "middle";
      }
    </script>
  </body>
</html>