<?php
include 'test.php';
?>
<html>
<body>

<?php
$myfile = fopen("answer.txt", "r") or die("Unable to open file!");
?><center><h3 style="color:#FC0"><?php echo fread($myfile,filesize("answer.txt"));
fclose($myfile);
?></h3></center>

</body>
</html>