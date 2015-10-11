
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
activeWindow = App.focusedWindow()

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
			
	def terminateApp(self, argAppName):
		#App.open("taskkill /f /im %s" % (argAppName,))
		try:
			myApp = self.getApp(argAppName)
			myApp.close()
		except FindFailed:
			self.log.failed("Unable to close the application: '%s'." % (argApp,))
		
	def setImageRecognitionSensitivity(self, *args):
		if(args[1] == "exact"):
			return Pattern(args[0]).exact()
		else:
			return Pattern(args[0]).similar(float(args[1]))

	def getAppRegion(self, argApp):
		myApp = self.getApp(argApp)
		myApp.focus(); wait(1)
		appWindow = myApp.window()
		appRegion = (appWindow.getX(), appWindow.getY(), appWindow.getW(), appWindow.getH())
		return appRegion
	
	def getActiveWindowsRegion(self):
	    activeWindowsRegion = (activeWindow.getX(), activeWindow.getY(), activeWindow.getW(), activeWindow.getH())
	    return activeWindowsRegion

	def captureWindow(self, *args):
		try:
			if(args[0] == "active"):
				region = self.getActiveWindowsRegion()
			else:
				region = self.getAppRegion(args[0])
			imgScreenshot = capture(*region)
			shutil.copy(imgScreenshot, str(args[1]))
		except FindFailed:
			self.log.failed("Application '%s' is not detected." % (args[0],))

	def by_y(match):
		return match.y

	def getImageRegionCoordinates(self, *args):
		s.find(self.setImageRecognitionSensitivity(args[0], args[1]))
		match = s.getLastMatch()
		self.appCoordinates = (match.getX(), match.getY(), match.getW(), match.getH())
		appRegion = Region(*self.appCoordinates)
	
	def getPatternsInRegion(self, *args):
		reg = self.getImageRegionCoordinates(args[0], args[1])
		listOfPatterns = []
		listOfSortedPatterns = []
		with reg.findAll(args[2]) as foundImages:
			while foundImages.hasNext():
				listOfPatterns.append(foundImages.next())
			listOfSortedPatterns = sorted(listOfPatterns, key=by_y)
		return listOfSortedPatterns
	
	def clickAllPatternsInRegion(self, *args):
		for pattern in getPatternsInRegion(args[0], args[1], args[2]):
			click(pattern)
			
	def getImageBasedOnReferenceImage(self, *args): # arguments: spatial location, reference image, target image, image recogniton sensitivity,
		imgRecognitionSensitivity = args[3]
		if (args[0] == "left"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).left().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		elif (args[0] == "right"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).right().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		elif (args[0] == "above"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).above().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		elif (args[0] == "below"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).below().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		elif (args[0] == "inside"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).inside().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		elif (args[0] == "nearby"):
			return activeWindow.find(self.setImageRecognitionSensitivity(args[1], imgRecognitionSensitivity)).nearby().find(self.setImageRecognitionSensitivity(args[2], imgRecognitionSensitivity))
		else:
			return None
		
	def userActionOnImageBasedOnReference(self, *args): # arguments: action, spatial location, reference image, target image, image sensitivity
		if (args[0] == "click"):
			click(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]))
		elif (args[0] == "doubleClick"):
			doubleClick(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]))
		elif (args[0] == "rightClick"):
			rightClick(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]))
		elif (args[0] == "type"):
			type(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]), args[5])
		elif (args[0] == "paste"):
			paste(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]), args[5])
		elif (args[0] == "dragDrop"):
			dragDrop(self.getImageBasedOnReferenceImage(args[1], args[2], args[3], args[4]), args[5])
			
	def setWaitValue(self, argDelay):
		s.wait(int(argDelay))

	def setSleepValue(self, argSleep):
		s.sleep(int(argSleep))
		
	def verifyApp(self, *args):
		# check application
		if activeWindow.exists(args[0]):
			self.log.passed("'%s' window appeared." % (args[1],))
		else:
			self.log.failed("No visible '%s' window." % (args[1],))
		MyApp = App(args[2])
		MyApp.focus()
		wait(1)
				
	def getXLSCellValue(self, *args):
		xls_file = str(args[0])
		xls_workbook = xlrd.open_workbook(xls_file)
		xls_sheet = xls_workbook.sheet_by_name(str(args[1]))
		cellValue = xls_sheet.cell(int(args[2]),int(args[3])).value
		return cellValue

	def imageExists(self, *args):
		try:
			activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1]))
			return True
		except FindFailed:
			return False
			
	def imageExistsInReferenceToAnotherImage(self, *args):
		try:
			activeWindow.find(self.getImageBasedOnReferenceImage(args[0], args[1], args[2], args[3]))
			return True
		except FindFailed:
			return False
        
	def getResultFromClipboard(self):
		type('c', KEY_CTRL)
		return str(Env.getClipboard())
		
	def pressKey(self, argKey):
		#s.focus()
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
		if (argKey == "DELETE"):
			activeWindow.type(Key.DELETE, KeyModifier.CTRL | KeyModifier.ALT)
		elif (argKey == "ESC"):
			activeWindow.type(Key.ESC, KeyModifier.CTRL | KeyModifier.ALT)
		else:
			sleep(1)
			
	def pressCtrlShiftPlusKey(self, argKey):
		#self.setFocus()
		if (argKey == "DELETE"):
			activeWindow.type(Key.DELETE, KeyModifier.CTRL | KeyModifier.SHIFT)
		else:
			sleep(1)
			
	def pressWindowsKeyPlusKey(self, argKey):
		#self.setFocus()
		if (argKey == "UP"):
			activeWindow.type(Key.UP, KeyModifier.KEY_WIN)
		elif (argKey == "DOWN"):
			activeWindow.type(Key.DOWN, KeyModifier.KEY_WIN)
		else:
			sleep(1)
			
	def pressCtrlPlusKey(self, argKey):
		#self.setFocus()
		activeWindow.type(argKey, KeyModifier.CTRL)
		sleep(1)
		
	def pressAltPlusKey(self, argKey):
		#self.setFocus()
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
			region = activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1]))
			for i in range(5):
				region.highlight(1)
				wait(0.5)
			#self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def hoverAtImage(self, *args):
		try:
			activeWindow.hover(self.setImageRecognitionSensitivity(args[0], args[1]))
			#self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def scrollFromReferenceImage(self, *args):
		try:
			activeWindow.wheel(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]), int(args[3]))
			#self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def dragImage(self, *args):
		try:
			activeWindow.drag(self.setImageRecognitionSensitivity(args[0], args[1]))
			#self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def dropToImage(self, *args):
		try:
			activeWindow.dropAT(self.setImageRecognitionSensitivity(args[0], args[1]))
			#self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def clickImage(self, *args):
		try:
			activeWindow.click(self.setImageRecognitionSensitivity(args[0], args[1]))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
		
	def clickImageinXY(self, *args):
		try:
			activeWindow.click(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
	
	def doubleClickImage(self, *args):
		try:
			activeWindow.doubleClick(self.setImageRecognitionSensitivity(args[0], args[1]))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (argImage,))
	
	def doubleClickImageinXY(self, *args):
		try:
			activeWindow.doubleClick(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
		
	def rightClickImage(self, *args):
		try:
			activeWindow.rightClick(self.setImageRecognitionSensitivity(args[0], args[1]))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (argImage,))	
	
	def rightClickImageinXY(self, *args):
		try:
			activeWindow.rightClick(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])))
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
		
	def waitForImageToBeVisible(self, *args):
		try:
			if (args[1] == 'FOREVER'):			
				activeWindow.wait(self.setImageRecognitionSensitivity(args[0], args[1]), FOREVER)
			else:
				activeWindow.wait(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))
		
	def waitForImageToVanish(self, *args):#arguments: image(path or filename), time (s)
		try:
			if (args[1] == 'FOREVER'):			
				activeWindow.waitVanish(self.setImageRecognitionSensitivity(args[0], args[1]), FOREVER)
			else:
				activeWindow.waitVanish(self.setImageRecognitionSensitivity(args[0], args[1]), int(args[2]))
		except FindFailed:
			self.log.failed("Matching UI with '%s' persists." % (args[0],))
		
	def typeText(self, argText):
		activeWindow.type(argText)

	def typeTextInsideImageXY(self, *args):
		try:
			activeWindow.type(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])), args[4])
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def pasteText(self, argText):
		activeWindow.paste(argText)

	def pasteTextInsideImageXY(self, *args):
		try:
			activeWindow.paste(self.setImageRecognitionSensitivity(args[0], args[1]).targetOffset(int(args[2]), int(args[3])), args[4])
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))	
		
	def assertImageExists(self, *args): #arguments: image(path or filename), image recogniton sensitivity,
		try:
			assert exists(self.setImageRecognitionSensitivity(args[0], args[1]))
			self.log.passed("UI matched with reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))

	def assertImageNotExists(self, *args): #arguments: image(path or filename), image recogniton sensitivity,
		try:
			#if not exists(self.setImageRecognitionSensitivity(args[0], args[1])):
			assert not exists(self.setImageRecognitionSensitivity(args[0], args[1]))
			self.log.passed("No matching UI detected on screen in reference to image: '%s'." % (args[0],))
		except FindFailed:
			self.log.failed("UI matched with reference image: '%s'." % (args[0],))
	
	def readText(self, *args): #arguments: image(path or filename), image recogniton sensitivity, offset (pixels), spatial location
		offsetVal = int(args[2])
		try:
			if(args[3] == 'Right'):
				return activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1])).right(offsetVal).text()
			elif(args[3] == 'Left'):
				return activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1])).left(offsetVal).text()
			elif(args[3] == 'Above'):
				return activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1])).above(offsetVal).text()
			elif(args[3] == 'Below'):
				return activeWindow.find(self.setImageRecognitionSensitivity(args[0], args[1])).below(offsetVal).text()
			self.log.passed("UI load successful. Reference image:'%s'." % (args[0],))
		except FindFailed:
			self.log.failed("No matching UI detected on screen or '%s' does not exist." % (args[0],))