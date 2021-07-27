** Settings ***
Documentation     How to use a custom Python Dialogs.
Library     QtDialogs.py


*** Test Cases ***
test Function
    pause_execution
test3
    ${a}=   get_value_from_user     put a val   default value
test4
    ${user} =	Get Selections From User 	Select user	  user1	  user2	  admin
test5
    ${a}=   get_value_from_user     put a val   default value