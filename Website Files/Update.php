<?php

$servername = "localhost";
$username = "id12730815_rbproject";
$password = "myproject";
$database = "id12730815_attendancedb";


// Create connection
$conn = mysqli_connect($servername, $username, $password,$database);

//Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully<br>"; 

mysqli_select_db($conn,$database);

// This is important to prevent injection attacks
$courseQuery = $_POST['Course'];
$firstnameQuery = $_POST['FirstName'];
$lastnameQuery = $_POST['LastName'];
$dateQuery = $_POST['Date'];
$attendanceQuery = $_POST['Attendance'];
$lateQuery = $_POST['Late'];

//set attendance value default is 0, if it's on, it's 1
$att = 0;
if($attendanceQuery == 'on'):
    $att = 1;
endif;
echo $att . "Attendance <br>";
//set late value default is 0, if it's on, it's 1
$late = 0;
if($lateQuery == 'on'):
    $late = 1;
endif;
echo $late . "Late <br>";

//Insert data to database table with on duplicate ket update statement to avoid duplicate value
    $sql = "INSERT INTO Students(Course,  FirstName, LastName,Date, Attendance, Late) VALUES ('" . $courseQuery . "', '" . $firstnameQuery . "', '" . $lastnameQuery . "','" . $dateQuery . "',  '" . $att . "', '" . $late . "')
      ON DUPLICATE KEY UPDATE  Attendance='" . $att . "', Late ='" . $late . "'" ;

if (mysqli_query($conn, $sql)) {
echo "New record created successfully<br>";
} else {
echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

// Close the connection to the database server
mysqli_close($conn);
?>
