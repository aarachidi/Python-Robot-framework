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
    ${Max Values}=  UserMesures.getMaxValues
    ${Min Values}=  UserMesures.getMinValues
    ${size}=    get Length  ${Invalid Result}
    Run Keyword if      ${size}!= 0     print Erreur    ${Invalid Result}   ${Max Values}       ${Min Values}

print Erreur
    [Arguments]    ${Element Names}     ${Max Values}   ${Min Values}
    FOR    ${Name}     IN    @{Element Names}
    FOR    ${Unit}      IN      @{Element Names}[${Name}]
    ${size}=    get Length      ${Element Names}[${Name}][${Unit}]
    Run Keyword if      ${size}!= 0     Compare to min and max    ${Name}     ${Unit}     ${Element Names}[${Name}][${Unit}]          ${Min Values}[${Name}][${Unit}]         ${Max Values}[${Name}][${Unit}]
    Run Keyword if      ${size}== 0     Empty Input     ${Name}     ${Unit}     
    END
    END

Compare to min and max
    [Arguments]     ${Name}     ${unit}    ${value}     ${min}      ${max}
    Run Keyword And Continue On Failure     Should Be True      ${min}<=${value}<=${max}    *HTML* Value of ${Name} in ${unit} should be between ${min} and ${max}

Empty Input
    [Arguments]     ${Name}     ${unit}
    Run Keyword And Continue On Failure     Should Be True     5>6      *HTML* You left the ${Unit} of ${Name} empty

*** Test Cases ***
Do Test
    UserMes