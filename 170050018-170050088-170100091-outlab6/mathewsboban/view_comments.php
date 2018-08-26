<!doctype html>
<html lang="en">
  <head>
    <link rel="icon" href="M.jpeg">
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="custom.css">

    <title>Previous Comments</title>
    
  </head>
  <body>
 <nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <a class="navbar-brand" href="#">Welcome Aboard</a>
    </div>
    <ul class="nav navbar-nav">
      <li class="active"><a href="index.php">Home</a></li>
      <li><a href="academics.html">Academics</a></li>
      <li><a href="misc.html">Interests</a></li>
      <li><a href="projects.html">Projects</a></li>
      <li><a href="https://www.cse.iitb.ac.in/~sbayare/cs251.php">CS 251</a></li>
      <li><a href="contact.html">Contact</a></li>
      <li><a href="comment.html">Comments</a></li>
      <li><a href="view_comments.php">Previous Comments</a></li>
    </ul>
  </div>
</nav>



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
            <h1 class="hidden-xs">Previous Comments</h1>
            
            <?php
              $cmt_file = fopen('php/responses.html', 'r');
              echo fread($cmt_file, filesize("php/responses.html"));
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
