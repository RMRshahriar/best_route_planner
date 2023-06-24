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
      height: 200vh;
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
    input[type="month"],
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



  
  </style>
  
</head>
<body>
  <h1>ROUTE PLANNER</h1>

  <form id="routeForm">
  

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
    <input type="date" id="date" name="date">

    <!-- Time -->
    <label for="time">Time:</label>
    <input type="time" id="time" name="time">

    <!-- Submit Button -->
    <button type="submit" value="Execute" name="send"><a href="page_2.php">Submit</a></button>
  </form>

  <!-- Map container -->
 <div id="map" style="text-align: center;">
  <h2 style="font-size: 50px; color: rgb(255, 154, 2);">PLANNED ROUTE</h2>
  <img src="map.jpeg" alt="Map" style="max-width: 70%; margin: 10px auto; display: block; border-radius: 8px;">
</div>


  
</body>
</html>
