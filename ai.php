<?php

header('Location: page_2.php');

?>

<?php
session_start();
include "db_conn.php";
error_reporting(E_ALL);
ini_set('',1);

$connection = mysqli_connect('localhost','root','','cse_404');

$command = escapeshellcmd('/home/rafi/Desktop/htdocs/test.py');
$output = shell_exec($command);
echo $output;
echo 'Alhamdulillah';


if(isset($_POST['send'])){
    $c_date = $_POST['c_date'];
    $c_time = $_POST['c_time'];
    
    if(empty($c_date) || empty($c_time)){
        $_SESSION['notification'] = "Please fill in all the fields.";
        
    } else {
        $request = "INSERT INTO i_values(c_date,c_time) VALUES ('$c_date', '$c_time')";
        $x = mysqli_query($connection,$request);
        // if ($x){
        //     $_SESSION['notification'] = "btn success";    
        // } else {
        //     $_SESSION['notification'] = "btn fail:" . mysqli_error($connection);  
        // }
        // // echo 'Done' ;
        // $_SESSION['notification'] = "Button executed successfully.";
        
    }

    // header('location:notification.php');
    // echo 'Done' ;
    exit();
} else {
    echo 'Something went wrong.';
}

?>


