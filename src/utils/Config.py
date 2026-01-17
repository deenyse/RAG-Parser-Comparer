import yaml
import os



class Config:
    _config_path = "configs/config.yaml"

    _config = None

    @classmethod
    def get(cls) -> dict:
        if cls._config is not None:
            return cls._config

        return cls.__get_from_file(cls._config_path)


    @classmethod
    def get_value(cls, *keys):
        """
        Get value by chain of keys
        Example: Config.get_value("azure", "api_key")
        """
        cfg = cls.get()
        try:
            for key in keys:
                cfg = cfg[key]
            return cfg
        except (KeyError, TypeError):
            raise KeyError(f"Config key path {' -> '.join(keys)} not found")

    @classmethod
    def __get_from_file(cls, file_path:str) -> dict:
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

            cls._config = config
            return config

        except yaml.YAMLError as e:
            raise ValueError(f"Parsing YAML issue: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error during confing loading: {str(e)}")
