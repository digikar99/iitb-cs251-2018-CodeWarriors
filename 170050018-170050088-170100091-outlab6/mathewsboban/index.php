<!DOCTYPE html>
<html lang="en">
  <head>
  <link rel="icon" href="M.jpeg">
  <title>Mathews Boban, IITB CSE</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
#hits {
  width: 300px;
  border: solid red 2px;
}
.carousel-inner img {
  margin: auto;
}

  </style>
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



  <h1 style="text-align:left">Welcome</h1>
  <a type="button" data-toggle="modal" data-target="#myModal" style="font-size:30px">Hey there, i am Mathews Boban, Master of the Mystic Arts ;)</a>

  
  <!-- Modal -->
  <div id="myModal" class="modal fade" role="dialog">
    <div class="modal-dialog">

      <!-- Modal content-->
      <div class="modal-content">
	<div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">Short Bio</h4>
	</div>
	<div class="modal-body">
          <p>I am Mathews Boban. I hail from Kerala. I am currently doing second year B.Tech at CSE, IIT Bombay.</p>
	</div>
	<div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
	</div>
      </div>
      
    </div>
  </div>

  <div class="container">
  <div id="myCarousel" class="carousel slide" style="width:400px; text-align:center" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <!-- <li data-target="#myCarousel" data-slide-to="2"></li> -->
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="1.jpg" alt="Image 1" style="width:240px;height:300px" >
	<!-- <img src="1.jpg" alt="Image 1" style="height:100%" > -->
      </div>

      <div class="item">
        <img src="3.jpg" alt="Image 2" style="width:400px;height:300px">
      </div>
    

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
    </div>
  </div>
 
 <!-- <div class="w3-bar w3-black"> -->
 <!--   <a href="academics.html" class="button">Academics</a> -->
 <!--   <p>  </p> -->
 <!--  <a href="misc.html" class="button">Interests</a> -->
 <!--  <a href="misc.html" class="button">Interests</a> -->
 <!-- </div> -->


<?php
$myfile = fopen("count.txt", "r") or die("Unable to open file!");
   $a = fread($myfile,filesize("count.txt"));
  fclose($myfile);
  echo "<h3> Hit Counter:" . $a ."</h3>"; 
$myfile = fopen("count.txt", "w") or die("Unable to open file!");   
   $b = $a + 1;
fwrite($myfile, $b);
fclose($myfile);
   ?>

 
</body>
</html>
