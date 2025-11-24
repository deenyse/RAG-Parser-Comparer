from pymongo import MongoClient
from bson import ObjectId
from typing import List, Dict, Optional


class MongoDBHandler:
    def __init__(self, config: dict) -> None:
        mongo_conf = config.get("mongodb", {})
        uri = mongo_conf.get("uri")
        db_name = mongo_conf.get("db_name")

        if not uri or not db_name:
            raise ValueError("MongoDB URI or DB Name is missing in config.")

        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]

            self.files_collection = self.db['files']
            self.qa_collection = self.db['qapairs']

        except Exception as e:
            raise Exception(f"Failed to connect to MongoDB: {e}")

    def getFileNames(self) -> List[str]:
        """
        Retrieves a list of all filenames from the 'files' collection.
        Returns:
            List[str]: List of filenames (e.g. ['G1341119.PDF', ...])
        """
        try:
            cursor = self.files_collection.find({}, {"filename": 1, "_id": 0})

            return [doc["filename"] for doc in cursor if "filename" in doc]
        except Exception as e:
            print(f"Error fetching filenames: {e}")
            return []

    def getFilesLinks(self, filenames: List[str]) -> Dict[str, str]:
        """
        Retrieves links for the provided list of filenames.
        Args:
            filenames (List[str]): List of filenames to look up.
        Returns:
            Dict[str, str]: Dictionary {filename: fileLink}
        """
        try:
            query = {"filename": {"$in": filenames}}
            projection = {"filename": 1, "fileLink": 1, "_id": 0}

            cursor = self.files_collection.find(query, projection)

            result = {}
            for doc in cursor:
                fname = doc.get("filename")
                flink = doc.get("fileLink")
                if fname:
                    result[fname] = flink

            return result
        except Exception as e:
            print(f"Error fetching file links: {e}")
            return {}

    def getFileQuestions(self, filename: str) -> List[str]:
        """
        Retrieves all questions associated with a specific file.
        1. Finds the file's _id in 'files' collection by filename.
        2. Uses that _id to find documents in 'qapairs' where fileId matches.

        Args:
            filename (str): Name of the file.
        Returns:
            List[str]: List of questions.
        """
        try:
            file_doc = self.files_collection.find_one({"filename": filename}, {"_id": 1})

            if not file_doc:
                print(f"File '{filename}' not found in database.")
                return []

            file_id = file_doc["_id"]

            query = {"fileId": file_id}
            projection = {"question": 1, "_id": 0}

            cursor = self.qa_collection.find(query, projection)

            return [doc["question"] for doc in cursor if "question" in doc]

        except Exception as e:
            print(f"Error fetching questions for {filename}: {e}")
            return []

    def close(self):
        self.client.close()