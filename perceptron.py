# 데이터 분석을 위한 기초 라이브러리로 고성능 수치계산을 위해 제작되었음
# Numeric Python 의 약칭, 백터 및 행렬 연산에 있어서 매우 편리한 기능을 제공
import numpy as np

# 과학 분석 알고리즘을 위한 모듈, 수치적분, 미분방정식 해석기, 확률 분포와 같은
# 다양한 통계관련 도구를 제공, 여기서는 Sigmoid 함수를 위한 special 만 사용
import scipy.special

# 신경망 클래스 정의
class NeuralNetwork:
    # 신경망 초기화
    # 입력노드, 히든노드, 출력노드의 개수와 학습률을 초기화하고 가중치 행렬을 생성
    def __init__(self, inputnodes, hiddennodes, outputnodes):
        self.inodes = inputnodes    # 입력 노드
        self.hnodes = hiddennodes   # 히든 노드
        self.onodes = outputnodes   # 출력 노드

        # 가중치 행렬 wih (weight of input -> hidden)
        # 가중치 행렬 who (weight of hidden -> output)
        # 중앙값이 0.0이고 표준편차를 노드 개수에 루트를 씌우고 역수를 취한값을 지정한 분포도 생성
        # 분포도에서 랜덤한 값을 가져와 (노드 개수 x 노드 개수)의 행렬을 생성한다.
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # 활성화 함수로 시그모이드 함수를 사용
        self.activation_function = lambda x: scipy.special.expit(x)

    # 신경망 학습 함수
    def train(self, inputs_list, targets_list, learning_rate):
        # 입력 리스트를 2차원 전치 행렬로 변환
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T

        # 히든 계층으로 들어오는 신호를 계산
        hidden_layer_in = np.dot(self.wih, inputs)
        # 히든 계층에서 나가는 신호를 계산
        hidden_layer_out = self.activation_function(hidden_layer_in)

        # 출력 계층으로 들어오는 신호를 계산
        output_layer_in = np.dot(self.who, hidden_layer_out)
        # 출력 계층에서 나가는 신호를 계산 (인풋 -> 히든 -> 아웃풋의 최종 결과)
        output_layer_out = self.activation_function(output_layer_in)

        # 실제 값과의 오차를 계산 (오차 = 실제 값 - 계산 값)
        output_error = targets - output_layer_out
        # 은닉 계층의 오차를 계산 (가중치에 의해 나뉜 출력 계층의 오차들을 재조합)
        hidden_error = np.dot(self.who.T, output_error)

        # 은닉 계층과 출력 계층 간의 가중치 업데이트 (역전파 발생)
        self.who += learning_rate * np.dot((output_error * output_layer_out * (1.0 - output_layer_out)), np.transpose(hidden_layer_out))
        # 입력 계층과 은닉 계층 간의 가중치 업데이트 (역전파 발생)
        self.wih += learning_rate * np.dot((hidden_error * hidden_layer_out * (1.0 - hidden_layer_out)), np.transpose(inputs))


    # 신경망에 물어보기
    def query(self, inputs_list):
        # 입력 리스트를 2차원 전치 행렬로 변환
        inputs = np.array(inputs_list, ndmin=2).T

        # 은닉 계층으로 들어오는 신호를 계산
        hidden_layer_in = np.dot(self.wih, inputs)
        # 은닉 계층에서 나가는 신호를 계산
        hidden_layer_out = self.activation_function(hidden_layer_in)

        # 출력 계층으로 들어오는 신호를 계산
        output_layer_in = np.dot(self.who, hidden_layer_out)
        # 출력 계층에서 나가는 신호를 계산 (결과값)
        output_layer_out = self.activation_function(output_layer_in)

        return output_layer_out
