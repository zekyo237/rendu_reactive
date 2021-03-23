from flask_bcrypt import check_password_hash, generate_password_hash


class User(object):
    def __init__(self, username, password):
        self.id=10
        self.username = username
        self.password = password

    def hash_password(self):
         self.password = generate_password_hash(self.password).decode('utf8')


    def check_password(self,password):
        return check_password_hash(self.password,password)

    def  creation_id(self,id):
        self.id=id
    
    def is_autenticated(self):
        return True

   

    

    
        