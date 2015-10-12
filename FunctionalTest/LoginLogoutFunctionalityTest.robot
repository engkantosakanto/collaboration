*** Settings ***
Documentation     This suite covers the test cases for login logout functionality test of the Desktop App
Test Setup        Set Default Image Library Path    ${FREELANCER_DESKTOPAPP_IMAGELIBRARY}
Test Teardown     Close Application    Freelancer Desktop App
Default Tags      LoginLogoutFunctionalityTest    Functional
Library           OperatingSystem
Resource          ../Resources/CommonResources/desktopapp_global_helper.robot
Resource          ../Resources/PageResources/desktopapp_login_page.robot
Resource          ../Resources/PageResources/desktop_install_uninstall_dialog.robot
Resource          ../Resources/CommonResources/sikuli_keywords.robot
Resource          ../Resources/CommonResources/desktopapp_global_constants.robot

*** Variables ***
${freelancerUsername}    botFLNFTDTLogin
${freelancerInvalidUsername}    invalidUserName
${freelancerInvalidPassword}    invalidPassword
#${freelancerFBUsername}    testuser+botFLNFTDTLogin@freelancer.com

*** Test Cases ***

User Should Be Able to View the Update Checker
    Given The "Windows" Desktop App Is Installed
    When User Runs the "Windows" Desktop App
    Then User Should Be Able To View The Update Checker
    [Teardown]    Close Application    Freelancer Desktop App

User Should Successfully Login To The Windows Desktop App
    Given The "Windows" Desktop App Is Installed
    And User Runs the "Windows" Desktop App
    And User Is In Desktop App Login Page
    When User Logs In With "${freelancerUsername}" And "${FREELANCER_TEST_PASSWORD}"
    Then User Should Be Logged In Successfully

User Should Successfully Logout From The Windows Desktop App
    Given User Home Page Is Displayed
    When User Logs Out From The Desktop App
    Then User Should Be Successfully Logged Out
    [Teardown]    Close Application    Freelancer Desktop App

User Should Successfully Login To The Windows Desktop App Via Facebook Login
    Given The "Windows" Desktop App Is Installed
    And User Runs the "Windows" Desktop App
    And User Is In Desktop App Login Page
    When User Logs In With "${FREELANCER_FBTEST_EMAIL}" And "${FREELANCER_FBTEST_PASSWORD}" Via Facebook Login
    Then User Should Be Logged In Successfully
    [Teardown]    Close Application    Freelancer Desktop App

User With Invalid Username Should Not Be Able To Login
    Given The "Windows" Desktop App Is Installed
    And User Runs the "Windows" Desktop App
    And User Is In Desktop App Login Page
    When User Logs In With "${freelancerInvalidUsername}" And "${FREELANCER_TEST_PASSWORD}"
    Then Desktop App "Invalid Credentials" Alert Should Be Launched
    [Teardown]    Close Application    Freelancer Desktop App

User With Invalid Password Should Not Be Able To Login
    Given The "Windows" Desktop App Is Installed
    And User Runs the "Windows" Desktop App
    And User Is In Desktop App Login Page
    When User Logs In With "${freelancerUsername}" And "${freelancerInvalidPassword}"
    Then Desktop App "Invalid Credentials" Alert Should Be Launched
    [Teardown]    Close Application    Freelancer Desktop App

User With Blank Username Or Password Should Not Be Able To Login
    Given The "Windows" Desktop App Is Installed
    And User Runs the "Windows" Desktop App
    And User Is In Desktop App Login Page
    When User Logs In With "${EMPTY}" And "${EMPTY}"
    Then Desktop App "Required Field Is Empty" Alert Should Be Launched
    [Teardown]    Close Application    Freelancer Desktop App