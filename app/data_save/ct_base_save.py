from abc import ABC, abstractmethod
from typing import List
from app.model.ct_transaction import TransactionRecord

class CTDataSave(ABC):
    
    @abstractmethod
    def save_data(self, records: List[TransactionRecord], wallet_address: str, target: str): #target can be filename or tablename
        pass

