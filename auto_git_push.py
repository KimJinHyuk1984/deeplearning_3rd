import subprocess
import os
from datetime import datetime

# GitHub 원격 저장소 주소
REPO_URL = "https://github.com/KimJinHyuk1984/deeplearning_3rd.git"
BRANCH = "main"

# 현재 작업 폴더
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)

# 현재 시간으로 커밋 메시지
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_msg = f"최초 커밋 또는 자동 업데이트: {now}"

# Git 초기화
if not os.path.exists(os.path.join(current_dir, ".git")):
    print("🧱 Git 저장소가 없네요 → 초기화 및 원격 설정 중...")
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "remote", "add", "origin", REPO_URL], check=True)
        subprocess.run(["git", "branch", "-M", BRANCH], check=True)
    except subprocess.CalledProcessError as e:
        print("❌ git 초기화/원격 설정 오류:", e.stderr)
        exit(1)

# add, commit, push
try:
    subprocess.run(["git", "add", "."], check=True)

    result = subprocess.run(
        ["git", "commit", "-m", commit_msg],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if "nothing to commit" in result.stdout.lower():
        print("📁 커밋할 변경사항이 없습니다. push 생략.")
        exit(0)
    else:
        print(f"✅ 커밋 완료: {commit_msg}")

    subprocess.run(["git", "push", "-u", "origin", BRANCH], check=True)
    print("🚀 원격 저장소에 업로드 완료!")

except subprocess.CalledProcessError as e:
    print("❌ Git 명령 오류:", e.stderr)
