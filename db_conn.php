<?php
session_start(); 
$sname= "localhost";
$unmae= "root";
$password = "";

$db_name = "cse_404";

$conn = mysqli_connect($sname, $unmae, $password, $db_name);

if (!$conn) {
	// echo "Connection failed!";
}
else
{
	// echo "Successful";
}

?>