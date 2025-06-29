from app.data_sources.ct_etherscan import CTEtherscan
from app.data_processing.ct_etherscan_processor import CTEtherscanProcessor
from app.data_save.ct_csv_save import CTCSVSave
from app.configuration.ct_config import AppConfig
from datetime import datetime

def main():

    wallet_addresses = ['0xa39b189482f984388a34460636fea9eb181ad1a6','0xd620AADaBaA20d2af700853C4504028cba7C3333']

    for wallet_address in wallet_addresses:
        print(f"\nFetching transactions for: {wallet_address}\n")

        #Data Retrieval
        data_source = CTEtherscan(wallet_address)
        normal = data_source.get_normal_transactions()
        internal = data_source.get_internal_transactions()
        erc20 = data_source.get_ERC20_transfers()
        erc721 = data_source.get_ERC721_transfers()
        erc1155 = data_source.get_ERC1155_transfers()

        #Data Processing
        data_processor = CTEtherscanProcessor()
        normal = data_processor.normal_transactions_processor(normal)
        internal = data_processor.internal_transactions_processor(internal)
        erc20 = data_processor.ERC20_transfers_processor(erc20)
        erc721 = data_processor.ERC721_transfers_processor(erc721)
        erc1155 = data_processor.ERC1155_transfers_processor(erc1155)

        #Data Export
        app_config = AppConfig()
        export_path = app_config.file_export_path
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        export_path += f"\{wallet_address}_transactions_{timestamp}.csv"
        csv_save = CTCSVSave()
        all_transactions = normal + internal + erc20 + erc721 + erc1155
        csv_save.save_data(all_transactions, wallet_address, export_path)

        print(f"\nFetching transactions completed for: {wallet_address}\n")


if __name__ == "__main__":
    main()


