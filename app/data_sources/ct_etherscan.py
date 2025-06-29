import requests
from app.data_sources.ct_base import CTBase
import time
from app.configuration.ct_config import AppConfig

class CTEtherscan(CTBase):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        app_config = AppConfig()
        self.base_url = app_config.etherscan_base_url
        self.api_key = app_config.etherscan_api_key
        self.chain_id = 1

    def api_call(self, action: str) -> list:
        errorCount = 0
        page_no = 1
        offset = 1000
        transaction_data_raw = []
        while True:
            try:
                url = f"{self.base_url}?chainid={self.chain_id}&module=account&action={action}&address={self.wallet_address}&sort=desc&page={page_no}&offset={offset}&apikey={self.api_key}"
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                response = response.json()

                if isinstance(response['result'], str):
                    raise Exception(response["result"])
                
                if "Invalid API Key" in response['result']:
                    raise Exception("Invalid API key")

                if "Max rate limit reached" in response['result']:
                    raise Exception("Max rate limit reached")

                if len(response['result']) > 0:
                    transaction_data_raw += response['result']
                    page_no += 1
                else:
                    break
                
            except Exception as e:
                errorMessage = str(e)
                if (errorCount < 10 and ('Too Many Requests' in errorMessage or 'Read timed out' in errorMessage or 
                                        'RequestTimeout' in errorMessage or 'Max retries exceeded' in errorMessage or 
                                        'Request timestamp expired' in errorMessage or 'NetworkError' in errorMessage or 
                                        'Max rate limit reached' in errorMessage)):
                    print(f'Method:api_call; Timeout error.', action)
                    time.sleep(1)
                    errorCount += 1
                else:
                    print(('Method:{};action:{},{}').format('api_call',action, errorMessage))
                    raise
        return transaction_data_raw

    def get_normal_transactions(self) -> list:
        return self.api_call(action = 'txlist')        
        
    def get_internal_transactions(self) -> list:
        return self.api_call(action = 'txlistinternal')

    def get_ERC20_transfers(self) -> list:
        return self.api_call(action = 'tokentx')

    def get_ERC721_transfers(self) -> list:
        return self.api_call(action = 'tokennfttx')
            
    def get_ERC1155_transfers(self) -> list:
        return self.api_call(action = 'token1155tx')
