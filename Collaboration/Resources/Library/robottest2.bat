@echo off

set sikulix_jar=JarFiles/sikulixapi.jar
set robot_framework_jar=JarFiles/robotframework-2.9.1.jar

java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath=sikulilibrary.sikuli ^
     --outputdir=. ^
     --loglevel=TRACE ^
     %*