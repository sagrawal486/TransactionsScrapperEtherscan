import os
from app.data_sources.ct_etherscan import CTEtherscan
from app.data_processing.ct_etherscan_processor import CTEtherscanProcessor
from app.data_save.ct_csv_save import CTCSVSave
from datetime import datetime
import pathlib

def test_normal_transactions_end_to_end():
    wallet = "0xa39b189482f984388a34460636fea9eb181ad1a6"
    file_path = f"D:\\Shivam\\test_{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"

    client = CTEtherscan(wallet)
    raw = client.get_normal_transactions()
    client_processor = CTEtherscanProcessor()
    records = client_processor.normal_transactions_processor(raw)
    saver = CTCSVSave()
    saver.save_data(records, wallet, str(file_path))
    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

def test_internal_transactions_end_to_end():
    assert 1 == 1


#Similarly define for other types of transactions

#End to end code for all types of transactions
def test_all_transactions_end_to_end():
    assert 1 == 1

