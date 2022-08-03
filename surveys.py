class AnonymousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses =[]
    
    def show_question(self):
        print(self.question)
    
    def store_response(self,new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print('All Responses to this question')
        for response in self.responses:
            print(f"- {response}")



class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name= first_name
        self.last_name = last_name
        self.salary = salary
        self.salary_raise = 6000
    
    def give_raise(self,new_salary_raise):
        if(new_salary_raise):
            total = int(self.salary) + new_salary_raise
            return total
        else:
            total = int(self.salary) + self.salary_raise
            return total