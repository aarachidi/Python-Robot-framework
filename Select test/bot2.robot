** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     Dialogs
Library     OperatingSystem
Metadata         --name    Dialogs
    

*** Test Cases ***
test2 Function
    ${a}=    get_value_from_user     enter an input
    Pause Execution        Test is paused for now