import os
import shutil
import gdown
from typing import List
from src.utils.MongoDBHandler import MongoDBHandler


class FileManager:
    """
    Tool for managing local test files.
    Assumes ALL links provided are Google Drive links.
    Uses 'gdown' for robust downloading (handles auth, large files, view/download links).
    """
    def __init__(self, base_folder: str = "data/files") -> None:
        self.base_folder = base_folder

    def get_file_location(self, file_name: str) -> str:
        return os.path.join(self.base_folder, file_name)
    def reinitFiles(self) -> None:
        if os.path.exists(self.base_folder):
            try:
                shutil.rmtree(self.base_folder)
                print(f"Folder '{self.base_folder}' cleared.")
            except Exception as e:
                print(f"Error clearing folder: {e}")

        os.makedirs(self.base_folder, exist_ok=True)
        print(f"Folder '{self.base_folder}' (re)created.")

    def updateFiles(self, mongo: MongoDBHandler) -> List[str]:
        required_files = mongo.getFileNames()

        if not required_files:
            print("No files required/found.")
            return []

        if not os.path.exists(self.base_folder):
            os.makedirs(self.base_folder)

        existing_files = set(os.listdir(self.base_folder))
        required_set = set(required_files)
        missing_files = list(required_set - existing_files)

        if not missing_files:
            print(f"All {len(required_files)} required files are present in '{self.base_folder}'.")
            return required_files

        print(f"Missing files: {missing_files}")

        links_map = mongo.getFilesLinks(missing_files)

        for filename in missing_files:
            link = links_map.get(filename)
            if not link:
                print(f"⚠️ Warning: No link found for '{filename}' in DB. Skipping.")
                continue

            print(f"Downloading '{filename}' from Google Drive...")
            dest_path = os.path.join(self.base_folder, filename)

            success = self._download_from_google_drive(link, dest_path)

            if success:
                print(f"✅ '{filename}' downloaded successfully.")
            else:
                print(f"❌ Failed to download '{filename}'.")
                if os.path.exists(dest_path):
                    try:
                        os.remove(dest_path)
                    except:
                        pass

        return required_files

    def _download_from_google_drive(self, url: str, destination: str) -> bool:
        """
        Downloads file using gdown library.
        Handles 'view' links, ID extraction, and virus warning confirmations automatically.
        """
        try:
            output = gdown.download(url, destination, quiet=False, fuzzy=True)

            return output is not None

        except Exception as e:
            print(f"gdown error: {e}")
            return False