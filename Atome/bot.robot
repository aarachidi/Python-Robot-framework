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
    ${size}=    get Length  ${Invalid Result}
    Run Keyword if      ${size}!= 0     test Keyword        4.5         5   5

printErreur
    [Arguments]    ${Element Names}
    FOR    ${Name}     IN    @{Element Names}
    FOR    ${Unit}      IN      @{Element Names}[${Name}]
    Run Keyword And Continue On Failure     Should Be Equal      ${Element Names}[${Name}][${Unit}]        achraf
    END
    END

test Keyword
    [Arguments]    ${value}     ${min}      ${max}
    Run Keyword And Continue On Failure     Should Be True      ${min}<${value}<${max}

*** Test Cases ***
Do Test
    UserMes