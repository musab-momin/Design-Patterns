from canvas import Canvas
from selection import SelectionTool
from brush import Brush


canvas = Canvas()
selection_tool = SelectionTool()
canvas.create_tool(selection_tool)
canvas.mouse_up()
canvas.mouse_down()

print()
print('-*-*-*-*-*-*-*-*-*-*')
print()


canvas = Canvas()
brush_tool = Brush()
canvas.create_tool(brush_tool)
canvas.mouse_up()
canvas.mouse_down()

