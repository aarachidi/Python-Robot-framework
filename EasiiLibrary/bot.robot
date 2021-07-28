** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     OperatingSystem
Library     EasiiDialogs_py.py
*** Variables *** 

*** Keywords ***
init
    ${obj1} =      EasiiDialogs_py.init
    ${app} =       EasiiDialogs_py.appVal
    Set Global Variable   ${obj}    ${obj1}
    Call Method    ${obj}       setApp     ${app}

Label
    [Arguments]    @{expected}
    Call Method    ${obj}      createLabel     @{expected}

Entry
    [Arguments]    @{expected}
    Call Method    ${obj}      createEntry  @{expected}


Entry with regex Expression
    [Arguments]    @{expected}
    Call Method    ${obj}      createEntryWithRegex  @{expected}


Button
    [Arguments]    @{expected}
    Call Method    ${obj}      createButton  @{expected}

Image
    [Arguments]    @{expected}
    Call Method    ${obj}      createImage  @{expected}

Table from Data
    [Arguments]    @{expected}
    Call Method    ${obj}      createTable  @{expected}

Result of Table
    ${valid Result}=  Call Method    ${obj}      getValidResult
    ${Invalid Result}=  Call Method    ${obj}      getInvalidResult
    ${Max Values}=  Call Method    ${obj}      getMaxValues
    ${Min Values}=  Call Method    ${obj}      getMinValues
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

show
    [Arguments]      @{expected}
    Call Method    ${obj}      sh        @{expected}
    ${a}=    Call Method    ${obj}       getResult







    