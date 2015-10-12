*** Settings ***
Documentation     This resource contains all the variables used for login and facebook login in the Freelancer Desktop App.

*** Variables ***
${COMMON_FOLDER}    Common
${COMMON_LOGINPAGE_FOLDER}    ${COMMON_FOLDER}/LoginPage
${COMMON_FBLOGINPAGE_FOLDER}    ${COMMON_FOLDER}/FBLoginPage
${COMMON_HOMEPAGE_FOLDER}    ${COMMON_FOLDER}/UserHomePage
${COMMON_UPDATECHEKER_FOLDER}    ${COMMON_FOLDER}/UpdateChecker
#************************ Desktop App Login Page Elements ************************
${DESKTOPAPP_LOGIN_PAGE}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_DEFAULT_LOGINPAGE.png
${DESKTOPAPP_CLOSE_BUTTON}    ${COMMON_LOGINPAGE_FOLDER}/WINDOWS7_LOGIN_CLOSE_BUTTON.png
${DESKTOPAPP_USERNAME_FIELD}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_USERNAME_FIELD.png
${DESKTOPAPP_PASSWORD_FIELD}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_PASSWORD_FIELD.png
${DESKTOPAPP_LOGIN_BUTTON}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_LOGIN_BUTTON.png
${DESKTOPAPP_FBLOGIN_BUTTON}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_FBLOGIN_BUTTON.png
${DESKTOPAPP_LOGIN_INVALIDCREDENTIALS_ALERT}    ${COMMON_LOGINPAGE_FOLDER}/LOGIN_INVALIDCREDENTIALS_ALERT.png
${DESKTOPAPP_LOGIN_PROBLEMSSIGNINGIN_LINK}    ${COMMON_FBLOGINPAGE_FOLDER}/LOGIN_PROBLEMSSIGNINGIN_LINK.png
#************************ Desktop App FAcebook Login Page Elements ************************
${FBLOGIN_LOGIN_BUTTON}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_LOGIN_BUTTON.png
${FBLOGIN_USERNAME_FIELD}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_EMAILORPHONE_FIELD.png
${FBLOGIN_PASSWORD_FIELD}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_PASSWORD_FIELD.png
${FBLOGIN_LOGIN_DEFAULTPAGE}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN__LOGIN_DEFAULTPAGE.png
${FBLOGIN_KEEPMELOGGEDINCHECKED_CHECKBOX}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_KEEPMELOGGEDINCHECKED_CHECKBOX.png
${FBLOGIN_KEEPMELOGGEDINUNCHECKED_CHECKBOX}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_KEEPMELOGGEDINUNCHECKED_CHECKBOX.png
${FBLOGIN_CANCEL_BUTTON}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_CANCEL_BUTTON.png
${FBLOGIN_INCORRECTEMAIL_ALERT}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_INCORRECTEMAIL_ALERT.png
${FBLOGIN_FORGOTYOURPASSWORD_LINK}    ${COMMON_FBLOGINPAGE_FOLDER}/FBLOGIN_FORGOTYOURPASSWORD_LINK.png
#************************ Desktop App User Home Page Elements ************************
${USERHOMEPAGE_MYWORK_BUTTON}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_BUTTON_MYWORK.png
${USERHOMEPAGE_BROWSEPROJECTS_BUTTON}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_BUTTON_BROWSEPROJECTS.png
${USERHOMEPAGE_ZEROCURRENTWORK_PAGE}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_DEFAULT_ZEROCURRENTWORK.png
${USERHOMEPAGE_EXPANDCONTEXTMENU_BUTTON}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_BUTTON_EXPANDCONTEXTMENU.png
${USERHOMEPAGE_LOGOUT_CONTEXTMENU}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_CONTEXTMENU_LOGOUT.png
${USERHOMEPAGE_LOGOUTCONFIRMATION_BUTTON}    ${COMMON_HOMEPAGE_FOLDER}/USERHOMEPAGE_BUTTON_YESIMSURE.png
#************************ Update Cheher Elements ************************
${UPDATECHECKER_BACKGROUND}    ${COMMON_UPDATECHEKER_FOLDER}/UPDATECHECKER_BACKGROUND.png
${UPDATECHECKER_STATUS}    ${COMMON_UPDATECHEKER_FOLDER}/UPDATECHECKER_STATUS.png
