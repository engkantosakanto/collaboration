*** Settings ***
Documentation     This resource contains all the keywords used for login and facebook login to the Freelancer Desktop App.
Library           sikulilibrary.SikuliMethods
Library           OperatingSystem
Resource          ../CommonResources/sikuli_keywords.robot
Resource          ../CommonResources/desktopapp_global_helper.robot
Resource          ../Variables/desktopapp_login_constants.robot
Resource          ../CommonResources/desktopapp_global_constants.robot

*** Keywords ***
User Runs the "${tc_OS}" Desktop App
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Start Application    ${WINDOWS_APPLICATION_INSTALLATION_DIRECTORY}/${WINDOWS_DESKTOPAPP_EXECUTABLE}

User Logs In With "${tc_USER_NAME}" And "${tc_USER_PASSWORD}"
    User Inputs Username "${tc_USER_NAME}"
    User Inputs Password"${tc_USER_PASSWORD}"
    User Clicks "${DESKTOPAPP_LOGIN_BUTTON}"

User Logs In With "${tc_USER_NAME}" And "${tc_USER_PASSWORD}" Via Facebook Login
    User Clicks "${DESKTOPAPP_FBLOGIN_BUTTON}"
    User Inputs FB Username "${tc_USER_NAME}"
    User Inputs FB Password"${tc_USER_PASSWORD}"
    User Clicks "${FBLOGIN_LOGIN_BUTTON}"

User Should Be Able To View The Update Checker
    Wait In Seconds    1
    Run Keyword And Ignore Error
    ...    Assert That Image Should Exist    ${UPDATECHECKER_BACKGROUND}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Run Keyword And Ignore Error
    ...    Assert That Image Should Exist    ${UPDATECHECKER_STATUS}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Should Be Logged In Successfully
    Wait And Assert That "${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}" Is Visible
    Wait And Assert That "${USERHOMEPAGE_BROWSEPROJECTS_BUTTON}" Is Visible
    Wait And Assert That "${USERHOMEPAGE_MYWORK_BUTTON}" Is Visible

User Should Not Be Able To Login
    User Home Page Should Not Be Displayed

User Logs Out From The Desktop App
    User Clicks "${USERHOMEPAGE_EXPANDCONTEXTMENU_BUTTON}"
    User Clicks "${USERHOMEPAGE_LOGOUT_CONTEXTMENU}"
    User Confirms Logout

User Should Be Successfully Logged Out
    User Home Page Should Not Be Displayed
    User Is In Desktop App Login Page

User Inputs Username "${t_userName}"
    User Inputs String "${t_userName}" in "${DESKTOPAPP_USERNAME_FIELD}" Field

User Inputs Password"${t_userPassword}"
    User Inputs String "${t_userPassword}" in "${DESKTOPAPP_PASSWORD_FIELD}" Field

User Inputs FB Username "${t_userName}"
    User Inputs String "${t_userName}" in "${FBLOGIN_EMAILORPHONE_FIELD}" Field

User Inputs FB Password"${t_userPassword}"
    User Inputs String "${t_userPassword}" in "${FBLOGIN_PASSWORD_FIELD}" Field

User Home Page Should Not Be Displayed
    Assert That Image Should Not Exist    ${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Assert That Image Should Not Exist    ${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}
    Assert That Image Should Not Exist    ${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Is In Desktop App Login Page
    Switch Application Focus    ${FREELANCER_DESKTOPAPP_NAME}
    Wait For Image To Appear    ${DESKTOPAPP_LOGIN_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Assert That Image Should Exist    ${DESKTOPAPP_LOGIN_PAGE}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Confirms Logout
    User Clicks "${USERHOMEPAGE_LOGOUTCONFIRMATION_BUTTON}"

User Closes The Desktop App
    User Clicks "${DESKTOPAPP_CLOSE_BUTTON}"

The "${tc_DESKTOPAPP_PROMPT}" Alert Should Be Displayed
    Run Keyword If    '${tc_DESKTOPAPP_PROMPT}' == 'Invalid username or password.'
    ...    Wait And Assert That "${DESKTOPAPP_LOGIN_INVALIDCREDENTIALS_ALERT}" Is Visible
