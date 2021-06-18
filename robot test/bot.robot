** Settings ***
Documentation     How to use a custom Python Dialogs.
Library           script.py

*** Variables ***
@{numbers}    1    2    3
&{function1}       type=createEntry    name=variable1     x=150    y=280      max=10   min=2
&{function5}       type=createEntry    name=variable2     x=150    y=300      max=8   min=4
&{function2}       type=createButton    name=Bt     text=validate     x=400    y=330
&{function3}       type=createImage     name=Img        x=300    y=10   path=easii-ic.png
&{function4}       type=createLabel     text=Inputs    x=200    y=250
*** Keywords ***
Custome Dialog
    [Documentation]     This keyword make a custom dialog depending on 
    ...                 the input.
    ...           
    ...                 The variables passed to the keyword must be dictionaries.\n
    ...                 There is three types of widgets :\n
    ...                 -----createEntry  for user's input\n
    ...                 Example :\n
    ...                 &{example1}       type=createEntry(required)    name=variable1(required)     x=40    y=30      max=10   min=2\n
    ...                 Custome Dialog   ${example1}\n
    ...                 -----createImage  to insert images\n
    ...                 Example :\n
    ...                 &{example2}       type=createImage(required)     name=Img(required)        x=150    y=150   path=example.png(required)\n
    ...                 Custome Dialog   ${example2}
    ...                 -----createButton  to insert button\n
    ...                 Example :\n
    ...                 &{example3}       type=createButton(required)     name=Bt(required)        x=150    y=150   text=validate(required)\n
    ...                 Custome Dialog   ${example3}
    ...                 -----createLabel  to insert Text\n
    ...                 Example :\n
    ...                 &{example4}       type=createLabel(required)     text=Text here(required)        x=150    y=150\n
    ...                 Custome Dialog   ${example4}
    [Arguments]    @{expected}
    ${a}=   test    ${expected}


*** Test Cases ***
test Function 
    Custome Dialog   ${function1}   ${function2}    ${function3}       ${function4}     ${function5}