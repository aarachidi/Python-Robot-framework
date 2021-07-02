import npyscreen


dict = []
result = {}
class MyTestApp(npyscreen.NPSAppManaged):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def show(self):
        self.run()

    def createLabel(self, text="", value=""):
        temp = {}
        temp['type'] = "FixedText"
        temp['text'] = text
        temp['value'] = value
        dict.append(temp)

    def createEntry(self, name=""):
        temp = {}
        temp['type'] = "TitleText"
        temp['name'] = name
        dict.append(temp)

    def getResult(self):
        results = {}
        keys = result.keys()
        for key in keys:
            results[key] = result[key].value
        return results

    def onStart(self):
        self.form = MainForm()
        for element in dict:
            if element['type'] == "FixedText":
                self.form.add(npyscreen.TitleText, name= element['text'],  value= element['value'], editable=False)
            elif element['type'] == "TitleText":
                input = self.form.add(npyscreen.TitleText, name = element['name'])
                result[element['name']] = input
        self.registerForm("MAIN", self.form)


class MainForm(npyscreen.Form):   
    def afterEditing(self):
        self.parentApp.setNextForm(None)