from abc import ABC, abstractmethod

class CTBaseProcessor(ABC):
    @abstractmethod
    def normal_transactions_processor(self, raw_data: list) -> list:
        pass

    @abstractmethod
    def internal_transactions_processor(self, raw_data: list) -> list:
        pass

    @abstractmethod
    def ERC20_transfers_processor(self, raw_data: list) -> list:
        pass

    @abstractmethod
    def ERC721_transfers_processor(self, raw_data: list) -> list:
        pass

    @abstractmethod
    def ERC1155_transfers_processor(self, raw_data: list) -> list:
        pass
