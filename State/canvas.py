from tools import Tool

class Canvas:

    __current_tool = None

    def create_tool(self, active_tool):
        self.__current_tool = Tool(active_tool)
    

    def mouse_up(self):
        self.__current_tool.call_mouse_up()
    
    def mouse_down(self):
        self.__current_tool.call_mouse_down()