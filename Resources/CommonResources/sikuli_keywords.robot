*** Settings ***
Library           sikulilibrary.SikuliMethods
Resource          desktopapp_global_constants.robot

*** Keywords ***
# =============================================== #
#                    Image assertions             #
# =============================================== #
Assert That Image Should Exist
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Assert Image Exists    ${p_image}    ${p_imageRecognitionSensitivity}

Assert That Image Should Not Exist
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Assert Image Not Exists    ${p_image}    ${p_imageRecognitionSensitivity}

Verify If Image Does Not Exist Based On Reference Image
    [Arguments]    ${p_imageSpatialLocation}    ${p_referenceImage}    ${p_image}    ${p_imageRecognitionSensitivity}
    ${TrueFalse} =    Run Keyword
    ...    Image Exists In Reference To Another Image    ${p_imageSpatialLocation}    ${p_referenceImage}
    ...    ${p_image}    ${p_imageRecognitionSensitivity}
    [Return]    ${TrueFalse}

Verify If Image Does Not exist
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    ${TrueFalse} =    Run Keyword    Image Exists    ${p_image}    ${p_imageRecognitionSensitivity}
    Should Not Be True    ${TrueFalse}

Verify If Image Exists
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    ${img}=    Image Exists    ${p_image}    ${p_imageRecognitionSensitivity}
    [Return]    ${img}

Verify If Image Exists Based On Reference Image
    [Arguments]    ${p_imageSpatialLocation}    ${p_referenceImage}    ${p_image}    ${p_imageRecognitionSensitivity}
    ${TrueFalse} =    Run Keyword
    ...    Image Exists In Reference To Another Image    ${p_imageSpatialLocation}    ${p_referenceImage}
    ...    ${p_image}    ${p_imageRecognitionSensitivity}
    [Return]    ${TrueFalse}

# =============================================== #
#                   User Actions                  #
# =============================================== #
Click Application Image
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Click image    ${p_image}    ${p_imageRecognitionSensitivity}

Click Image In XY Coordinates
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${xCoordinate}    ${yCoordinate}
    clickImageinXY    ${p_image}    ${p_imageRecognitionSensitivity}    ${xCoordinate}    ${yCoordinate}

Close Application
    [Arguments]    ${g_APPLICATION_NAME}
    Terminate App    ${g_APPLICATION_NAME}

Doubleclick Application Image
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Doubleclick image    ${p_image}    ${p_imageRecognitionSensitivity}

Doubleclick Image In XY Coordinates
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${xCoordinate}    ${yCoordinate}
    Doubleclick Image in XY    ${p_image}    ${p_imageRecognitionSensitivity}    ${xCoordinate}    ${yCoordinate}

Get String From Region
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_Offset}    ${p_region}
    [Documentation]    Returns the string from a region
    Run Keyword If    '${p_region}' == 'Right'
    ...    Read Text    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_Offset}    ${p_region}
    Run Keyword If    '${p_region}' == 'Left'
    ...    Read Text    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_Offset}    ${p_region}
    Run Keyword If    '${p_region}' == 'Above'
    ...    Read Text    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_Offset}    ${p_region}
    Run Keyword If    '${p_region}' == 'Below'
    ...    Read Text    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_Offset}    ${p_region}

Input Strings
    [Arguments]    ${p_string}
    Type text    ${p_string}

Input Strings In Image XY Coordinates
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_xOffset}    ${p_yOffset}    ${p_String}
    Type Text Inside Image XY    ${p_image}    ${p_imageRecognitionSensitivity}
    ...    ${p_xOffset}    ${p_yOffset}    ${p_String}

Paste Strings
    [Arguments]    ${p_string}
    Paste Text    ${p_string}

Paste Strings In Image XY coordinates
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_xOffset}    ${p_yOffset}    ${p_String}
    Paste Text Inside Image XY    ${p_image}    ${p_imageRecognitionSensitivity}
    ...    ${p_xOffset}    ${p_yOffset}    ${p_String}

Right-click Application Image
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Rightclick Image    ${p_image}    ${p_imageRecognitionSensitivity}

Right-click Image In XY Coordinates
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_xOffset}    ${p_yOffset}
    Rightclick Image in XY    ${p_image}    ${p_imageRecognitionSensitivity}
    ...    ${p_xOffset}    ${p_yOffset}

