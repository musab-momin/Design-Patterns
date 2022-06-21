# from editor_module import Editor
from orignator import Editor
from memento import EditorState
from caretaker import History


#My approach 
# writer = Editor()

# writer.set_content('Musab Momin')
# writer.set_content('Web Developer')
# writer.set_content('Football is love')
# writer.set_content('I am funny')
# print(writer.get_content())

# print(writer.undo())
# print(writer.undo())
# print(writer.undo())
# print(writer.undo())
# print(writer.undo())


#Solving undo problem with Memento 
editor = Editor()
history = History()

editor.set_content('Musab Momin')
history.push(editor.create_state())

editor.set_content('Web Developer')
history.push(editor.create_state())

editor.set_content('Football is love')

editor.restore(history.pop())
print(editor.get_content())


editor.restore(history.pop())
print(editor.get_content())
