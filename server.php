<!doctype html>
<html>


<?php
    
//----------------------------------------------------------------------------------------------//
//Version    : 1.0
//Date       : 29.06.2022
//Description: This Code create a Website to show the neweset picture of the camera surveillance
//             and the and the latest temperature and humidity of the cameras' environment. This 
//             Website refresh every 5 seconds to get the newest data.
//
//----------------------------------------------------------------------------------------------//

// get the temperature near the camera
$temp1 = file("/home/pi/CAM1/Measurements/tempcam1.txt")[0];
$temp2 = file("/home/pi/CAM2/Measurements/tempcam2.txt")[0];
$temp3 = file("/home/pi/CAM3/Measurements/tempcam3.txt")[0];
$temp4 = file("/home/pi/CAM4/Measurements/tempcam4.txt")[0];
// get the humidity near the camera
$humidity1 = file("/home/pi/CAM1/Measurements/humcam1.txt")[0];
$humidity2 = file("/home/pi/CAM2/Measurements/humcam2.txt")[0];
$humidity3 = file("/home/pi/CAM3/Measurements/humcam3.txt")[0];
$humidity4 = file("/home/pi/CAM4/Measurements/humcam4.txt")[0];
?>


</ / Head Settings>

<head>
    <link rel="stylesheet" href="stylesheet.css">
    </ / seperate stylecheet for website>
    <meta http-equiv="refresh" content="5">
    </ / relaod intervall>
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
            </div>

            <!-- Class for the second Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam2-->
                <div class="image">
                    <figcaption> <b> Camera 2 </b> </figcaption>
                    <img src="CAM2.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
            </div>


             <!-- Class for the third Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam3-->
                <div class="image">
                    <figcaption> <b> Camera 3 </b> </figcaption>
                    <img src="CAM3.jpg" alt="TEST"> <!-- Name from the latest picture -->
                </div>
            </div>

            <!-- Class for the fourth Camera -->
            <div class="camera">
                <!-- Class to show the current picture of Cam4-->
                <div class="image">
                    <figcaption> <b> Camera 4 </b> </figcaption>
                    <img src="CAM4.jpg" alt="TEST"> <!-- Name from the latest picture -->
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
                                    <th> Temperature[°C] </th>
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
        </div>

    </main>

</body>

</html>

