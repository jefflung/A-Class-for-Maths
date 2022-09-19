class MathEngine:
    num = 0
    input_num = 0
    def __init__(self, num, input_num):
        self.num = num
        self.input_num = input_num
    def add(self):
       return self.num + self.input_num
    def sub(self):
       return self.num - self.input_num
    def mult(self):
       return self.num * self.input_num
    def div(self):
       return self.num / self.input_num

continue_program = ""
while not (continue_program == "exit"):
    input_num = int(input("Please give me a number: "))
    calculate = MathEngine(5,input_num)
    
    action = input("Please enter 1(to add) or 2(to subtract) or 3(to multiply) or 4(to divide):")

    if action == "1":
        print(calculate.add())
    elif action == "2":
        print(calculate.sub())
    elif action == "3":
        print(calculate.mult())
    elif action == "4":
        print(calculate.div())

    continue_program = input("Type 'exit' to quit ")
