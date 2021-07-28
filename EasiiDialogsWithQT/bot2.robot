** Settings ***
Resource    bot.robot
Metadata         --name    Dialogs


*** Test Cases ***
test Function
    Log      a
    init
    Label    name:        achraf
    Entry       input1     17      12   12   10  
    Entry       input2      
    Entry with regex Expression        input3      ^start
    show        Main Interface