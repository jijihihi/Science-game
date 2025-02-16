from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

print("현재 작업 디렉토리:", os.getcwd())  # 현재 Flask가 실행 중인 위치 출력
print("템플릿 경로:", os.path.join(os.getcwd(), "templates"))  # Flask가 찾는 templates 경로 출력

# 웹 페이지 기본 화면
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/result')
def result():
    age = request.args.get('age', 'Unknown')  # URL에서 `age` 값 가져오기
    gender = request.args.get('gender', 'Unknown')  # URL에서 `gender` 값 가져오기
    history = request.args.get('history', 'Unknown')  # URL에서 `history` 값 가져오기

    print(f"🔍 받은 데이터 - 나이: {age}, 성별: {gender}, 가족력: {history}")
    
    return render_template('result.html', age=age, gender=gender, history=history)


# 사용자 입력 처리 (예: 나이를 입력하면 간단한 계산 수행)
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    age = int(data.get('age', 30))
    
    # 간단한 계산: 나이가 많을수록 위험도 증가 (단순 모델)
    risk = (age - 20) * 2  # (실제론 더 복잡한 모델을 적용 가능)

    return jsonify({"risk": risk})



if __name__ == '__main__':
    app.run(debug=True)