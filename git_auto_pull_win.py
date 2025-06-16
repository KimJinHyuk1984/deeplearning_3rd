import subprocess
import os

# GitHub 저장소 정보
REPO_URL = "https://github.com/KimJinHyuk1984/deeplearning_3rd.git"
REPO_FOLDER = "deeplearning_3rd"

# 현재 작업 디렉터리 (파이썬 파일이 위치한 폴더)
current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(current_dir, REPO_FOLDER)

# 1️⃣ 저장소가 없으면 clone
if not os.path.exists(target_dir):
    print("📥 저장소 없음 → clone 실행 중...")
    try:
        subprocess.run(["git", "clone", REPO_URL], check=True)
    except subprocess.CalledProcessError as e:
        print("❌ clone 중 오류 발생:")
        print(e.stderr)
        exit(1)

# 2️⃣ 저장소가 있다면 pull
else:
    print("📁 저장소 존재 → pull 실행 중...")
    os.chdir(target_dir)
    try:
        result = subprocess.run(
            ["git", "pull", "origin", "main"],
            check=True,
            text=True,
            capture_output=True,
            encoding="utf-8"
        )
        print("✅ 최신 내용으로 갱신 완료!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("❌ pull 중 오류 발생:")
        print(e.stderr)
