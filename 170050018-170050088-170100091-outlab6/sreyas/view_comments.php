<!doctype html>
<html lang="en">
  <head>
    <link rel="icon" href="webicon.jpeg">
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="custom.css">
    <title>Collection</title>
    
  </head>
  <body>


         <ul class="main-nav">
    <li><a href="index.php"> HOME </a></li> 
    <li><a href="interests.html"> INTERESTS </a></li>
    <li><a href="project.html"> PROJECTS </a></li>
    <li><a href="https://www.cse.iitb.ac.in/~sbayare/cs251.php"> TEAM </a></li>
    <li><a href="contact.html"> CONTACTS </a></li>
    <li><a href="academics.php"> ACADEMICS </a></li>
    <li><a href="comment.html"> COMMENT </a></li>
    <li class="active" ><a href="view_comments.php"> COLLECTION </a></li>
  </ul>


    <!-- The whole page - START-->
    <div class="container-fluid">
      <div class="row">

          <div class="col-md-2"></div>

          <!-- Sidebar | Navbar - Start -->
          <div id="nav-placeholder"></div>
          <!-- Reference: https://stackoverflow.com/questions/31954089/html-css-navigation-bar-on-multiple-pages -->
          <!-- Sidebar | Navbar - End -->

          <!-- HOME PAGE -->
          <div class="col-sm-8 col-md-6 col-xs-12" id="main">

            <?php
              $cmt_file = fopen('responses.txt', 'r');
              echo fread($cmt_file, filesize("responses.txt"));
              fclose($cmt_file);
            ?>

            </div>
          </div>
      </div>
    </div>


    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
    <script src="js/nav.js"> </script>
  </body>
</html>