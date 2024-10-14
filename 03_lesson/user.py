class User:
    def __init__(self, first_name, last_name):
        self.user_fn = first_name
        self.user_ln = last_name
    def printFirstname(self):
        print(self.user_fn)
    def printLastname(self):
        print(self.user_ln)
    def printFullname(self):
        print(self.user_fn, self.user_ln)