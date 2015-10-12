*** Settings ***
Documentation     This resource contains all the keywords used for login and facebook login to the Freelancer Desktop App.
Library           sikulilibrary.SikuliMethods
Library           OperatingSystem
Resource          ../CommonResources/sikuli_keywords.robot
Resource          ../CommonResources/desktopapp_global_helper.robot
Resource          ../Variables/desktopapp_login_constants.robot
Resource          ../CommonResources/desktopapp_global_constants.robot

*** Keywords ***
# =============================================== #
#                       Given                     #
# =============================================== #

User Logs In With "${tc_USER_NAME}" And "${tc_USER_PASSWORD}"
    User Inputs "${tc_USER_NAME}" In "Desktop App Username" Field
    User Inputs "${tc_USER_PASSWORD}" In "Desktop App Password" Field
    User Clicks "${DESKTOPAPP_LOGIN_BUTTON}"

User Logs In With "${tc_USER_NAME}" And "${tc_USER_PASSWORD}" Via Facebook Login
    User Clicks "${DESKTOPAPP_FBLOGIN_BUTTON}"
    User Inputs "${tc_USER_NAME}" In "FBLogin Username" Field
    User Inputs "${tc_USER_PASSWORD}" In "FBLogin Password" Field
    User Clicks "${FBLOGIN_LOGIN_BUTTON}"

# =============================================== #
#                       When                      #
# =============================================== #

User Logs Out From The Desktop App
    User Clicks "${USERHOMEPAGE_EXPANDCONTEXTMENU_BUTTON}"
    User Clicks "${USERHOMEPAGE_LOGOUT_CONTEXTMENU}"
    User Confirms Logout

User Runs the "${tc_OS}" Desktop App
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Open Application    ${${tc_OS}_APPLICATION_INSTALLATION_DIRECTORY}/${${tc_OS}_DESKTOPAPP_EXECUTABLE}

User Is In Desktop App Login Page
    Switch Application Focus    ${FREELANCER_DESKTOPAPP_NAME}
    Wait For Image To Appear    ${DESKTOPAPP_LOGIN_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Assert That Image Should Exist    ${DESKTOPAPP_LOGIN_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Home Page Is Displayed
    Wait And Assert That "${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}" Is Visible
    Wait And Assert That "${USERHOMEPAGE_BROWSEPROJECTS_BUTTON}" Is Visible
    Wait And Assert That "${USERHOMEPAGE_MYWORK_BUTTON}" Is Visible

# =============================================== #
#                       Then                      #
# =============================================== #
User Should Be Able To View The Update Checker
    Wait In Seconds    1
    Run Keyword And Ignore Error
    ...    Assert That Image Should Exist    ${UPDATECHECKER_BACKGROUND}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Run Keyword And Ignore Error
    ...    Assert That Image Should Exist    ${UPDATECHECKER_STATUS}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Should Be Logged In Successfully
    User Home Page Is Displayed

User Should Not Be Able To Login
    User Home Page Should Not Be Displayed

User Should Be Successfully Logged Out
    User Is In Desktop App Login Page
    User Home Page Should Not Be Displayed

User Home Page Should Not Be Displayed
    Assert That Image Should Not Exist    ${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Assert That Image Should Not Exist    ${USERHOMEPAGE_BROWSEPROJECTS_BUTTON}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Assert That Image Should Not Exist    ${USERHOMEPAGE_MYWORK_BUTTON}    ${IMAGE_RECOGNITION_SENSITIVITY}


User Confirms Logout
    User Clicks "${USERHOMEPAGE_LOGOUTCONFIRMATION_BUTTON}"

User Closes The Desktop App
    User Clicks "${DESKTOPAPP_CLOSE_BUTTON}"

The "${tc_DESKTOPAPP_PROMPT}" Alert Should Be Displayed
    Run Keyword If    '${tc_DESKTOPAPP_PROMPT}' == 'Invalid username or password.'
    ...    Wait And Assert That "${DESKTOPAPP_LOGIN_INVALIDCREDENTIALS_ALERT}" Is Visible

# =============================================== #
#              Internal Keywords                  #
# =============================================== #

# ${p_fieldName} is either DesktopApp Username, DesktopApp Password, FBLogin Username or FBLogin Password
User Inputs "${p_fieldValue}" In "${p_fieldName}" Field
    User Inputs String "${p_fieldValue}" in "${${p_fieldName}_FIELD}" Field

Desktop App "${p_alertType}" Alert Should Be Launched
    Wait And Assert That "${DESKTOPAPP_LOGIN_${p_alertType}_ALERT}" Is Visible