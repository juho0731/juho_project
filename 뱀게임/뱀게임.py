import pygame
import random
from datetime import datetime
from datetime import timedelta
from perceptron import*
# 스크린과 한 픽셀의 크기를 정의
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# 뱀게임에 사용할 색상을 정의
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
BLUE = (0, 0, 255)


# pygame 모듈 초기화
pygame.init()

# screen 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 배경을 그리는 함수 정의
def draw_background(screen):
    # 좌표상의 직사각형 공간을 정의후 draw.rect를 통해 그린다.
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

# 블록(픽셀)을 그리는 함수 정의
def draw_block(screen, color, position):
    block = pygame.Rect(
        (position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
        (BLOCK_SIZE, BLOCK_SIZE)
    )
    pygame.draw.rect(screen, color, block)

# 뱀이 움직이는 방향에 대한 오프셋
class Offset:
    NONE = [0, 0]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    UP = [0, -1]
    DOWN = [0, 1]

# 뱀의 위치와 방향, 색을 정의하는 클래스
class Snake:
    # 생성시 뱀의 색상과 위치, 초기에 움질일 방향을 입력
    def __init__(self, color, position, offset):
        self.color = color
        self.offset = offset
        # 머리 ~ 꼬리의 위치들
        self.positions =[
            position,
            [position[0], position[1] + 1],
            [position[0], position[1] + 2],
            [position[0], position[1] + 3]
        ]
        # TODO: snake 에 지능
        self.neural_network = NeuralNetwork(6,30,3)

    # 뱀을 그리는 함수
    def draw(self):
        for position in self.positions:
            draw_block(screen, self.color, position)

    # 뱀을 움직이는 함수 - 꼬리가 머리를 따라가게 함
    def move(self):
        # 현재 위치를 기억
        now_pos = [self.positions[0][0], self.positions[0][1]]
        # 머리를 오프셋만큼 이동
        self.positions[0][0] += self.offset[0]
        self.positions[0][1] += self.offset[1]
        # 마지막 위치를 기억
        last_pos = now_pos
        for i in range(1, len(self.positions)):
            now_pos = [self.positions[i][0], self.positions[i][1]]
            self.positions[i] = last_pos
            last_pos = now_pos

    # 뱀의 꼬리 길이를 한칸 늘리는 함수
    def grow(self):
        self.positions.append([self.positions[-1][0], self.positions[-1][1]])
    # TODO: 현재 방향을 기준으로 전방,좌측, 우측Offeset을 리턴하는 함수
    def getDirection(self):
        # 리턴 값은 [Front,left,right]
        if self.offset == Offset.UP:
            return [Offset.UP, Offset.LEFT, Offset.RIGHT]
        elif self.offset == Offset.DOWN:
            return [ Offset.DOWN, Offset.RIGHT, Offset.LEFT]
        elif self.offset ==  Offset.LEFT:
            return[ Offset.LEFT,  Offset.DOWN,Offset.UP]
        else:
            return [ Offset.RIGHT, Offset.UP,  Offset.DOWN]

    def obstacleSensor(self):
        ob_sensor = [1.0,1.0,1.0]
        direction = self.getDirection()

        head = list(self.positions[0])
        for i in range(3):
            for j in range(1,6):
                if not(20>head[0] + direction[i][0] * j >= 0
                and 20>head[1] + direction[i][1] * j>= 0):
                    ob_sensor[i] -=0.2
                elif True: # TODO: 뱀꼬리를 감지하는 경우
                    pass
        return ob_sensor

    def appleSensor(self, applepos):
        direction = self.getDirection()
        fbeam = list(self.positions[0])
        while  0 <= fbeam[0] <20 and 0 <= fbeam[1] < 20:
            fbeam[0] += direction[0][0]
            fbeam[1] += direction[0][1]
            if fbeam == applepos:
                return [1.0, 0.0, 0.0]

            lbeam = list(fbeam)
            while 0 <= lbeam[0] <20 and 0 <= lbeam[1] < 20:
                if lbeam == applepos:
                    return  [0.0, 1.0, 0.0]
                lbeam[0] += direction[1][0]
                lbeam[1] += direction[1][1]

            rbeam = list(fbeam)
            while 0 <= rbeam[0] < 20 and 0 <= rbeam[1] < 20:
                if rbeam == applepos:
                    return [0.0,0.0,1.0]
                rbeam[0] += direction[2][0]
                rbeam[1] += direction[2][1]

        return [0.0, 0.0, 0.0]
    # TODO: 신경망의 결과값을 보고 다음 이동 Offset 을 정해주는 함수
    def setOffeset(self,output):
        direction = self.getDirection()
        self.offset = direction[np.argmax(output)]


# 사과의 색과 위치를 정의하는 클래스
class Apple:
    # 생성시 사과의 위치와 색상을 입력한다.
    def __init__(self, color, position):
        self.color = color
        self.position = position

    # 사과를 그리는 함수
    def draw(self):
        draw_block(screen, self.color, self.position)

    # 사과를 랜덤한 위치로 이동 시키는 함수
    def random_move(self, snake):
        self.position = [random.randint(0, 19), random.randint(0, 19)]
        while self.position in snake.positions:
            self.position = [random.randint(0, 19), random.randint(0, 19)]

# 게임을 정의하는 클래스
class Game:
    # 생성시 뱀과 사과의 인스턴스를 생성한다.
    def __init__(self):
        self.snake = Snake(GREEN, [9, 9], Offset.UP)
        self.apple = Apple(RED, [3, 3])
        self.score = 0
        self.timer = 50
    # 배경과 생성된 인스턴스들을 그리는 함수
    def draw(self):
        draw_background(screen)
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()  # 그려진 내용이 반영되도록 업데이트를 합시다.

    def inCrush(self):
        shead = self.snake.positions[0]
        if shead in self.snake.positions[1:]:
            return True
        if shead[0] < 0 or shead[1] > 19 or shead[1] < 0 or shead[1] > 19:
            return True
        return False
    # 게임을 진행하는 함수
    def start(self):
        last_movement = datetime.now()
        keydown_flag = False    # 키가 눌림 상태인지 확인하는 플래그
        last_input = []
        last_output = []
        eat_list = []
        live_list = []
        time_speed = 1
        train_cnt = 0
        max_score = 0

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and not keydown_flag:
                    if event.key == pygame.K_RIGHT and self.snake.offset != Offset.LEFT:
                        self.snake.offset = Offset.RIGHT
                        keydown_flag = True
                    elif event.key == pygame.K_LEFT and self.snake.offset != Offset.RIGHT:
                        self.snake.offset = Offset.LEFT
                        keydown_flag = True
                    elif event.key == pygame.K_UP and self.snake.offset != Offset.DOWN:
                        self.snake.offset = Offset.UP
                        keydown_flag = True
                    elif event.key == pygame.K_DOWN and self.snake.offset != Offset.UP:
                        self.snake.offset = Offset.DOWN
                        keydown_flag = True
                    # TODO 계임 속도 조절
                    elif event.key == pygame.K_w:
                        time_speed = time_speed - 1 if not time_speed == 1 else 1
                    elif event.key == pygame.K_s:
                        time_speed = time_speed + 1 if not time_speed == 300 else 300

            if self.snake.positions[0] == self.apple.position:
                # 사과를 없애고 새로운 위치에 생성
                # 뱀의 길이를 한칸 늘려줌
                self.apple.random_move(self.snake)
                self.snake.grow()
                # TODO: 점수 증가와 타이머 증가
                self.score += 1
                self.timer += 50
                # TODO 사과를 먹은 경우에 대한 input과 output을 eat_list에 삽입
                output = [0.0, 0.0, 0.0]
                output[np.argmax(last_output)] = 1.0
                eat_list.insert(0, [last_input, output])

            # TODO: 뱀이 꼬리나 벽에 충돌했을때 처리
            if self.inCrush() or self.timer == 0:
                # TODO: 점수가 0점이면 마지막 input에 대해 랜덤 output 학습
                if self.score == 0:
                    for i in range(10):
                        output = [0.0, 0.0, 0.0]
                        output[random.randint(0, 2)] = 1.0
                        self.snake.neural_network.train(last_input, output, 0.1)
                elif self.inCrush():
                    for io in live_list:
                        self.snake.neural_network.train(io[0], io[1], 0.01)

                for io in eat_list:
                    self.snake.neural_network.train(io[0], io[1], 0.02)
                least_input = []
                last_output = []
                live_list = []

                train_cnt += 1
                if max_score < self.score:
                    print(F"{train_cnt}회 학습중 최고 점수{self.score}")
                    max_score = self.score

                brain = self.snake.neural_network
                self.__init__()
                self.apple.random_move(self.snake)
                self.snake.neural_network = brain


            if timedelta(milliseconds=time_speed) <= datetime.now() - last_movement:
                self.timer -= 1
                #TODO: 생존한 경우 생존 리스트에 마지만 input가ㅗ output 삽입
                if len(last_input) != 0 and len(last_output) != 0:
                    output = [0.0,0.0,0.0]
                    output[np.argmax(last_output)] = 1.0
                    live_list.insert(0,[last_input,output])
                # TODO: 신경망의 input 갑 생성
                input1 = self.snake.obstacleSensor()
                input2 = self.snake.appleSensor(self.apple.position)
                last_input = input1 + input2
                # TODO: 생성된 input 값으로 신경망에 절의(질문)
                last_output = self.snake.neural_network.query(last_input)
                # TODO: output 값을 보고 다음 이동방향 결정
                self.snake.setOffeset(last_output)


                self.snake.move()
                last_movement = datetime.now()
                keydown_flag = False

            self.draw()

game = Game()
game.start()
