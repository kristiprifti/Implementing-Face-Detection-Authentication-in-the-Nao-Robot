<?php
/* Search value in all columns of table to present what we are looking for
   when a button named search is hit, we get the value from text box valueToSearch
   $query will get all data from database table if the value are searched doesn't match anything in the table;
   otherwise, $query only get data that matched*/
    if(isset($_POST['search']))
{
    $valueToSearch = $_POST['valueToSearch'];
    // using concat mysql function
    $query = "SELECT * FROM `Students` WHERE CONCAT(`Course`, `FirstName`, `LastName`, `Date`, `Attendance`) 
    LIKE '%".$valueToSearch."%'";
    $search_result = filterTable($query);
    
}
 else {
    $query = "SELECT * FROM `Students`";
    $search_result = filterTable($query);
}



// function to connect and execute the query return 
function filterTable($query)
{
 $servername = "localhost";
$username = "id12730815_rbproject";
$password = "myproject";
$database = "id12730815_attendancedb";


// Create connection to database
    $connect =  mysqli_connect($servername, $username, $password, $database);
    $filter_Result = mysqli_query($connect, $query);
    return $filter_Result;
}


?>
<!DOCTYPE html>
<html>
<head></head>
<style>
body{
  background-color: #FFfACD;
}
table {
border-collapse: collapse;
width: 100%;
color: #FF7F50;
font-size: 25px;
text-align: left;
}
th {
background-color: #FF7F50;
color: white;
}
tr:nth-child(even) {background-color: #FFFAFA}
form {
    position: relative; 
    z-index: 1; 
    background: #FFFAF0; 
    max-width: 250px;
    margin: 0 auto 20px; 
    padding: 20px; 
    text-align: center;
}
h2{
    font-size: 50px;
   text-align:center; padding: 10px; 
   color: #FF4500;
}
</style>
<h2>Attendence Report</h2>
	
<body>
<!--Create a filter form to search value that we want to see in the table-->
  <form action="" method="post"> 
            <input type="text" name="valueToSearch" placeholder="Value To Search"><br><br>
            <input type="submit" name="search" value="Filter"><br>
  </form>

<!--Create a table in the webpage with 6 columns-->	
<table>
<tr>
    <th>Course</th>
	<th>First Name</th>
	<th>Last Name</th>
	<th>Date</th>
	<th>Attendance</th>
	<th>Late</th>
</tr>

    <?php while($row = mysqli_fetch_array($search_result)) {
	/* Output data stored and display in the table with mysqli_fetch_array() funtion, we take each row of the result and print the data stored*/
        $courseQuery = $row['Course'];
        $firstnameQuery =$row['FirstName'];
        $lastnameQuery = $row['LastName'];
        $dateQuery = $row['Date'];
        $att = $row['Attendance'];
        $late = $row['Late'];
          echo
            "<tr>
              <td>{$courseQuery}</td>
              <td>{$firstnameQuery}</td>
              <td>{$lastnameQuery}</td>
              <td>{$dateQuery}</td>
              <td>{$att}</td>
              <td>{$late}</td>
            </tr>";
                } ?>
   
</table>


</body>

</html>
