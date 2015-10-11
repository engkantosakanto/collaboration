@echo off

set sikulix_jar=JarFiles/sikuli-script.jar
set robot_framework_jar=JarFiles/robotframework-2.8.7.jar
set sikuli_library=sikulilibrary.sikuli

java -cp "%robot_framework_jar%;%sikulix_jar%" ^
     -Dpython.path="%sikulix_jar%/Lib" ^
     org.robotframework.RobotFramework ^
     --pythonpath="%sikuli_library%" ^
     --loglevel=TRACE ^
     %*