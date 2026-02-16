# Dockerfile
FROM python:3.10-slim

# 파이썬 출력 버퍼링 해제(로그 바로 보이게) + .pyc 생성 방지
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# (선택) OS 패키지 필요 시 여기에 추가
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#   && rm -rf /var/lib/apt/lists/*

# 의존성 먼저 복사 후 설치 (캐시 효율 ↑)
COPY requirements.txt ./
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY . .

# 런타임에서 GOOGLE_API_KEY 주입(빌드 시점에는 필요 없음)
# docker run -e GOOGLE_API_KEY=... ai-agent:tag
ENV GOOGLE_API_KEY=""

# 컨테이너 실행 시 기본 동작(원하시는 걸로 선택)
# 1) 파이프라인 시뮬레이터 실행
CMD ["python", "run_cicd_pipeline.py"]
