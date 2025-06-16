import subprocess
from datetime import datetime

# 현재 시간 포맷 설정
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"자동 커밋: {now}"

# Git 명령어 리스트
commands = [
    ['git', 'add', '.', '모두의 딥러닝 3rd.ipynb'],
    ['git', 'commit', '-m', commit_message],
    ['git', 'push', 'origin', 'main']
]

for cmd in commands:
    try:
        result = subprocess.run(
            cmd,
            check=True,
            text=True,
            capture_output=True,
            encoding='utf-8'  # 🔧 인코딩 설정 추가
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ 오류 발생: {e.stderr}")
