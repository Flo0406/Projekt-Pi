
<!doctype html>
<html>


<?php
//Set the status variable to empty
$Status1 = "";
$Status2 = "";
$Status3 = "";
$Status4 = "";
// check for camera 1 if any button is pressed
if (isset($_POST['camera1'])) { // take picture with camera
    shell_exec("/usr/bin/python3 /home/pi/webserver/take_picture.py");
} elseif (isset($_POST['seconds1'])) { // dropdown menu

    $time1 = $_POST['seconds1']; // get value from dropdown menu

    if (isset($_POST['video1'])) { // take video , duration == value form dropdown menu
        shell_exec("/usr/bin/python3 /home/pi/webserver/getVideo.py $time1");
        $Status1 = "Camera 1: Video start with $time1 seconds"; //Setting the message to user video has been made
    }
}

// check for camera 2 if any button is pressed

if (isset($_POST['camera2'])) { // take picture with camera
    shell_exec("/usr/bin/python3 /home/pi/webserver/take_picture.py");
} elseif (isset($_POST['seconds2'])) {  // dropdown menu

    $time2 = $_POST['seconds2']; // get value from dropdown menu

    if (isset($_POST['video2'])) { // take video , duration == value form dropdown menu
        shell_exec("/usr/bin/python3 /home/pi/webserver/getVideo.py $time2");
        $Status2 = "Camera 2: Video start with $time2 seconds"; //Setting the message to user video has been made
    }
}

//  check for camera 3 if any button is pressed

if (isset($_POST['camera3'])) { // take picture with camera
    shell_exec("/usr/bin/python3 /home/pi/webserver/take_picture.py");
} elseif (isset($_POST['seconds3'])) {  // dropdown menu

    $time3 = $_POST['seconds3']; // get value from dropdown menu

    if (isset($_POST['video3'])) { // take video , duration == value form dropdown menu
        shell_exec("/usr/bin/python3 /home/pi/webserver/getVideo.py $time3");
        $Status3 = "Camera 3: Video start with $time3 seconds"; //Setting the message to user video has been made
    }
}

// check for camera 4 if any button is pressed

if (isset($_POST['camera4'])) { // take picture with camera
    shell_exec("/usr/bin/python3 /home/pi/webserver/take_picture.py");
} elseif (isset($_POST['seconds4'])) {  // dropdown menu

    $time4 = $_POST['seconds4']; // get value from dropdown menu

    if (isset($_POST['video4'])) { // take video , duration == value form dropdown menu
        shell_exec("/usr/bin/python3 /home/pi/webserver/getVideo.py $time4");
        $Status4 = "Camera 4: Video start with $time4 seconds"; //Setting the message to user video has been made
    }
}

// refresh temperature and humidity values

if (isset($_POST['Data_new'])) {
    shell_exec("/usr/bin/python3 /home/pi/webserver/temp_webserver.py");
}

// get inital form text document
$temp = file("/home/pi/webserver/Measure/Temp_webserver.txt");
$humidity = file("/home/pi/webserver/Measure/Humidity_webserver.txt");

// initial values temperature camera1 == [0] ...
$temp1 = $temp[0];
$temp2 = $temp[1];
$temp3 = $temp[2];
$temp4 = $temp[3];
// initial values humidity camera1 == [0]...
$humidity1 = $humidity[0];
$humidity2 = $humidity[1];
$humidity3 = $humidity[2];
$humidity4 = $humidity[3];
?>


</ / Head Settings>

<head>
    <link rel="stylesheet" href="stylesheet.css">
    <!-- seperate stylecheet for website-->
    <meta http-equiv="refresh" content="5">
    <!-- relaod intervall-->
</head>


