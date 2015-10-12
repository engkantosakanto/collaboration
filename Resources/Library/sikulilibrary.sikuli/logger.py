# -*- coding: utf-8 -*-
from __future__ import with_statement
import logging
import datetime
import shutil
import common
import os
from sikuli import *

# hack to properly handle WARNING log level
logging.addLevelName(logging.WARNING, 'WARN')
# add HTML log level
HTML = logging.INFO + 5
logging.addLevelName(HTML, 'HTML')

class RobotHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self, level=logging.DEBUG)

    def emit(self, record):
        print self.format(record)

    def format(self, record):
        if not self.formatter:
            # add default formatter
            self.formatter = logging.Formatter('*%(levelname)s* %(message)s')
        return self.formatter.format(record)

class RobotLogger(logging.Logger):
    def __init__(self, name='robot', level=logging.INFO):
        if common.cfgLoggingLevel.lower() == 'debug':
            level = logging.DEBUG
        logging.Logger.__init__(self, name, level)
        self.addHandler(RobotHandler())

    def _get_unique_name(self, prefix="", suffix=""):
        now = datetime.datetime.now()
        return prefix + now.strftime('%Y-%m-%d_%H-%M-%S') + suffix

    def _create_screenshot_directory(self, argDir):
        if not os.path.exists(argDir):
            os.makedirs(argDir)
        return argDir

    def screenshot(self, msg="Screenshot: "):
        activeWindow = App.focusedWindow()
        activeWindowsRegion = (activeWindow.getX(), activeWindow.getY(), activeWindow.getW(), activeWindow.getH())
        folder = self._create_screenshot_directory(common.cfgScreenshots)
        name = self._get_unique_name(prefix="screenshot_", suffix=".png")
        img_src = capture(*activeWindowsRegion)
        shutil.copy(img_src, folder + '/' + name)
        self.html_img(msg, folder + '/' + name)

    def getResultFromClipboard(self):
        type('a', KEY_CTRL); wait(1)
        type('c', KEY_CTRL)
        return str(Env.getClipboard())
        
    def passed(self, msg, *args, **kwargs):
        self.info('PASS: ' + msg, *args, **kwargs)

    def failed(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.DEBUG):
            self.screenshot()
        raise common.VerificationFailed(msg)

    def html(self, msg, *args, **kwargs):
        self.log(HTML, msg, *args, **kwargs)

    def html_img(self, msg, image):
        #self.html('%s <img src="%s" width=500 />' % (msg, image))
        self.html('%s <img src="%s"/>' % (msg, image))

class BaseLogger(object):
    """ Base class for logging support """
    log = RobotLogger()

#============= Modification to RootLogger ===============#
# Use class RobotLogger instead of RootLogger as it support
# additional methods: passed(), failed()

# setup log level for RootLogger 
#logging.basicConfig(level=logging.INFO)
# remove default StreamHandler
#logging.getLogger('').removeHandler(logging.getLogger('').handlers[0])
# add RobotHandler to the RootLogger
#logging.getLogger('').addHandler(RobotHandler())
#========================================================#

# =============================================== #
#          Helper functions methods               #
# =============================================== #

# functions for accessing lastly searched images and region
_lastFoundImages = []
_lastFoundRegion = None
# flag for checking whether last image was already poped
# to prevent appearance old images in log file 
_is_new_image = 0

def getLastFoundImages():
    return _lastFoundImages

def getLastFoundImage():
    _is_new_image = 0
    return _lastFoundImages.pop()

def getLastFoundRegion():
    reg = _lastFoundRegion
    _lastFoundRegion = None
    return reg

def addFoundImage(img, reg=None):
    _lastFoundImages.append(img)
    _lastFoundRegion = reg
    _is_new_image = 1

# return filename from pattern's target object
def getFilename(target):
    try:
        filename = target.getFilename()
    except:
        filename = target
    return filename