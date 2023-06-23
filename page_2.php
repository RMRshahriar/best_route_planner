<?php 
session_start(); 
include "db_conn.php";
    

?>



<!DOCTYPE html>
<html>
<head>
  <title>Route Planner</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-image: url('Ai.jpg');
      background-size: cover;
      background-position: center;
    }

    h1 {
      font-size: 60px;
      color: rgb(255, 154, 2);
      text-shadow: black;
    }

    button[type="submit"] {
      width: 100%;
      padding: 10px;
      background-color: #4caf50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button[type="submit"]:hover {
      background-color: #45a049;
    }

    .content h1 {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 50px;
      padding-left: 20px;
      letter-spacing: 2px;
      text-align: center;
      color: #fff;
    }
    
    .par {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 25px;
      padding-bottom: 25px;
      letter-spacing: 1.2px;
      line-height: 30px;
      text-align: center;
      color: #fff;
    }

    .execute-button {
      margin-top: 20px;
      text-align: center;
    }
  </style>
</head>

<body>
  <div class="content">
    <h1>SUCCESSFUL!</h1>
    <p class="par">Now find your best route</p>
    <br>
    <div class="view-button">
        <button onclick="location.href = 'page_3.php';" type="submit">MAP VIEW</button>
      </div>
  </div>
</body>
</html>
