from pathlib import Path

base_path = Path(__file__).parent


target_folder = base_path / "test_folder"

print("프로그램 위치:", base_path)
print("정리할 폴더:", target_folder)
print("폴더 존재 여부:", target_folder.exists())

if target_folder.exists():
    for item in target_folder.iterdir():
        print(item.name)
else:
    print("test_folder를 찾을 수 없습니다.")

print("hello")
