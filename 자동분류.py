import os
import shutil

def organize_downloads():
    # 다운로드 폴더 경로
    download_folder = r'C:\Users\student\Downloads'

    # 이동할 폴더 경로 설정
    image_folder = os.path.join(download_folder, 'images')
    data_folder = os.path.join(download_folder, 'data')
    docs_folder = os.path.join(download_folder, 'docs')
    archive_folder = os.path.join(download_folder, 'archive')

    # 폴더 생성
    for folder in [image_folder, data_folder, docs_folder, archive_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # 파일 이동
    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)
        if os.path.isfile(file_path):
            if file.lower().endswith(('.jpg', '.jpeg')):
                shutil.move(file_path, os.path.join(image_folder, file))
            elif file.lower().endswith(('.csv', '.xlsx')):
                shutil.move(file_path, os.path.join(data_folder, file))
            elif file.lower().endswith(('.txt', '.doc', '.pdf')):
                shutil.move(file_path, os.path.join(docs_folder, file))
            elif file.lower().endswith('.zip'):
                shutil.move(file_path, os.path.join(archive_folder, file))

if __name__ == "__main__":
    organize_downloads()
