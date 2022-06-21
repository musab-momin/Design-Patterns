class EmailSender:

    def send_email(self):
        self.__connect()
        self.__authenticate()
        self.__action()
        self.__close_conection()

    def __connect(self):
        print('Connecting to email server...')
    
    def __authenticate(self):
        print('Authenticating user')
    
    def __action(self):
        print('Sending email')
    
    def __close_conection(self):
        print('closing connection')