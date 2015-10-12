*** Settings ***
Documentation     This resource contains all the keywords used for installation and uninstallation of Freelancer Desktop App.
Library           OperatingSystem
Resource          ../CommonResources/sikuli_keywords.robot
Resource          ../CommonResources/desktopapp_global_helper.robot
Resource          ../Variables/dektopapp_install_uninstall_constants.robot
Resource          ../Variables/desktopapp_login_constants.robot

*** Keywords ***
# =============================================== #
#                       Given                     #
# =============================================== #

User Goes To "${tc_URL}" Page Via "${tc_WEB_BROWSER}" Browser
    Run Keyword If    '${tc_WEB_BROWSER}' == 'Firefox'
    ...    Visit "${tc_URL}" Via Firefox

User Logs In With Valid Username "${tc_USER_NAME}" And Password "${tc_USER_PASSWORD}"
    User Clicks "${WEB_START_TRACKING_BUTTON}"
    User Inputs String "${tc_USER_NAME}" in "${WEB_LOGIN_USERNAME_FIELD}" Field
    User Inputs String "${tc_USER_PASSWORD}" in "${WEB_LOGIN_PASSWORD_FIELD}" Field
    User Clicks "${WEB_LOGIN_BUTTON}"
    User Clicks "${WEB_START_TRACKING_BUTTON}"

User Selects "${tc_OS}" Operating System
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Select Windows Desktop App Installer From Options

User Opens the "${tc_WEB_BROWSER}" Web Browser
    Run Keyword If    '${tc_WEB_BROWSER}' == 'Firefox'
    ...    Initialize Firefox Web Browser

User Clears The "${tc_WEB_BROWSER}" Browser Cache
    Run Keyword If    '${tc_WEB_BROWSER}' == 'Firefox'
    ...    Clear Firefox Browser Cache

The "${tc_OS}" Desktop App Installer Exists
    The "${tc_OS}" Desktop App Installer Should Be Successfully Downloaded


The "${tc_OS}" Desktop App Is Installed
    The "${tc_OS}" Desktop App Installer Should Be Successfully Installed


# =============================================== #
#                       When                      #
# =============================================== #

User Downloads The "${tc_OS}" Desktop App Installer
    User Clicks "${WEB_DESKTOPAPPDOWNLOAD_BUTTON}"
    User Clicks "${WEB_DESKTOPAPPSAVE_BUTTON}"
    Wait In Seconds    2
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Download The Windows Desktop App Installer

User Closes "${tc_WEB_BROWSER}" Browser
    Run Keyword If    '${tc_WEB_BROWSER}' == 'Firefox'
    ...    Close Firefox Browser

User Runs the "${tc_OS}" Desktop App Installer
    Run Keyword If    '${tc_OS}' == 'WIN7' or '${tc_OS}' == 'WIN8'
    ...    Run "${tc_OS}" Setup

User Uninstalls The "${tc_OS}" Desktop App
    Run Keyword If    '${tc_OS}' == 'WIN7' or '${tc_OS}' == 'WIN8'
    ...    Run "${tc_OS}" Uninstallation

User Deletes The "${tc_OS}" Desktop App Installer
    Run Keyword If    '${tc_OS}' == 'WIN7' or '${tc_OS}' == 'WIN8'
    ...    Delete The Windows Desktop App Installer

# =============================================== #
#                       Then                      #
# =============================================== #

The "${tc_OS}" Desktop App Installer Should Be Successfully Downloaded
    The "${tc_OS}" Desktop App Installer Should Exist
    The File Size of Downloaded "${tc_OS}" Desktop App Installer Should be Correct

The File Size of Downloaded "${tc_OS}" Desktop App Installer Should be Correct
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Should Be Equal As Strings    ${tc_WINDOWS_DESKTOP_APP_FILE_SIZE}    ${WINDOWS_DESKTOPAPP_FILESIZE}

The "${tc_OS}" Desktop App Installer Should Exist
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Installer Should Exist In Windows Download Directory

The "${tc_OS}" Desktop App Installer Should Be Successfully Installed
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Verify If Freelancer Desktop App Is Installed in Windows

The "${tc_OS}" Desktop App Installer Should Be Successfully Uninstalled
    Run Keyword If    '${tc_OS}' == 'Windows'
    ...    Verify If Freelancer Desktop App Is Not Installed in Windows

# =============================================== #
#                Internal Keywords                #
# =============================================== #

Clear Firefox Browser Cache
    Press ALT + "S"
    Wait In Seconds    1
    Press "C" key
    Wait In Seconds    1
    Press "Enter" key

