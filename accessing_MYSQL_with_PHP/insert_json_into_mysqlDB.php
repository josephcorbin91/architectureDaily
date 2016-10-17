<?php
    // open mysql connection
    $host = "localhost";
    $username = "root";
    $password = "";
    $dbname = "architecturedaily";
    $con = mysqli_connect($host, $username, $password, $dbname) or die('Error in Connecting: ' . mysqli_error($con));

    // use prepare statement for insert query
    #$st = mysqli_prepare($con, 'INSERT INTO skyscrapercity_posts(id, title, city, description, video, image, link, date, likes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)') or die(mysqli_error($con));
	$st = mysqli_prepare($con, 'INSERT INTO skyscrapercity_posts(id,title,image,likes) VALUES (?, ?, ?, ?)') or die(mysqli_error($con));

    // bind variables to insert query params
   # mysqli_stmt_bind_param($st, 'sssssssss', $id, $title, $city, $description, $video, $image, $link, $date, $likes);
	mysqli_stmt_bind_param($st, 'ssss', $id, $title, $image, $likes);

    // read json file
    $filename ='http://localhost/skyscrapercity_posts/posts.json';
    $json = file_get_contents($filename);   

    //convert json object to php associative array
    $data = json_decode($json, true);

    // loop through the array
    foreach ($data as $row) {
     	
        $id = $row['id'];		
		$title = $row['title'];	
		$image = $row['image'];	
		$likes = $row['like'];	
        
      
        // execute insert query
        mysqli_stmt_execute($st);
    }
    
    //close connection
    mysqli_close($con);
	
	#Command to run
	#http://localhost/skyscrapercity_posts/insert_into.php
?>
