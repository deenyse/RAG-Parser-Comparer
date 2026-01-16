import yaml
import os


def get_config(file_path="config.yaml"):
    """
    Get config from file, or from environment variables.
    """
    try:
        #check file existence
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No {file_path} config file found.")

        # Read YAML
        with open(file_path, "r") as file:
            config = yaml.safe_load(file)
            if not config:
                raise ValueError(f"Confing YAML {file_path} is empty.")

        # Check GEMINI_API_KEY existence
        if os.getenv("GEMINI_API_KEY") and not config["gemini_config"]["api_key"]:
            config["gemini_config"]["api_key"] = os.getenv("GEMINI_API_KEY")

        if not config["gemini_config"]["api_key"]:
            raise ValueError("GEMINI_API_KEY is not in config.yaml whether environment variables are set.")



        return config

    except yaml.YAMLError as e:
        raise ValueError(f"Parsing YAML issue: {str(e)}")
    except Exception as e:
        raise ValueError(f"Error during confing loading: {str(e)}")