*** Settings ***
Documentation     This suite covers the test cases for login logout functionality test of the Desktop App
Test Setup        Set Default Image Library Path    ${FREELANCER_DESKTOPAPP_IMAGELIBRARY}
Test Teardown     Close Application    Freelancer Desktop App
Default Tags      LoginLogoutFunctionalityTest
Library           OperatingSystem
Resource          ../Resources/CommonResources/desktopapp_global_helper.robot
Resource          ../Resources/PageResources/desktopapp_login_page.robot
Resource          ../Resources/PageResources/desktop_install_uninstall_dialog.robot
Resource          ../Resources/CommonResources/sikuli_keywords.robot
Resource          ../Resources/CommonResources/desktopapp_global_constants.robot

*** Test Cases ***
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
