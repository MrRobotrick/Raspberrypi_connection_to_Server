<?php
echo "Executing: insert.php";
$con= mysqli_connect('hostname', 'database_name', 'your_username', 'your_password');
$x = $_GET["x"];
echo "<br>x = " .$x. "";
$sql ="INSERT INTO ultraValue (ultvalue) VALUES ('$x')";
mysqli_query($con, $sql); 
mysqli_close($con);
echo "<br>done";
?>