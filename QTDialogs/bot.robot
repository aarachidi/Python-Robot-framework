** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     QtDialogs.py

*** Test Cases ***
test Function
    pause_execution     first test
test2
    execute manual step     second test
    ${a}=   get_value_from_user     put a val   default value
    ${user} =	Get Selections From User 	Select user	  user1	  user2	  admin
