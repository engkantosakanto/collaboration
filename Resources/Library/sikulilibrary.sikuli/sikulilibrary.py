
# This file contains the SikuliMethods class containing the most commonly used Sikuli methods.

from __future__ import with_statement
from sikuli import *
from logger import *
import shutil

# Sets the OcrText functions to True. When set to True, Sikuli's text() function can be used. 
# Note that the host computer should have Ocr installed 
Settings.OcrTextSearch = True
Settings.OcrTextRead = True

# Global declaration of variables used for the Region function
s = Screen()

class SikuliMethods(BaseLogger):
    # Initializes the visible region to the computer resolution.
    def __init__(self):
        self.appCoordinates = (SCREEN.getX(), SCREEN.getY(), SCREEN.getW(), SCREEN.getH())
    # Function to set the path for the image library.
    def setImageLibraryPath(self, argImgLibraryPath):
        addImagePath(argImgLibraryPath)
    # Replace string with another string. Arguments arg[0] string, 
    # arg[1] string to be replaced, arg[2] string that will replace arg[1]
    def replaceText(self, *args):
        return args[0].replace(args[1], args[2])
    # Function to starts the application.
    def startApp(self, argApp):
        try:
            fda = App("Freelancer Desktop App")
            if not fda.isRunning():
                openApp(str(argApp))
                while not fda.isRunning():
                    wait(1)
        except FindFailed:
            self.log.failed("Unable to launch the application: '%s'." % (argApp,))

    def getApp(self, argApp):
        myApp = App(str(argApp))
        return myApp
    # Function to get the OS, ex: WINDOWS, MAC, UNIX
    def getEnvOS(self):
        return str(Env.getOS())
    # Get OS version
    def getEnvOSVersion(self):
        return str(Env.getOSVersion())
    # Check if OS version is correct based on the argument argOS
    def confirmOS(self, argOS):
        if(argOS == "Windows"):
            return Settings.isWindows()
        elif (argOS == "Mac"):
            return Settings.isMac()
        elif (argOS == "Linux"):
            return Settings.isLinux()
        else:
            return None
    # Switches focus based on specified application name: Ex. Freelancer Desktop App
    def switchAppFocus(self, argApp):
        try:
            switchApp(str(argApp))
        except FindFailed:
            self.log.failed("Unable to swith to application: '%s'." % (argApp,))
    # Runs a command in command line
    def runCommand(self, argCommand):
        run(argCommand)
    # Sets focus based on specified application name
    def setAppFocus(self, argAppName):
        try:
            myApp = self.getApp(argAppName)
            myApp.focus()
            wait(1)
        except FindFailed:
            self.log.failed("Unable to set focus to the application: '%s'." % (argApp,))
    # Terminates the specified app based on parameter argAppName
    def terminateApp(self, argAppName):
        #App.open("taskkill /f /im %s" % (argAppName,))
        try:
            myApp = self.getApp(argAppName)
            myApp.close()
        except FindFailed:
            self.log.failed("Unable to close the application: '%s'." % (argApp,))
    # Sets the image recognition sensitivity to either exact or user defined value. 
    def setImageRecognitionSensitivity(self, *args): #arguments: image file, sensitivit from 0.00 to 0.99
        if(args[1] == "exact"):
            return Pattern(args[0]).exact()
        else:
            return Pattern(args[0]).similar(float(args[1]))
    # Gets the application region of a specific application as defined in argApp
    def getAppRegion(self, argApp):
        myApp = self.getApp(argApp)
        myApp.focus(); wait(1) # sets the application in focus
        appWindow = myApp.window() # gets the application window
        appRegion = (appWindow.getX(), appWindow.getY(), appWindow.getW(), appWindow.getH()) # gets the region of the application in focus
        return appRegion

    # Takes screenshot of either the whole window or the application in focus
    def captureWindow(self, *args):
        try:
            if(args[0] == "active"):
                region = self.getActiveWindowsCoordinates()
            else:
                region = self.getAppRegion(args[0])
            imgScreenshot = capture(*region)
            shutil.copy(imgScreenshot, str(args[1]))
        except FindFailed:
            self.log.failed("Application '%s' is not detected." % (args[0],))
    # Gets the region of the application or window that is in focus
    def getActiveWindowsCoordinates(self):
        activeWindow = App.focusedWindow();
        activeWindowsCoordinates = (activeWindow.getX(), activeWindow.getY(), activeWindow.getW(), activeWindow.getH())
        setROI(*activeWindowsCoordinates) #limit the search region
        return activeWindowsCoordinates

    def getActiveWindowsRegion(self):
        activeWindowsRegion = Region(*self.getActiveWindowsCoordinates())
        return activeWindowsRegion

    def getImageCoordinates(self, *args):
        s.find(self.setImageRecognitionSensitivity(args[0], args[1]))
        match = s.getLastMatch()
        self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
        appRegion = Region(*self.appCoordinates)

    def getImageRegion(self, *args):
        activeWindowsRegion = Region(*self.getImageCoordinates(*args))
        return activeWindowsRegion


    # Gets the matching pattern in the regio and sort it from top > down
    def imageOrder(match):
        return match.x, match.y

    # args[0] image or pattern to search, args[1] image sensitivity
    # Returns an array of all the matching images in screen
    # args[0] = image path; args[1] = image sensitivity from 0.00 to 0.99
    def getPatternsInRegion(self, *args):
        activeWindowsCoordinates = self.getActiveWindowsCoordinates()
        activeWindowsRegion = Region(*activeWindowsCoordinates)
        listOfPatterns = []; listOfSortedPatterns = []
        foundPatterns =  activeWindowsRegion.findAll(self.setImageRecognitionSensitivity(*args))
        while foundPatterns.hasNext():
            listOfPatterns.append(foundPatterns.next())
        listOfSortedPatterns = sorted(listOfPatterns, key=imageOrder)
        return listOfSortedPatterns

    # Clicks all matching patterns in a region
    def clickAllPatternsInRegion(self, *args):
        for pattern in self.getPatternsInRegion(*args):
            click(pattern)

    # Clicks all matching patterns in a region
    def clickAPatternInRegion(self, *args):
        self.getPatternsInRegion(*args)[args[2]].click()

    # Get the count of all matching images based on the recognition sensitivity
    # args[0] = image path; args[1] = image sensitivity from 0.00 to 0.99
    def getImageCountInRegion(self, *args):
        return len(self.getPatternsInRegion(*args))


    # args[0] reference Image, args[1] image or pattern to search, args[2] image sensitivity
    def getPatternsInReferenceImage(self, *args):
        reg = self.getImageRegion(args[0], args[1])
        listOfPatterns = []; listOfSortedPatterns = []
        foundPatterns =  reg.findAll(args[2])
        while foundPatterns.hasNext():
            listOfPatterns.append(foundPatterns.next())
        listOfSortedPatterns = sorted(listOfPatterns, key=imageOrder)
        return listOfSortedPatterns

    # Clicks a specific pattern in a reference image
    def clickAllPatternsInReferenceImage(self, *args):
        for pattern in self.getPatternsInReferenceImage(*args):
            click(pattern)
    # Checks the pattern based on spatial location of another image     
    def getImageBasedOnReferenceImage(self, *args): # arguments: spatial location, reference image, target image, image recogniton sensitivity
        imgRecognitionSensitivity = args[3]
        targetImage = activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity))
        referenceImage = activeWindow.find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
        if (args[0] == "left"):
            return targetImage.left().referenceImage
        elif (args[0] == "right"):
            return targetImage.right().referenceImage
        elif (args[0] == "above"):
            return targetImage.above().referenceImage
        elif (args[0] == "below"):
            return targetImage.below().referenceImage
        elif (args[0] == "inside"):
            return targetImage.inside().referenceImage
        elif (args[0] == "nearby"):
            return targetImage.nearby().referenceImage
        else:
            return None
    # Sets the user action on the target image
    def userActionOnImageBasedOnReference(self, *args): # arguments: action, spatial location, reference image, target image, image sensitivity
        img = self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4])
        if (args[0] == "click"):
            click(img)
        elif (args[0] == "doubleClick"):
            doubleClick(img)
        elif (args[0] == "rightClick"):
            rightClick(img)
        elif (args[0] == "type"):
            type(img, args[5])
        elif (args[0] == "paste"):
            paste(img, args[5])
        elif (args[0] == "dragDrop"):
            dragDrop(img, args[5])
    # Sets the wait value       
    def setWaitValue(self, argDelay):
        s.wait(int(argDelay))
    # Sets the sleep value
    def setSleepValue(self, argSleep):
        s.sleep(int(argSleep))
    # Verifies if the application is active
    def verifyAppIsRunning(self, *args):
        try:
            activeWindow = App.focusedWindow(); wait(0.5)
            activeWindow.exists(args[0])
            self.log.passed("'%s' window appeared." % (args[1],))
            MyApp = App(args[2])
            MyApp.focus()
            wait(1)
        except FindFailed:
            self.log.failed("No visible '%s' window." % (args[1],))

    def getXLSCellValue(self, *args):
        xls_file = str(args[0])
        xls_workbook = xlrd.open_workbook(xls_file)
        xls_sheet = xls_workbook.sheet_by_name(str(args[1]))
        cellValue = xls_sheet.cell(int(args[2]),int(args[3])).value
        return cellValue

    def imageExists(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.find(self.setImageRecognitionSensitivity(*args))
            return True
        except FindFailed:
            return False
            
    def imageExistsInReferenceToAnotherImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.find(self.getImageBasedOnReferenceImage(args[0], args[1], args[2], args[3]))
            return True
        except FindFailed:
            return False
        
    def getResultFromClipboard(self):
        type('c', KEY_CTRL)
        return str(Env.getClipboard())
        
    def pressKey(self, argKey):
        #s.focus()
        activeWindow = App.focusedWindow(); wait(0.5)
        if (argKey == "ENTER"):
            activeWindow.type(Key.ENTER)
        elif (argKey == "TAB"):
            activeWindow.type(Key.TAB)
        elif (argKey == "ESC"):
            activeWindow.type(Key.ESC)
        elif (argKey == "SPACE"):
            activeWindow.type(Key.SPACE)
        elif (argKey == "UP"):
            activeWindow.type(Key.UP)
        elif (argKey == "DOWN"):
            activeWindow.type(Key.DOWN)
        elif (argKey == "LEFT"):
            activeWindow.type(Key.LEFT)
        elif (argKey == "RIGHT"):
            activeWindow.type(Key.RIGHT)
        elif (argKey == "DELETE"):
            activeWindow.type(Key.DELETE)
        elif (argKey == "INSERT"):
            activeWindow.type(Key.INSERT)
        elif (argKey == "PAGE_UP"):
            activeWindow.type(Key.PAGE_UP)
        elif (argKey == "PAGE_DOWN"):
            activeWindow.type(Key.PAGE_DOWN)
        elif (argKey == "HOME"):
            activeWindow.type(Key.HOME)
        elif (argKey == "END"):
            activeWindow.type(Key.END)
        elif (argKey == "F1"):
            activeWindow.type(Key.F1)
        elif (argKey == "F2"):
            activeWindow.type(Key.F2)
        elif (argKey == "F3"):
            activeWindow.type(Key.F3)
        elif (argKey == "F4"):
            activeWindow.type(Key.F4)
        elif (argKey == "F5"):
            activeWindow.type(Key.F5)
        elif (argKey == "F6"):
            activeWindow.type(Key.F6)
        elif (argKey == "F7"):
            activeWindow.type(Key.F7)
        elif (argKey == "F8"):
            activeWindow.type(Key.F8)
        elif (argKey == "F9"):
            activeWindow.type(Key.F9)
        elif (argKey == "F10"):
            activeWindow.type(Key.F10)
        elif (argKey == "F11"):
            activeWindow.type(Key.F11)
        elif (argKey == "F12"):
            activeWindow.type(Key.F12)
        else:
            activeWindow.type(argKey)
            
    def pressCtrlAltPlusKey(self, argKey):
        #self.setFocus()
        activeWindow = App.focusedWindow(); wait(0.5)
        if (argKey == "DELETE"):
            activeWindow.type(Key.DELETE, KeyModifier.CTRL | KeyModifier.ALT)
        elif (argKey == "ESC"):
            activeWindow.type(Key.ESC, KeyModifier.CTRL | KeyModifier.ALT)
        else:
            sleep(1)
            
    def pressCtrlShiftPlusKey(self, argKey):
        #self.setFocus()
        activeWindow = App.focusedWindow(); wait(0.5)
        if (argKey == "DELETE"):
            activeWindow.type(Key.DELETE, KeyModifier.CTRL | KeyModifier.SHIFT)
        else:
            sleep(1)
            
    def pressWindowsKeyPlusKey(self, argKey):
        #self.setFocus()
        activeWindow = App.focusedWindow(); wait(0.5)
        if (argKey == "UP"):
            activeWindow.type(Key.UP, KeyModifier.KEY_WIN)
        elif (argKey == "DOWN"):
            activeWindow.type(Key.DOWN, KeyModifier.KEY_WIN)
        else:
            sleep(1)
            
    def pressCtrlPlusKey(self, argKey):
        #self.setFocus()
        activeWindow = App.focusedWindow(); wait(0.5)
        activeWindow.type(argKey, KeyModifier.CTRL)
        sleep(1)
        
    def pressAltPlusKey(self, argKey):
        #self.setFocus()
        activeWindow = App.focusedWindow(); wait(0.5)
        activeWindow.type(argKey, KeyModifier.ALT)
        sleep(1)
            
    def pressKeyNTimes(self, *args):
      if(int(args[1]) < 1):
        wait(0)
      else:
        pressCount = 1
        while( pressCount <= int(args[1])):
          self.pressKey(args[0])
          pressCount = pressCount + 1
            
    def clearTextField(self):
        self.pressCtrlPlusKey("a")
        self.pressKey("DELETE")
        
    def clearComboboxField(self):
        self.pressCtrlPlusKey("DELETE")

    def highlightRegion(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            region = activeWindow.find(self.setImageRecognitionSensitivity(*args))
            for i in range(5):
                region.highlight(1)
                wait(0.5)
            #self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def hoverAtImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.hover(self.setImageRecognitionSensitivity(args[0], args[1]))
            #self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def scrollFromReferenceImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.wheel(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]), int(args[3]))
            #self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def dragImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.drag(self.setImageRecognitionSensitivity(args[0], args[1]))
            #self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def dropToImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.dropAT(self.setImageRecognitionSensitivity(args[0], args[1]))
            #self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def clickImage(self, *args):
        try:
            setROI(*self.getActiveWindowsCoordinates())
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.click(self.setImageRecognitionSensitivity(args[0], args[1]))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
        
    def clickImageinXY(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.click(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
    
    def doubleClickImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.doubleClick(self.setImageRecognitionSensitivity(args[0], args[1]))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (argImage,))
    
    def doubleClickImageinXY(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.doubleClick(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
        
    def rightClickImage(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.rightClick(self.setImageRecognitionSensitivity(args[0], args[1]))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (argImage,))  
    
    def rightClickImageinXY(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.rightClick(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
        
    def waitForImageToBeVisible(self, *args):
        try:
            setROI(*self.getActiveWindowsCoordinates())
            #activeWindow = self.getActiveWindowsRegion(); wait(0.5)
            if (args[1] == 'FOREVER'):          
                s.wait(self.setImageRecognitionSensitivity(args[0], args[1]), FOREVER)
            else:
                s.wait(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
        
    def waitForImageToVanish(self, *args):#arguments: image(path or filename), time (s)
        try:
            activeWindow = App.focusedWindow()
            if (args[1] == 'FOREVER'):          
                activeWindow.waitVanish(self.setImageRecognitionSensitivity(args[0], args[1]), FOREVER)
            else:
                activeWindow.waitVanish(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]))
        except FindFailed:
            self.log.failed("Matching UI with '%s' persists." % (args[0],))
        
    def typeText(self, argText):
        activeWindow = self.getActiveWindowsRegion()
        activeWindow.type(argText)

    def typeTextInsideImageXY(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.type(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])), args[4])
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def pasteText(self, argText):
        activeWindow = self.getActiveWindowsRegion()
        activeWindow.paste(argText)

    def pasteTextInsideImageXY(self, *args):
        try:
            activeWindow = self.getActiveWindowsRegion()
            activeWindow.paste(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])), args[4])
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))   
        
    def assertImageExists(self, *args): #arguments: image(path or filename), image recogniton sensitivity,
        try:
            setROI(*self.getActiveWindowsCoordinates())
            assert exists(self.setImageRecognitionSensitivity(*args))
            self.log.passed("UI matched with reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

    def assertImageNotExists(self, *args): #arguments: image(path or filename), image recogniton sensitivity,
        try:
            setROI(*self.getActiveWindowsCoordinates())
            #if not exists(self.setImageRecognitionSensitivity(args[0], args[1])):
            assert not exists(self.setImageRecognitionSensitivity(args[0], args[1]))
            self.log.passed("No matching UI detected on screen in reference to image: '%s'." % (args[0],))
        except FindFailed:
            self.log.failed("UI matched with reference image: '%s'." % (args[0],))
    
    def readText(self, *args): #arguments: image(path or filename), image recogniton sensitivity, offset (pixels), spatial location
        activeWindow = self.getActiveWindowsRegion()
        offsetVal = int(args[2])
        img = activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1]))
        try:
            if(args[3] == 'Right'):
                return img.right(offsetVal).text()
            elif(args[3] == 'Left'):
                return img.left(offsetVal).text()
            elif(args[3] == 'Above'):
                return img.above(offsetVal).text()
            elif(args[3] == 'Below'):
                return img.below(offsetVal).text()
            self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
        except FindFailed:
            self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))