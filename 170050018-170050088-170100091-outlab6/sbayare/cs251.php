<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="custom.css">

    <title>Code Warriors, CS 251, IITB CSE</title>
    <style type="text/css">
      .h5{
        text-align:center;
      }
    </style>
  </head>
  <body>
    <!-- The whole page - START-->
    <div class="container-fluid">
      <div class="row">

          <div class="col-md-2"></div>

         <!-- Sidebar | Navbar - Start -->
         <div id="nav-placeholder">
           <?php
            $nav_file = fopen('nav.html', 'r');
            $nav_contents = fread($nav_file, filesize('nav.html'));
            echo $nav_contents;
            fclose($nav_file);
           ?>
         </div>
         <!-- Sidebar | Navbar - End -->
         
          
         <div class="col-sm-8 col-md-6 col-xs-12" id="main" style="background-image: url('pictures/stars.jpg');">
            <h1 class="hidden-xs">Code Warriors</h1>
             <div class="col-sm-12">
             <div id="time"><p></p></div>
             <script>
             function updateTime(){
             document.getElementById("time").innerHTML = new Date();
             }

             setInterval(updateTime, 500);
             </script>
            </div>
            <div class="col-sm-12 col-md-4 col-xs-12">
              <img class="center-block img-responsive" style="height:160px;" src="pictures/sreyas.jpg">
              <h5 style="text-align:center;">Sreyas Raghavan</h5>
            </div>
            <div class="col-sm-12 col-md-4 col-xs-12">
               <img class="center-block img-responsive" style="height:160px;" src="pictures/mathews.jpg">
               <h5 style="text-align:center;">Mathews Boban</h5>
            </div>
            <div class="col-sm-12 col-md-4 col-xs-12">
              <img class="center-block img-responsive" style="height:160px;" src="pictures/sbayare.jpg">
              <h5 style="text-align:center;">Shubhamkar B. Ayare</h5>
            </div>
         
        </div>
      </div>
    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <!-- <script src="js/nav.js"> </script> -->
    <script type="text/javascript">
      function start(){
        var xs_brand = document.getElementsByClassName('navbar-brand');
        //console.log(xs_brand.length);
        xs_brand[0].innerHTML = "Code Warriors";
      }
      window.onload = start;
    </script>
  </body>
</html>