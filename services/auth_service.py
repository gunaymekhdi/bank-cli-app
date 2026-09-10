from models.user import User
class AuthService:

    def __init__(self):
        self.users= []
        self.current_user= None


    def register(self, user_id, full_name, email, fin_code):
        for user in self.users:
            if user.fin_code == fin_code or user.user_id == user_id:
                raise ValueError ("Bu FIN kod və ya User ID ilə istifadəçi artıq mövcuddur!")
            
        new_user=User(
                user_id=user_id,
                full_name=full_name,
                email=email,
                fin_code=fin_code
                )

        self.users.append(new_user)
        return new_user


    def login(self, fin_code):
        for user in self.users:
            if user.fin_code == fin_code:
                self.current_user = user
                return self.current_user
            
        raise ValueError ("İstifadəçi tapılmadı!")


    def logout(self):
        self.current_user = None


    def get_current_user(self):
        return self.current_user
    
    
            
       

         