<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <link rel="stylesheet" href="custom.css">
    <link rel="shortcut icon" href="pictures/logo.ico" />
    <link rel="shortcut icon" href="pictures/logo.png" type="image/png">


    <title>Shubhamkar B. Ayare, IITB CSE</title>

      <style>
      html {
          position: relative;
          min-height: 100%;
      }
      .carousel-fade .carousel-inner .item {
          opacity: 0;
          transition-property: opacity;
      }
      .carousel-fade .carousel-inner .active {
          opacity: 1;
      }
      .carousel-fade .carousel-inner .active.left,
      .carousel-fade .carousel-inner .active.right {
          left: 0;
          opacity: 0;
          z-index: 1;
      }
      .carousel-fade .carousel-inner .next.left,
      .carousel-fade .carousel-inner .prev.right {
          opacity: 1;
      }
      .carousel-fade .carousel-control {
          z-index: 2;
      }
      @media all and (transform-3d),
      (-webkit-transform-3d) {
          .carousel-fade .carousel-inner > .item.next,
          .carousel-fade .carousel-inner > .item.active.right {
              opacity: 0;
              -webkit-transform: translate3d(0, 0, 0);
              transform: translate3d(0, 0, 0);
          }
          .carousel-fade .carousel-inner > .item.prev,
          .carousel-fade .carousel-inner > .item.active.left {
              opacity: 0;
              -webkit-transform: translate3d(0, 0, 0);
              transform: translate3d(0, 0, 0);
          }
          .carousel-fade .carousel-inner > .item.next.left,
          .carousel-fade .carousel-inner > .item.prev.right,
          .carousel-fade .carousel-inner > .item.active {
              opacity: 1;
              -webkit-transform: translate3d(0, 0, 0);
              transform: translate3d(0, 0, 0);
          }
      }
      .item:nth-child(1) {
          background-image:url('pictures/creeper.jpg'); no-repeat center center fixed;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
      }
      .item:nth-child(2) {
          background-image:url('pictures/lego.jpg'); no-repeat center center fixed;
          -webkit-background-size: cover;
          -moz-background-size: cover;
          -o-background-size: cover;
          background-size: cover;
      }
      .carousel {
          z-index: -99;
      }
      @media(min-width:992px){
        .carousel .item {
          position: fixed;
          margin-left:33%;
          width:50%;
          height:100%;
        }
      }
      @media(max-width:991px){
        .carousel .item{
          position:fixed;
          margin-left:0;
          height:100%;
          width:100%;
        }
      }
      .title {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        text-shadow: 2px 2px #000;
        color: #FFF;
      }
    </style>
    
  </head>
  <body>
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
            <!-- Inspired by https://codepen.io/transportedman/pen/NPWRGq -->

            <div class="carousel slide carousel-fade" data-ride="carousel">

                <!-- Wrapper for slides -->
                <div class="carousel-inner" role="listbox">
                    <div class="item active"></div>
                    <div class="item"></div>
                </div>
            </div>
            <h1 class="hidden-xs inverted">Shubhamkar B. Ayare</h1>

            <div class="tall-pg">
              <div class="visible-xs" style="text-align:center; color:#bbb;">Screen space left for tall devices, for ease of one hand usage.</div>

              <div data-toggle="modal" data-target="#biography" id="oneliner">
              Failing to be a robot.<br>
              (PS: Robots can be highly productive.)
              </div>
              
              <div class="modal" tabindex="-1" role="dialog" aria-labelledby="biography" id="biography">
                <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title">See right to close the window if you did not expect this to open. Bad design?</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                    <div class="modal-body">
                      <p>Hi!</p>
                      <p>I am currently a Sophie in 2nd year at IITB (CSE). Feel free to take a look around, or leave a <a href="comment.html">public message</a>. I wish to be able to connect myself to the internet some day. It's a vast place. I hope you explore it frequently.</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="inverted" id="counter">
                 This page has been viewed 
                 <span id="counter-number"><?php
                   $cnt_file = fopen("config.txt", "r");
                   $cnt = fread($cnt_file, filesize("config.txt"));
                   $cnt = $cnt + 1;
                   echo $cnt;
                   fclose($cnt_file);
                   $cnt_file = fopen("config.txt", "w");
                   fwrite($cnt_file, $cnt);
                   fclose($cnt_file);

                 ?></span>
                 times.
              </div> 
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