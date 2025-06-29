from app.data_processing.ct_base_processor import CTBaseProcessor
from app.model.ct_transaction import TransactionRecord
from datetime import datetime, timezone

class CTEtherscanProcessor(CTBaseProcessor):

    def normal_transactions_processor(self, raw_data) -> list:
        records = []
        try:
            for row in raw_data:
                records.append(TransactionRecord(
                    transaction_hash = row.get("hash"),
                    transaction_time = datetime.fromtimestamp(int(row.get("timeStamp")),tz=timezone.utc),
                    from_address = row.get("from"),
                    to_address = row.get("to"),
                    transaction_type = "ETH transfer",
                    asset_contract_address = row.get("contractAddress"),
                    asset_symbol = "eth",
                    token_id = None,
                    value = int(row.get("value", 0)) / (10 **  18),
                    gas_fee_eth = int(row.get("gasUsed",0)) * int(row.get("gasPrice",0)) / (10 ** 18)
                ))
            return records
        except Exception as e:
            print(f"Error while parsing internal_transactions_processor data - ", str(e))
            raise
    
    def internal_transactions_processor(self, raw_data) -> list:
        records = []
        try:
            for row in raw_data:
                records.append(TransactionRecord(
                    transaction_hash = row.get("hash"),
                    transaction_time = datetime.fromtimestamp(int(row.get("timeStamp")),tz=timezone.utc),
                    from_address = row.get("from"),
                    to_address = row.get("to"),
                    transaction_type = "contract interaction",
                    asset_contract_address = row.get("contractAddress"),
                    asset_symbol = "eth",
                    token_id = None,
                    value = int(row.get("value", 0)) / (10 ** int(row.get("tokenDecimal", 0))),
                    gas_fee_eth = int(row.get("gasUsed",0)) * int(row.get("gasPrice",0)) / (10 ** 18)
                ))
            return records
        except Exception as e:
            print(f"Error while parsing internal_transactions_processor data - ", str(e))
            raise
    
    def ERC20_transfers_processor(self, raw_data) -> list:
        records = []
        try:
            for row in raw_data:
                records.append(TransactionRecord(
                    transaction_hash = row.get("hash"),
                    transaction_time = datetime.fromtimestamp(int(row.get("timeStamp")),tz=timezone.utc),
                    from_address = row.get("from"),
                    to_address = row.get("to"),
                    transaction_type = "ERC-20",
                    asset_contract_address = row.get("contractAddress"),
                    asset_symbol = row.get("tokenSymbol"),
                    token_id = None,
                    value = int(row.get("value", 0)) / (10 ** int(row.get("tokenDecimal", 0))),
                    gas_fee_eth = int(row.get("gasUsed",0)) * int(row.get("gasPrice",0)) / (10 ** 18)
                ))
            return records
        except Exception as e:
            print(f"Error while parsing internal_transactions_processor data - ", str(e))
            raise

    def ERC721_transfers_processor(self, raw_data) -> list:
        records = []
        try:
            for row in raw_data:
                records.append(TransactionRecord(
                    transaction_hash = row.get("hash"),
                    transaction_time = datetime.fromtimestamp(int(row.get("timeStamp")),tz=timezone.utc),
                    from_address = row.get("from"),
                    to_address = row.get("to"),
                    transaction_type = "ERC-721",
                    asset_contract_address = row.get("contractAddress"),
                    asset_symbol = row.get("tokenSymbol"),
                    token_id = row.get('tokenID'),
                    value = 1,
                    gas_fee_eth = int(row.get("gasUsed",0)) * int(row.get("gasPrice",0)) / (10 ** 18)
                ))
            return records
        except Exception as e:
            print(f"Error while parsing internal_transactions_processor data - ", str(e))
            raise
    
    def ERC1155_transfers_processor(self, raw_data) -> list:
        records = []
        try:
            for row in raw_data:
                records.append(TransactionRecord(
                    transaction_hash = row.get("hash"),
                    transaction_time = datetime.fromtimestamp(int(row.get("timeStamp")),tz=timezone.utc),
                    from_address = row.get("from"),
                    to_address = row.get("to"),
                    transaction_type = "ERC-1155",
                    asset_contract_address = row.get("contractAddress"),
                    asset_symbol = row.get("tokenSymbol"),
                    token_id = row.get('tokenID'),
                    value = int(row.get("tokenValue", 0)),
                    gas_fee_eth = int(row.get("gasUsed",0)) * int(row.get("gasPrice",0)) / (10 ** 18)
                ))
            return records
        except Exception as e:
            print(f"Error while parsing internal_transactions_processor data - ", str(e))
            raise
    
