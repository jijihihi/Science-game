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

@app.route('/process')
def process():
    return render_template('process.html')

@app.route('/animation')
def animation():
    return render_template('animation.html')

@app.route('/differentiation')
def differentiation():
    # 필요하다면 쿼리 파라미터 받아서 활용 가능
    age = request.args.get('age')
    gender = request.args.get('gender')
    history = request.args.get('history')
    return render_template('differentiation.html', age=age, gender=gender, history=history)

@app.route('/result')
def result():
    age = request.args.get('age', 'Unknown')
    gender = request.args.get('gender', 'Unknown')
    history = request.args.get('history', 'Unknown')
    return render_template('result.html', age=age, gender=gender, history=history)

# 새로운 final.html 파일을 렌더링하는 엔드포인트 추가
@app.route('/final')
def final():
    # 클라이언트 측 JavaScript가 URL의 쿼리 파라미터를 바로 읽어 처리하는 경우 아래처럼 단순히 렌더링할 수 있습니다.
    return render_template('final.html')
    
    # 만약 서버에서 기본값을 전달하고 싶다면, 아래와 같이 쿼리 파라미터를 받아 템플릿에 전달 가능합니다.
    # brainScore = request.args.get('brainScore', '85.6')
    # pdRisk = request.args.get('pdRisk', '5.1')
    # risks = request.args.get('risks', '운동 부족,영양 부족,과도한 스트레스')
    # effects = request.args.get('effects', '운동:규칙적인 운동은 도움이 됨,영양:균형 잡힌 식단 제공,스트레스:긍정적 정서 유지')
    # return render_template('final.html', brainScore=brainScore, pdRisk=pdRisk, risks=risks, effects=effects)

# 사용자 입력 처리 (예: 나이를 입력하면 간단한 계산 수행)
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    age = int(data.get('age', 30))
    
    # 간단한 계산: 나이가 많을수록 위험도 증가 (단순 모델)
    risk = (age - 20) * 2

    return jsonify({"risk": risk})

if __name__ == '__main__':
    app.run(debug=True)
