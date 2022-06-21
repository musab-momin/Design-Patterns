class Tool:

    def __init__(self, active_tool):
        self.active_tool = active_tool

    def call_mouse_up(self):
        self.active_tool.mouse_up()

    def call_mouse_down(self):
        self.active_tool.mouse_down()