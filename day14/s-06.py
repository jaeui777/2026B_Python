# 로지스틱 회귀 : 범주형을 예측하는 대표적인 분류 알고리즘
import pandas as pd
df = pd.read_csv( './day15/Fish.csv') 


# [1] 데이터 로드 및 상단에서 2개 어종(이진 분류 대상) 먼저 추출

df = pd.read_csv('./day14/Fish.csv')
df_binary = df[(df['Species'] == 'Bream') | (df['Species'] == 'Smelt')]


# 특성 6개 (Weight, Length1, Length2, Length3, Height, Width) 및 타깃 정의

X = df_binary[['Weight', 'Length1', 'Length2', 'Length3', 'Height', 'Width']]
Y = df_binary['Species']


# [2] 훈련 / 테스트 세트 분리 (stratify 파라미터로 두 어종의 비율 유지)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42, stratify=Y )


# [3] 특성 스케일링 (훈련 데이터 기준으로 변환기 학습 후 테스트 데이터 적용)
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)


# [4] 로지스틱 회귀 모델 학습
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train_scaled, Y_train)


# [5] 모델 평가: 분류 정확도(Accuracy) 확인

y_pred = model.predict(X_test_scaled)
from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test, y_pred)

print(f"테스트 세트 분류 정확도(Accuracy): {acc:.4f}")


# [6] 결과 및 확률 확인 (테스트 세트 기준)

print("\n클래스 레이블 순서:", model.classes_) # ['Bream', 'Smelt']

print("예측값 (상위 3개):", model.predict(X_test_scaled[:3]))

print("예측 확률 (상위 3개):\n", model.predict_proba(X_test_scaled[:3]))