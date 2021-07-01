import npyscreen


dict = []
result = []
class MyTestApp(npyscreen.NPSAppManaged):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def show(self):
        self.run()

    def createLabel(self, text=""):
        temp = {}
        temp['type'] = "FixedText"
        temp['text'] = text
        dict.append(temp)

    def createSimpleInput(self, text="",name=""):
        temp = {}
        temp['type'] = "TitleText"
        temp['text'] = text
        temp['name'] = name
        dict.append(temp)

    def getResult(self):
        results = []
        for element in result:
            results.append(element.value)
        return results

    def onStart(self):
        self.form = MainForm()
        for element in dict:
            if element['type'] == "FixedText":
                self.form.add(npyscreen.FixedText, value = element['text'])
            elif element['type'] == "TitleText":
                input = self.form.add(npyscreen.TitleText, name = element['text'])
                result.append(input)
        self.registerForm("MAIN", self.form)


class MainForm(npyscreen.Form):   
    def afterEditing(self):
        self.parentApp.setNextForm(None)