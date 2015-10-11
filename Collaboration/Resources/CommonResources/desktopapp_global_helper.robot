*** Settings ***
Library           OperatingSystem
Resource          sikuli_keywords.robot
Resource          desktopapp_global_constants.robot

*** Keywords ***
User Clicks "${t_UI}"
    Wait For Image To Appear    ${t_UI}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Click Application Image    ${t_UI}    ${IMAGE_RECOGNITION_SENSITIVITY}

User Inputs String "${t_string}" in "${t_field}" Field
    Wait For Image To Appear    ${t_field}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Input Strings In Image XY Coordinates    ${t_field}
    ...    ${IMAGE_RECOGNITION_SENSITIVITY}    0    0    ${t_string}

Maximize Windows
    Press Windows Key + "UP"

Close "${t_browser}" Browser
    Run Keyword If    '${t_browser}' == 'Mozilla Firefox'    Press CTRL + "W"
    ...    ELSE    Close Application    ${t_browser}

Get The Windows Local Download Directory
    ${t_userName}=    Run    echo %username%
    ${t_windows_download_directory}=    Set Variable    C:/Users/${t_userName.strip()}/Downloads
    [Return]    ${t_windows_download_directory}

Wait And Assert That "${t_image}" Is Visible
    Wait For Image To Appear    ${t_image}    ${IMAGE_RECOGNITION_SENSITIVITY}    ${TIMEOUT}
    Assert That Image Should Exist    ${t_image}    ${IMAGE_RECOGNITION_SENSITIVITY}
