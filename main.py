import random
import time

from flask import Flask, request, render_template

# --

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    start_time = time.time()

    q = request.values.get('q')  # 쿼리
    m = request.values.get('m')  # 모드(일반/개발)
    g = request.values.get('g')  # 위치

    # 쿼리
    if not q:
        samples = ['제주국제공항', '스타벅스', '이마트서귀포점', '다음스페이스', '산방산온천', '협재해수욕장', '노형오거리']
        q = samples[random.randrange(len(samples))]

    # 모드(일반/개발)
    if not m:
        m = "1"  # 일반 모드

    # 위치
    if not g:
        g = str(random.randrange(3) + 1)
    if g == "1":  # 제주 공항
        latlng = "33.51106, 126.49144"
    elif g == "2":  # 중문 신라호텔
        latlng = "33.24739, 126.40802"
    elif g == "3":  # 성산일출봉
        latlng = "33.45782, 126.94253"

    return render_template('_index.html',
                           q=q,
                           m=m,
                           g=g,
                           elapsed='{:.3f}'.format((time.time() - start_time)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
