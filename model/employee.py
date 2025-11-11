class Employee:
    def __init__(self,id,first_name, last_name,role,username,password,salary,phone_number):
     self.id = id
     self.first_name=first_name
     self.last_name=last_name
     self.role=role
     self.username=username
     self.password=password
     self.salary=salary
     self.phone_number=phone_number
    def validate(self):
        pass

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id,self.first_name,self.last_name,self.role,self.username,self.password,self.salary,self.phone_number))

    def full_name(self):
        return f"{self.first_name} {self.last_name}"





