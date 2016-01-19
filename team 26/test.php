<?php
error_reporting(0);
//include the S3 class              
if (!class_exists('S3'))require_once('S3.php');
 
//AWS access info
if (!defined('awsAccessKey')) define('awsAccessKey', 'AKIAJVEJ2WV7WQH2I3XQ');
if (!defined('awsSecretKey')) define('awsSecretKey', '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');
 
//instantiate the class
$s3 = new S3(awsAccessKey, awsSecretKey);
 
//we'll continue our script from here in step 4!
?>

<html>
<head>
<script type="text/javascript">
    fun()
	{
		window.location.href = "test1.php";
	}
</script>
</head>

    <body bgcolor="#900">
	<div style="background-color:#FC0">
	<center>
	<h1 style="color:#900"> Spam Ham Filtering</h1>
	</center>
	</div>
	<div>
	<center>
	<img src="img/profile1.png" alt="" id="usclogo" width="150" height="150">
	</center>
	</div>
	<div>
	<br>
	<center>
        <form name="form" method="post">

			<textarea name="text_box" id="text_box" rows="20" cols="100">
			<?php if(isset($_POST['text_box'])) { 
			$value=$_POST['text_box'];
         echo $value; }?>
			</textarea>
			<br>
            <input type="submit" id="submit" value="submit" />
			<button type="button" onclick="window.location.href='test1.php'">Show Spam/Ham</button> 
			</center>
			
	
        </form>
	</div>
    </body>
</html>
<?php
    if(isset($_POST['text_box'])) { //only do file operations when appropriate
        $a = $_POST['text_box'];
        $myFile = "input.txt";
        $fh = fopen($myFile, 'w') or die("can't open file");
        fwrite($fh, $a);
        fclose($fh);
    }

//check whether a form was submitted


//create a new bucket
//$s3->putBucket("jurgens-nettuts-tutorial", S3::ACL_PUBLIC_READ);
 
//move the file
if ($s3->putObjectFile($myFile, "ishanisheth", $myFile, S3::ACL_PUBLIC_READ)) {
    //echo "We successfully uploaded your file.";
}else{
    //echo "Something went wrong while uploading your file... sorry.";
}


 
?>