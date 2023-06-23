






<!DOCTYPE html>
<html>
<head>
  <title>Route Details</title>
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
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      margin-bottom: 30px;
    }

    .content {
      background-color: rgba(255, 255, 255, 0.9);
      padding: 40px;
      border-radius: 10px;
      text-align: center;
      box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    }

    .box {
      margin-bottom: 20px;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
      background-color: #f5f5f5;
      text-align: left;
      box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    }

    h3 {
      font-size: 24px;
      color: #333;
      margin-top: 0;
      margin-bottom: 20px;
      text-transform: uppercase;
    }

    p {
      margin: 0;
      color: #666;
      line-height: 1.4;
    }

    .footer {
      margin-top: 30px;
      font-size: 14px;
      color: #999;
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
<?php
$connection = mysqli_connect('localhost', 'root', '', 'cse_404');

$query = "SELECT * FROM best_route ORDER BY id_r DESC LIMIT 1";
$result = mysqli_query($connection, $query);
if ($result && mysqli_num_rows($result) > 0) {
  $row = mysqli_fetch_assoc($result);
  $route = $row['route'];
  $cost = $row['cost'];
  $dir = $row['dir'];
  // Display the latest value on the front page
} else {
  echo "No records found.";
}
?>
  <div class="content">
    <h1>PLANNED ROUTE</h1>
    <div class="box">
      <h3>Route</h3>
      <input type="route" id="route" name="route" size='100' value="<?= $dir; ?>">
     
    </div>

    <div class="box">
      <h3>Cost</h3>
      <input type="cost" id="cost" name="cost" value="<?= $cost; ?>">
   
    </div>


   <div>
   <img src="<?= $route; ?>.png" alt="Best Route Map" width="800" height="400">
   </div>
   <p>&nbsp;</p>
   <div class="view-button">
   <button onclick="location.href = 'index.php';" type="submit">Back To Home</button>
   </div>

    <div class="footer">
      <p>&copy; AI LAB 404 </p>
    </div>
  </div>
</body>
</html>
