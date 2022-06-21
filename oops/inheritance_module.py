class Behavior:
    def focus(self):
        print('Auto focus is added')
    
    def border(self):
        print('border is added on field')

class Button(Behavior):
    def click(self):
        print('Button is clicked')

class TextField(Behavior):
    def write(self):
        print('wrote something in text field')   