<!doctype html>
<html lang="en">
<head>
  <link rel="icon" href="webicon.jpeg">
  <title>Sreyas Raghavan</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  body
  {
    font-family: Arial;
    background-color: black
  }
  .container button
  {
    color:white;
  }
   .container h3
  {
    color:white;
  } 
  .modal-body
  {
    color:black;
  }
  .modal-body
  {
    color:black;
  }
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
.main-nav li a:hover
{
    border: 1px solid white;
}
.main-nav li.active a
{
    border: 1px solid white;
    background-color: darkorange;
    
}
.main-nav li a
{
    color: white;
    text-decoration: none;
    padding: 5px 20px;
    font-family: "Roboto", sans-serif;
    font-size: 15px;
}
  p
  {
  	color:white;
  	text-align:right;
  	font-size:23px;
  }
</style>
</head>
<body>

	 <ul class="main-nav">
	<li class="active"><a href="index.php"> HOME </a></li>	
    <li><a href="interests.html"> INTERESTS </a></li>
    <li><a href="project.html"> PROJECTS </a></li>
    <li><a href="https://www.cse.iitb.ac.in/~sbayare/cs251.php"> TEAM </a></li>
    <li><a href="contact.html"> CONTACTS </a></li>
    <li><a href="academics.php"> ACADEMICS </a></li>
    <li><a href="comment.html"> COMMENT </a></li>
    <li><a href="view_comments.php"> COLLECTION </a></li>
  </ul> 

<div class="container">
  <h3 align="center">Hi , I am Sreyas</h3>
  <!-- Trigger the modal with a button -->
  <div align="center">
<button type="button" style="background-color:inherit;font-family:verdana;border:none;" data-toggle="modal" data-target="#myModal">Still Looking For That One Sentence To define Me</button></div>

  <!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">
    
      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <b style="margin-left: 250px">About Me</b>
          <button type="button" class="close" data-dismiss="modal" font-size:15px>close</button>
        </div>
        <div class="modal-body" align="center">
          <p1>I am a CSE sophomore at IITB . I was born on june 24th and i am from Kerala <br>Have a nice day </p1>
        </div>
      </div>
      
    </div>
  </div>

  <p1><br><p1>


    <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="image_1.jpg" alt="Los Angeles" style="width:100%;">
      </div>

      <div class="item">
        <img src="image_2.jpg" alt="Chicago" style="width:100%;">
      </div>
    
      <div class="item">
        <img src="image_3.jpg" alt="New york" style="width:100%;">
      </div>
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
  <p><br></p>
	<?php
	$handle=fopen("counter_file.txt",'r+') or die ("cannot open the file");
	$count_value=fread($handle,filesize("counter_file.txt"));
	echo "<p>Hit Counter : $count_value<p>";
	 $count_value=$count_value+1;
	fseek($handle,0);
	fwrite($handle,$count_value);
	fclose($handle);
	?>


</body>
</html>