<body>
    <h2> Camera Surveillance </h2>  <!--Create heading-->
    <main>
        <div class="container">
            <!-- Class for the first camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam1-->
                <div class="image">
                    <figcaption> <b> Camera 1 </b> </figcaption>
                    <img src="CAM1.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
                <form action="pic.php" method="post">
                    <div class="buttons">
                        <div class="take picture">
                            <button name="camera1">Take Picture </button> <!-- Create the button to take a photo -->
                            <button name="video1"> Start Video </button>  <!-- Create button to start a video -->
                            <select size="1" name="seconds1">    <!-- Dropdown-menu to set the time of the video  -->
                                <option value="5">5s</option>
                                <option value="10">10s</option>
                                <option value="15">15s</option>
                                <option value="20">20s</option>
                            </select>
                        </div>
                    </div>
                    <!-- Tell the user a video has been started -->
                    <div class="Status">
                    <p><?php echo $Status1; ?></p>
                    </div>
            </div>

            <!-- Class for the second Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam2-->
                <div class="image">
                    <figcaption> <b> Camera 2 </b> </figcaption>
                    <img src="CAM1.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
                <div class="buttons">
                    <div class="take picture">
                        <button name="camera2">Take Picture </button><!-- Create the button to take a photo -->
                        <button name="video2"> Start Video </button> <!-- Create button to start a video -->
                        <select size="1" name="seconds2"> <!-- Dropdown-menu to set the time of the video  -->
                            <option value="5">5s</option>
                            <option value="10">10s</option>
                            <option value="15">15s</option>
                            <option value="20">20s</option>
                        </select>
                    </div>
                </div>
                <!-- Tell the user a video has been started -->
                <div class="Status">
                    <p><?php echo $Status2; ?></p>
                </div>
            </div>


             <!-- Class for the third Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam3-->
                <div class="image">
                    <figcaption> <b> Camera 3 </b> </figcaption>
                    <img src="CAM1.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
                <div class="buttons">
                    <div class="take picture">
                        <button name="camera3">Take Picture </button><!-- Create the button to take a photo -->
                        <button name="video3"> Start Video </button> <!-- Create button to start a video -->
                        <select size="1" name="seconds3"> <!-- Dropdown-menu to set the time of the video  -->
                            <option value="5">5s</option>
                            <option value="10">10s</option>
                            <option value="15">15s</option>
                            <option value="20">20s</option>
                        </select>
                    </div>
                </div>
                <!-- Tell the user a video has been started -->
                <div class="Status">
                    <p><?php echo $Status3; ?></p>
                </div>
            </div>

            <!-- Class for the fourth Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam4-->
                <div class="image">
                    <figcaption> <b> Camera 4 </b> </figcaption>
                    <img src="CAM1.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
                <div class="buttons">
                    <div class="take picture">
                        <button name="camera4">Take Picture </button><!-- Create the button to take a photo -->
                        <button name="video4"> Start Video </button> <!-- Create button to start a video -->
                        <select size="1" name="seconds4"> <!-- Dropdown-menu to set the time of the video  -->
                            <option value="5">5s</option>
                            <option value="10">10s</option>
                            <option value="15">15s</option>
                            <option value="20">20s</option>
                        </select>
                    </div>
                </div>
                <!-- Tell the user a video has been started -->
                <div class="Status">
                    <p><?php echo $Status4; ?></p>
                </div>

            </div>

        </div>

        <br><br><br>

        <!-- Create the table to show the current temperature and humidity -->
        <div class="Table">
            <div class="data">
                <table>
                    <tr>
                        <td>
                            <table>
                                <tr>
                                    <th> Camera </th>
                                    <th> Temperature[Â°C] </th>
                                    <th> Humidity[%] </th>
                                </tr>
                                <tr>
                                    <td>Cam 1</td>
                                    <td>
                                        <p><?php echo $temp1; ?></p> <!-- Write the temperature from the Cam 1 Pi -->
                                    </td>
                                    <td>
                                        <p><?php echo $humidity1; ?></p><!-- Write the humidity from the Cam 1 Pi  -->
                                    </td>
                                </tr>
                                <tr>
                                    <td>Cam 2</td>
                                    <td>
                                        <p><?php echo $temp2; ?></p> <!-- Write the temperature from the Cam 2 Pi -->
                                    </td>
                                    <td>
                                        <p><?php echo $humidity2; ?></p><!-- Write the humidity from the Cam 2 Pi -->
                                    </td>
                                </tr>
                                <tr>
                                    <td>Cam 3</td>
                                    <td>
                                        <p><?php echo $temp3; ?></p><!-- Write the temperature from the Cam 3 Pi -->
                                    </td>
                                    <td>
                                        <p><?php echo $humidity3; ?></p><!-- Write the humidity from the Cam 3 Pi -->
                                    </td>
                                </tr>
                                <tr>
                                    <td>Cam 4</td>
                                    <td>
                                        <p><?php echo $temp4; ?></p><!-- Write the temperature from the Cam 4 Pi -->
                                    </td>
                                    <td>
                                        <p><?php echo $humidity4; ?></p><!-- Write the humidity from the Cam 4 Pi -->
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table><br>
            </div>
            <!-- Create the button to refresh the temperature and humidity data -->
            <div class="renew">
                <button name="Data_new"> Refresh Data Test </button>
            </div>
            </form>

        </div>

    </main>

</body>

</html>