Close Firefox Browser
    Wait In Seconds    1
    Set Application Focus    Freelancer | Online Jobs | Freelance Employment | Outsourcing Services | Programmers | Web Design | Freelancers
    Wait In Seconds    1
    Press CTRL + "w"

Run "${p_OS}" Setup
    Start Process    ${tc_${p_OS}_LOCAL_DOWNLOAD_DIRECTORY}/${${p_OS}_DESKTOPAPP_INSTALLER}
    Set Application Focus    Setup - Freelancer Desktop App
    Repeat Keyword    4 times    User Clicks "${${p_OS}_SETUP_NEXT_BUTTON}"
    User Clicks "${${p_OS}_SETUP_INSTALL_BUTTON}"
    Wait For Image To Appear    ${${p_OS}_SETUP_COMPLETING_INSTALLATION_DIALOG}
    ...    ${IMAGE_RECOGNITION_SENSITIVITY}    60
    User Clicks "${${p_OS}_SETUP_LAUNCH_DESKTOPAPP_CHECKBOX}"
    User Clicks "${${p_OS}_SETUP_FINISH_BUTTON}"

Run "${t_OS}" Uninstallation
    Start Process    ${WINDOWS_DESKTOPAPP_UNINSTALL_FILE}
    User Clicks "${${t_OS}_UNINSTALL_YES_BUTTON}"
    User Clicks "${${t_OS}_UNINSTALL_OK_BUTTON}"
    Remove Directory    C:/Program Files (x86)/Freelancer.com

Select Windows Desktop App Installer From Options
    ${t_WindowsIconIsActive}=    Run Keyword And Return Status
    ...    Assert That Image Should Exist    ${WINDOWS_DESKTOPAPPACTIVE_INSTALLER_LINK}
    ...    ${IMAGE_RECOGNITION_SENSITIVITY}
    Run Keyword If    '${t_WindowsIconIsActive}'
    ...    User Clicks "${WINDOWS_DESKTOPAPPACTIVE_INSTALLER_LINK}"
    ...    ELSE    User Clicks "${WINDOWS_DESKTOPAPPINACTIVE_INSTALLER_LINK}"

Verify If Freelancer Desktop App Is Installed in Windows
    Directory Should Not Be Empty    ${WINDOWS_APPLICATION_INSTALLATION_DIRECTORY}
    File Should Exist    ${WINDOWS_APPLICATION_INSTALLATION_DIRECTORY}/${WINDOWS_DESKTOPAPP_EXECUTABLE}

Verify If Freelancer Desktop App Is Not Installed in Windows
    Directory Should Not Exist    ${WINDOWS_DESKTOPAPP_UNINSTALL_FILE}

Initialize Firefox Web Browser
    Open Application    ${WINDOWS_FIREFOX_BROWSER}
    Wait In Seconds    2
    Set Application Focus    "Mozilla Firefox"
    Wait For Image To Appear    ${FIREFOX_URL_FIELD}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Wait In Seconds    2
    Clear Firefox Browser Cache

Installer Should Exist In Windows Download Directory
    File Should Exist    ${tc_WINDOWS_LOCAL_DOWNLOAD_DIRECTORY}/${WINDOWS_DESKTOPAPP_INSTALLER}

Get File Size Of Windows Desktop App Installer
    ${t_windowsDesktopAppInstallerFileSize}=
    ...    Get File Size    ${tc_WINDOWS_LOCAL_DOWNLOAD_DIRECTORY}/${WINDOWS_DESKTOPAPP_INSTALLER}
    ${t_windowsDesktopAppInstallerFileSize}=    Convert To String    ${t_windowsDesktopAppInstallerFileSize}
    Set Test Variable    ${tc_WINDOWS_DESKTOP_APP_FILE_SIZE}    ${t_windowsDesktopAppInstallerFileSize}

Delete The Windows Desktop App Installer
    Remove File    ${tc_WINDOWS_LOCAL_DOWNLOAD_DIRECTORY}/${WINDOWS_DESKTOPAPP_INSTALLER}

Download The Windows Desktop App Installer
    Wait Until Removed    ${tc_WINDOWS_LOCAL_DOWNLOAD_DIRECTORY}/${WINDOWS_DESKTOPAPP_PART_FILE}

Visit "${tc_URL}" Via Firefox
    User Inputs String "${tc_URL}" in "${FIREFOX_URL_FIELD}" Field
    Press "Enter" Key

Get The Windows Local Download Directory
    ${t_userName}=    Run    echo %username%
    ${t_windowsdownloaddirectory}=    Set Variable    C:/Users/${t_userName.strip()}/Downloads
    Set Test Variable    ${tc_WINDOWS_LOCAL_DOWNLOAD_DIRECTORY}    ${t_windowsdownloaddirectory}