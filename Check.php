<?php
$servername = "localhost";
$username = "<username>";
$password = "<password>";
$conn  = new mysqli($servername, $username, $password, "<database>");
	        session_start();


?>

<html>
<body>
	<?php

            $sql = 'select * from Machines;';
			$result = mysqli_query($conn, $sql);
			$resultCheck = mysqli_num_rows($result);
			
			while($row=mysqli_fetch_assoc($result)){
			if($_POST['uname']==$row['Machine_ID']&& password_verify($_POST['pwd'],$row['Password'] ))
			{
			$_SESSION['uname'] = $_POST['uname'];
			$sql = "select * from Machines where Machine_ID='".$_POST['uname']."';";
			$result = mysqli_query($conn, $sql);
			$resultCheck = mysqli_num_rows($result);

			if($resultCheck>0)
				while($row = mysqli_fetch_assoc($result))
					echo "<p>".$row['Update_req']."</p>";
			}

		}


	?>

