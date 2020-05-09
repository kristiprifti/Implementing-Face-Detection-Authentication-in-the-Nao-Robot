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
    $currentDirectory = getcwd(); // get current directoty
    $uploadDirectory = "/files/"; // specifies the directory where the file is going to be placed

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['txt']; //  only text file is allowed 

    $fileName = $_FILES['the_file']['name'];
    $fileSize = $_FILES['the_file']['size'];
    $fileTmpName  = $_FILES['the_file']['tmp_name'];
    $fileType = $_FILES['the_file']['type'];
    $fileExtension = strtolower(end(explode('.',$fileName)));

    $uploadPath = $currentDirectory . $uploadDirectory . basename($fileName);  // specifies the path of the file to be uploaded
    // Check if we click on submit button
    if (isset($_POST['submit'])) {
        // Connect to database table
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
       // Check if selected file type is match 
      if (!in_array($fileExtension,$fileExtensionsAllowed)) {
        $errors[] = "This file extension is not allowed. Please upload a text file";
      }
      // Check file size
      if ($fileSize > 4000000) {
        $errors[] = "File exceeds maximum size (4MB)";
      }
       //Check if $error is set to 0 
      if (empty($errors)) {
        $didUpload = move_uploaded_file($fileTmpName, $uploadPath);
        // Check if file already exists
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
    // open the file to be read
    $open = fopen( $uploadPath,'r');
/* The feof() function checks if the "end-of-file" (EOF) has been reached 
   If the end of file has not been reached, using he fgetc() function is used to read a text line from a file.
   with explode()- Split a string by a string, we split string by comma */
    while (!feof($open)) 
    {
	$getTextLine = fgets($open);
	$explodeLine = explode(",",$getTextLine);
	
	list($courseQuery,$firstnameQuery,$lastnameQuery,$dateQuery,$att) = $explodeLine;
	
	$sql = "INSERT INTO Students(Course,  FirstName, LastName,Date, Attendance) 
	VALUES ('" . $courseQuery . "', '" . $firstnameQuery . "', '" . $lastnameQuery . "','" . $dateQuery . "', ' $att')";

	if (mysqli_query($conn, $sql)) {
        echo "New record created successfully<br>";
    } else {
       echo "Error: " . $sql . "<br>" . mysqli_error($conn);
    }
    }
    
    fclose($open); // close the file after we finish reading
	    
    }
?>
