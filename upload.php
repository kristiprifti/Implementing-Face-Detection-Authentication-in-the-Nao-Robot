<!DOCTYPE html>
<html>
	<head>
		<title>Upload </title>
		<style type="text/css">
			h3{font-family:tahoma;background:#00ccdd;padding:5px 10px;color:#FFF;text-align:center;}
			table tr td label{font:14px tahoma;}
		</style>
	</head>
	<body>
    <!-- create a form interface to be read and insert data into database -->
		<form action="" method="post" enctype="multipart/form-data">
		<table cellpadding="10" align="center" rules="all" frame="box">
			<tr>
				<td colspan="2">
					<h3>
						 Upload File
					</h3>
				</td>
			</tr>
			<tr>
				<td>
					<label for="txt-file">Open File(*.txt):</label>
				</td>
				<td>
                <input type="file" name="the_file" id="fileToUpload">
                </td>
			</tr>
			<tr>
				<td colspan="2" align="right">
					<input type="submit" name="submit" value="Start Upload"><!--button to submit the form to read data from the file-->
				</td>
			</tr>
		</table>
		</form>
	</body>
</html>
 
  <?php
    $currentDirectory = getcwd();
    $uploadDirectory = "/files/";

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['txt']; // These will be the only file extensions allowed 

    $fileName = $_FILES['the_file']['name'];
    $fileSize = $_FILES['the_file']['size'];
    $fileTmpName  = $_FILES['the_file']['tmp_name'];
    $fileType = $_FILES['the_file']['type'];
    $fileExtension = strtolower(end(explode('.',$fileName)));

    $uploadPath = $currentDirectory . $uploadDirectory . basename($fileName); 

    if (isset($_POST['submit'])) {
        
    $servername = "localhost";
	$username = "id12730815_rbproject";
	$password = "myproject";
	$database = "id12730815_attendancedb";
	
	$conn =  mysqli_connect($servername, $username, $password);
	if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
	} else {
	    echo "connect sucessful";
	}
	mysqli_select_db($conn,$database);

      if (! in_array($fileExtension,$fileExtensionsAllowed)) {
        $errors[] = "This file extension is not allowed. Please upload a text file";
      }

      if ($fileSize > 4000000) {
        $errors[] = "File exceeds maximum size (4MB)";
      }

      if (empty($errors)) {
        $didUpload = move_uploaded_file($fileTmpName, $uploadPath);

        if ($didUpload) {
          echo "The file " . basename($fileName) . " has been uploaded";
        } else {
          echo "An error occurred. Please contact the administrator.";
        }
      } else {
        foreach ($errors as $error) {
          echo $error . "These are the errors" . "\n";
        }
      }

    $open = fopen( $uploadPath,'r');
    while (!feof($open)) 
    {
	$getTextLine = fgets($open);
	$explodeLine = explode(",",$getTextLine);
	
	list($courseQuery,$firstnameQuery,$lastnameQuery,$dateQuery,$att) = $explodeLine;
	
	$sql = "INSERT INTO Students(Course,  FirstName, LastName,Date, Attendance) VALUES ('" . $courseQuery . "', '" . $firstnameQuery . "', '" . $lastnameQuery . "','" . $dateQuery . "', ' $att')";

	if (mysqli_query($conn, $sql)) {
        echo "New record created successfully<br>";
    } else {
       echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
    }
 
    fclose($open);
    }
?>