Highlight App Region
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Highlight Region    ${p_image}    ${p_imageRecognitionSensitivity}

Get Screenshot
    [Arguments]    ${p_App}    ${p_Screenshot_Directory}
    Capture Window    ${p_App}    ${p_Screenshot_Directory}

Get SUT OS
    ${t_OS}=    Get Env OS
    [Return]    ${t_OS}

Get SUT OS Version
    ${t_OS_Version}=    Get Env OS Version
    [Return]    ${t_OS_Version}

Confirm SUT OS
    [Arguments]    ${p_OS}
    ${t_Is_Correct_OS}=    Confirm OS    ${p_OS}
    [Return]    ${t_Is_Correct_OS}

Open Application
    [Arguments]    ${g_APPLICATION_PATH}
    Wait Until Keyword Succeeds    ${TIMEOUT}    ${RETRY_INTERVAL}
    ...    Start App    ${g_APPLICATION_PATH}

Sleep In Seconds
    [Arguments]    ${p_seconds}
    Set Sleep Value    ${p_seconds}

Start Application
    [Arguments]    ${g_APPLICATION_PATH}
    Start App    ${g_APPLICATION_PATH}
    #Set Application Focus    ${FREELANCER_DESKTOPAPP_NAME}

Get Pattern Count In Active Region
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}
    Get Pattern Count In Region    ${p_image}    ${p_imageRecognitionSensitivity}

Click xth Pattern In Active Region
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_index}
    Click A Pattern In Reference Image    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_index}

Get Pattern Count In Reference Image
    [Arguments]    ${p_referenceImage}    ${p_targetImage}    ${p_imageRecognitionSensitivity}
    Get Pattern Count In Image    ${p_referenceImage}    ${p_targetImage}    ${p_imageRecognitionSensitivity}

Click xth Pattern In Reference Image
    [Arguments]    ${p_referenceImage}    ${p_targetImage}    ${p_imageRecognitionSensitivity}    ${p_index}
    Click A Pattern In Reference Image    ${p_referenceImage}    ${p_targetImage}
    ...    ${p_imageRecognitionSensitivity}    ${p_index}

Set Default Image Library Path
    [Arguments]    ${p_imageLibraryPath}
    Set Image Library Path    ${p_imageLibraryPath}

# =============================================== #
#                       Wait                      #
# =============================================== #

Wait For Image To Appear
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_seconds}
    Wait For Image To Be Visible    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_seconds}

Wait For Image To Disappear
    [Arguments]    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_seconds}
    Wait For Image to Vanish    ${p_image}    ${p_imageRecognitionSensitivity}    ${p_seconds}

Wait In Seconds
    [Arguments]    ${p_seconds}
    Set Wait Value    ${p_seconds}

# =============================================== #
#                    Run Scripts                  #
# =============================================== #

Run Script
    [Arguments]    ${p_script}
    Run Command    ${p_script}

# =============================================== #
#           Set Application Focus                 #
# =============================================== #

Set Application Focus
    [Arguments]    ${p_application_name}
    Set App Focus    ${p_application_name}

Switch Application Focus
    [Arguments]    ${p_application_name}
    Switch App Focus    ${p_application_name}

# =============================================== #
#                 Keyboard Actions                #
# =============================================== #

Press "${p_keyboardKey}" key
    Press Key    ${p_keyboardKey}

Press CTRL + ALT + "${p_keyboardKey}"
    Press Ctrl Alt Plus Key    ${p_keyboardKey}

Press CTRL + Shift + "${p_keyboardKey}"
    Press Ctrl Shift Plus Key    ${p_keyboardKey}

Press "${p_keyboardKey}" Key "${PRESS_COUNT}" Times
    Press Key N Times    ${p_keyboardKey}    ${PRESS_COUNT}

Press CTRL + "${p_keyboardKey}"
    Press Ctrl Plus Key    ${p_keyboardKey}

Press Windows Key + "${p_keyboardKey}"
    Press Windows Key Plus Key    ${p_keyboardKey}

Press ALT + "${p_keyboardKey}"
    Press ALT Plus Key    ${p_keyboardKey}

