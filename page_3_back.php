<?php
session_start();
$connection = mysqli_connect('localhost', 'root', '', 'cse_404');

if (isset($_POST['send'])) {
    $route = $_POST['route'];
    $cost = $_POST['cost'];

    if (empty($route) || empty($cost)) {
        $_SESSION['notification'] = "Please fill in all the fields.";
    } else {
        $query = "INSERT INTO planned_route (route, cost) VALUES ('$route', '$cost')";
        mysqli_query($connection, $query);
        $_SESSION['notification'] = "Button executed successfully.";
    }

    header('location: notification.php');
    exit();
}
?>
