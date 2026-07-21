from pathlib import Path
import shutil

# 초기 과정 시작
# print(Path.cwd())
# :현재 작업하는 기준폴더를 의미합니다

# folder = Path("test_folder")
# folder = Path(__file__).parent / "test_folder"
# __file__은 현재 파일의 주소입니다. .parent는 부모폴더이고 부모폴더중 test_folder를 찾게 됩니다

# print("현재 실행 위치:", Path.cwd())
# print("찾는 경로:", folder.resolve())
# 경로의 정확한 주소를 제공합니다. 디버깅할때 사용되고요

# print("폴더 존재:", folder.exists())
# 파일이나 폴더가 존재하는지 확인할때 사용합니다

# if not folder.exists():
#     print("test_folder를 찾을 수 없습니다.")
# else:
#     for file in folder.iterdir():
#         print(file.name)

# for file in folder.iterdir():
#     if file.is_file():
#         # print(file.name,file.suffix())
#         print(file.name,file.suffix)
# 초기 과정 끝

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".hwp"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
}

def get_category(extension):
    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print(f"폴더가 존재하지 않습니다: {folder.resolve()}")
        return

    if not folder.is_dir():
        print("입력한 경로는 폴더가 아닙니다.")
        return

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix)

        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file.name

        shutil.move(str(file), str(destination))

        print(f"{file.name} → {category}")


base_folder = Path().parent


# 정리할 폴더를 지정합니다
# path.home()은 c:\users\user를 의미하니 윈도우+E를 사용해서 주소창에 c:\users하면 user 폴더가 있는데 거기 폴더를 넣습니다
# "" 안에 정리할 폴더명을 넣습니다
# target_folder = Path.home() / "Documents"

# c:\users\user가 아닌 다른 경로의 폴더 정리시 ""안에 경로를 넣어주세요
target_folder = Path(r"")

organize_files(target_folder)