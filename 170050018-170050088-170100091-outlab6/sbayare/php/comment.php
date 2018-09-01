<?php
	
	
	$nm = $_POST['name'];
	$cmt = $_POST['comment'];
	date_default_timezone_set("Asia/Calcutta");
	$tm = date('Y/m/d h:i:s');
	$timestamp = "<div class=\"timestamp\">$tm</div>";
	$name = "<div class=\"comment-name\">Name: $nm</div>";
	$comment = "<div class=\"comment-comment\">Comment: $cmt</div>";
	$to_write = "<div class=\"comment\">\n$name\n$comment\n$timestamp\n</div>\n\n";	
	$res_file = fopen('responses.html', 'r');
	$existing_contents = fread($res_file, filesize('responses.html'));
	fclose($res_file);
	$res_file = fopen('responses.html' , 'w');

	fwrite($res_file, $to_write);
	fwrite($res_file, $existing_contents);
	fclose($res_file);
	echo "Your comment has been posted. Redirecting to the comments page.";
	header("Location: ../view_comments.php"); /* 		Redirect browser */
	exit();
?> 
