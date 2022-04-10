#연산자의 우선순의를 판별하기 위한 클래스
class Operator:
    #생성자
    def __init__(self, op:str):
        self.op = op #op = Operate(연산자)
        if op not in ("+", "-", "*", "/"):
            raise ValueError('사용가능한 연산자가 아닙니다.')

    #매직 메소드(Magic methords): 기본 연산자 밑 내장 함수의 기능에 대하여
    #오버라이딩을 가능하게 해주는 메소드
    #other 와 같음 (equal, ==)

    def __eq__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)}''타입과의 비교는 지원하지 않습니다.')

        if self.op in ('+', '-') and other.op in ('+', '-'):
            return True
        if self.op in ('*', '/') and other.op in ('*', '/'):
            return True
        else:
            return False
#other보다 작음 (less than, <)
    def __lt__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)}''타입과의 비교는 지원하지 않습니다.')

        return self.op in ('+', '-') and other.op in ('*', '/')



    # other보다 작거나 같음 (less than ~ or equal, <=)
    def __le__(self,other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)}''타입과의 비교는 지원하지 않습니다.')

        return  self.__eq__(other) or self.__lt__(other)

    # other 보다 큼(greator than, >)
    def __gt__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)}''타입과의 비교는 지원하지 않습니다.')
        return not self.__le__(other)

    #other 보다 크거나 같음 (greator than ~ or equal, >=)
    def __ge__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)}''타입과의 비교는 지원하지 않습니다.')
        return not self.__lt__(other)
    #클래스의 정보를 표현함

    def __repr__(self):
        return f'Operate({self.op})'

    def operation(self, X, Y):
        if self.op == '+':
            return X + Y
        elif self.op == '-':
            return X - Y
        elif self.op == '*':
            return X * Y
        elif self.op == '/':
            return X / Y

class InCalc:
    def __init__(self):
        self.infix_expr = []

    # 문자열 수식을 리스트로 변환하여 infix_expr에 저장하는 함수
    def set_expression(self, expr: str):
        self.infix_expr.clear()
        operand = ''#피연산자

        for x in expr:
            if x.isdigit():#현재 수식이 숫자인 경우
                operand += x
            else:#현재 수식이 연산자인 경우
                if len(operand) > 0:
                    self.infix_expr.append(int(operand))
                    operand = ''
                self.infix_expr.append(Operator(x))

        if len(operand) > 0:
            self.infix_expr.append(int(operand))
        print('수식을 리스트로:', self.infix_expr)

    # 1.숫자는 그대로 출력 (prefix_expr에 붙인다는 뜻)한다.
    # 2.연산자는 스택에 넣는다.
    # 2-1. 스택이 비어있는 경우는 무조건 넣는다.
    # 2-2. 스택이 비어있지 않은 경우는 넣으려는 연사자와 스택에 있는 연산자를 비교아여
    #      스택에 있는 연산자의 우선수의가 넣으려는 연산자의 우선순의보다 작을떄가지
    #      스택에서 Pop하면서 출력하고 넣으려는 연산자를 스택에 넣어준다.
    # 3.마지막으로 남았있는 스택에 모든 연산자를 출력한다.
    def infix_to_prefix(self):
        stack = []
        prefix_expr = []

        for x in self.infix_expr:
            if type(x) == int:
                prefix_expr.append(x)
            else:
                while len(stack) > 0 and stack[-1] > x:
                    prefix_expr.append(stack.pop())
                stack.append(x)
        while len(stack) > 0:
            prefix_expr.append(stack.pop())
        print('후의 연산자 변환:',prefix_expr)
        return prefix_expr


    def evalution(self):
        stack = []
        prefix_expr = self.infix_to_prefix()
        for x in prefix_expr:
            if type(x) == int:
                stack.append(x)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(x.operation(operand1,operand2))
        if len(stack) > 1:
            raise ValueError('잘모된 수식을 계산하려고 했습니다.')

        return stack.pop()


calc = InCalc()
calc.set_expression('12+28-3*4')
print(calc.evalution())
