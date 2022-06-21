

class History:
    __states = []

    def push(self, state):
        self.__states.append(state)

    def pop(self):
        last_index = len(self.__states) - 1
        if len(self.__states ) > 0:
            last_sate = self.__states[last_index]
            self.__states.pop(last_index)
            return last_sate
        else:
            return None