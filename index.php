<?php 
session_start(); 
include "db_conn.php";
// include "ai.php";
?>


<!DOCTYPE html>
<html>
<head>
  <title>Route Planner</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
      padding: 0;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100%;
      background-image: url('Ai.jpg');
      background-size: cover;
      background-position: center;
      
    }

    h1 {
      font-size: 60px;
     
      color: rgb(255, 154, 2);
      text-shadow: black;
    
      
    }

    form {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 450px;
      background-color: rgba(255, 255, 255, 0.8);
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      
    }

    label {
      margin-bottom: 10px;
      font-weight: bold;
    }

    select,
    input[type="date"],
    input[type="time"] {
      width: 100%;
      padding: 10px;
      margin-bottom: 20px;
      border: 1px solid #ddd;
      border-radius: 4px;
      outline: none;
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
    .content {
      background-color: rgba(255, 255, 255, 0.9);
      padding: 40px;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }


  
  </style>

  <script type="text/javascript">
      document.getElementById("myButton").onclick = function () {
          location.href = "page_2.php";
      };
  </script>
  
</head>
<body>
  

  <div class='content'>
  <h1>ROUTE PLANNER</h1>
  <form action="ai.php" method="POST">
  

    <label for="start">Start Location:</label>
      <select id="start" name="start">
        <option value="ECB">ECB</option>
      
      </select>

   
    <label for="end">End Location:</label>
      <select id="end" name="end">
        <option value="AGAEGOAN">AGAEGOAN</option>
      </select>

    <img src="map.jpeg" alt="Map" style="max-width: 100%; margin-top: 10px; border-radius: 8px;">

    <!-- Date -->
    <label for="date">Date:</label>
    <input type="date" id="c_date" name="c_date">

    <!-- Time -->
    <label for="time">Time:</label>
    <input type="time" id="c_time" name="c_time">

    <!-- Submit Button -->
    <button id='myButton' type="submit" value="Execute" name="send" onclick="location.href = 'page_2.php';">Submit</button>
  </form>
  </div>

  
</body>
</html>
