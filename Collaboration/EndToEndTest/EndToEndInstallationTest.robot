*** Settings ***
Documentation     This suite is for the end to end installation of the Desktop App
Library           OperatingSystem
Resource          ../Resources/CommonResources/desktopapp_global_helper.robot
Resource          ../Resources/PageResources/desktopapp_login_page.robot
Resource          ../Resources/PageResources/desktop_install_uninstall_dialog.robot
Resource          ../Resources/CommonResources/sikuli_keywords.robot

*** Test Cases ***
Freelancer Desktop App Should Be Successfully Downloaded In Windows
    [Setup]    User Opens the "Firefox" Web Browser
    Given User Goes To "${WEB_DESKTOPAPP_DOWNLOAD_URL}" Page Via "Firefox" Browser
    And User Logs In With Valid Username "${FREELANCER_TEST_EMAIL}" And Password "${FREELANCER_TEST_PASSWORD}"
    And User Selects "Windows" Operating System
    When User Downloads the "Windows" Desktop App Installer
    Then The "Windows" Desktop App Installer Should Be Successfully Downloaded
    [Teardown]    Run Keywords    User Clears The "Firefox" Browser Cache    User Closes "Firefox" Browser

Freelancer Desktop App Should Be Successfully Installed In Windows
    Given The "Windows" Desktop App Installer Exists
    When User Runs the "WIN7" Desktop App Installer
    Then The "Windows" Desktop App Installer Should Be Successfully Installed
    [Teardown]    Stop All Processes

User Should Successfully Login To The Windows Desktop App
    Given The "Windows" Desktop App Is Installed
    When User Runs the "Windows" Desktop App
    Then User Should Be Able To View The Update Checker
    When User Is In Desktop App Login Page
    And User Logs In With "${FREELANCER_TEST_EMAIL}" And "${FREELANCER_TEST_PASSWORD}"
    Then User Should Be Logged In Successfully
    When User Logs Out From The Desktop App
    Then User Should Be Successfully Logged Out
    [Teardown]    Close Application    Freelancer Desktop App

User Should Successfully Login To The Windows Desktop App Via Facebook Login
    Given The "Windows" Desktop App Is Installed
    When User Runs the "Windows" Desktop App
    Then User Should Be Able To View The Update Checker
    When User Is In Desktop App Login Page
    And User Logs In With "${FREELANCER_FBTEST_EMAIL}" And "${FREELANCER_FBTEST_PASSWORD}" Via Facebook Login
    Then User Should Be Logged In Successfully
    When User Logs Out From The Desktop App
    User Should Be Successfully Logged Out
    [Teardown]    Close Application    Freelancer Desktop App

Freelancer Desktop App Should Be Successfully Uninstalled In Windows
    Given The "Windows" Desktop App Is Installed
    User Uninstalls The "WIN7" Desktop App
    The "Windows" Desktop App Installer Should Be Successfully Uninstalled
    [Teardown]    Run Keywords    User Deletes The "Windows" Desktop App Installer    Stop All Processes
