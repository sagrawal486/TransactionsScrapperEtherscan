from app.data_save.ct_base_save import CTDataSave
import pandas as pd
from typing import List
from app.model.ct_transaction import TransactionRecord
import os
class CTCSVSave(CTDataSave):
    
    def save_data(self, records: List[TransactionRecord], wallet_address: str, filename: str):
        try:
            rows = []
            for r in records:
                row = r.model_dump(by_alias=True)  # use model_dump in Pydantic v2
                row = {"Wallet Address": wallet_address, **row}  # insert as first column
                rows.append(row)

            df = pd.DataFrame(rows)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            df.to_csv(filename, index=False)

        except Exception as e:
            print(f"Error while saving data into file - ", str(e))
            raise


