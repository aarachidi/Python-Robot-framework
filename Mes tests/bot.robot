** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     UserMeasure.py         WITH NAME    UserMesures
*** Variables ***
${numbers}    

*** Keywords ***
UserMes
    UserMesures.show
    ${valid Result}=  UserMesures.getValidResult
    ${Invalid Result}=  UserMesures.getInvalidResult
    Run Keyword And Continue On Failure    Should Be Empty     ${Invalid Result}
    FOR    ${key}     IN    @{valid Result}
    Log     The current key is: ${key}
    END

*** Test Cases ***
Do Test
    UserMes