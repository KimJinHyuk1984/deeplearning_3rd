import subprocess

# 현재 폴더의 모든 파일을 원격(main 브랜치)에서 덮어쓰기
command = ['git', 'checkout', 'origin/main', '--', '.']

try:
    result = subprocess.run(
        command,
        check=True,
        text=True,
        capture_output=True,
        encoding='utf-8'
    )
    print("✅ 원격 저장소의 최신 상태로 현재 디렉터리 파일을 갱신했습니다.\n")
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("❌ 오류 발생:")
    print(e.stderr)
