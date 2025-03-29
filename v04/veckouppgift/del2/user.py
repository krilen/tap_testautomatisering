
class User():
    
    def __init__(self):
        self.__valid_credentials = [("john", "mypass")]


    def login(self, username, password):
        for credentials in self.__valid_credentials:
            if username == credentials[0] and password == credentials[1]:
                break

        else:
            return False

        return True


if __name__ == "__main__":
    print("Wrong file")