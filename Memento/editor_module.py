class Editor:
    __previouse_values = []
    __content = None

    def get_content(self):
        return self.__content

    def set_content(self, value):
        self.__content = value
        self.__previouse_values.append(self.__content)

    def undo(self):
        if len(self.__previouse_values) > 0:
            self.__previouse_values.pop(-1)
            return self.__previouse_values[len(self.__previouse_values) - 1 ] if len(self.__previouse_values) > 0 else None
        else:
            return None



