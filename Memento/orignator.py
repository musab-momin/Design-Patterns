from memento import EditorState


class Editor:
    __content = None


    def create_state(self):
        return EditorState(self.__content)

    
    def restore(self, state):
        self.__content = state.get_content()


    def get_content(self):
        return self.__content
    

    def set_content(self, value):
        self.__content = value