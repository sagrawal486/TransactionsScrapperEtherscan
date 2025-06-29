import os
import configparser

class AppConfig:
    def __init__(self):

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # up 3 levels
        config_path = os.path.join(base_dir, 'app_settings.ini')

        self.parser = configparser.ConfigParser()
        self.parser.read(config_path)

        # Validate presence
        if not self.parser.sections():
            raise FileNotFoundError(f"Could not read config file at: {config_path}")

    @property
    def etherscan_base_url(self) -> str:
        return self.parser.get("ETHERSCANAPI", "BASEURL")

    @property
    def etherscan_api_key(self) -> str:
        return self.parser.get("ETHERSCANAPI", "APIKEY")
    
    @property
    def file_export_path(self) -> str:
        return self.parser.get("SYSTEMSETTING","EXPORTPATH")
