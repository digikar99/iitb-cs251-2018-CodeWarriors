<?php
	$cnt_file = fopen("config.txt", "r");
	echo fread($cnt_file, filesize("config.txt"));
	fclose($cnt_file);

?>
