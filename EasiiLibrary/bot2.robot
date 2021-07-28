** Settings **
Resource    bot.robot
Metadata         --name    Dialogs


*** Test Cases ***
test Function
    Log      a
    init
    Table from Data  data.json
    show        Main Interface
    Result of Table