from abc import ABC, abstractmethod

class CTBase(ABC):
    @abstractmethod
    def get_normal_transactions(self, address: str) -> list:
        pass

    @abstractmethod
    def get_internal_transactions(self, address: str) -> list:
        pass

    @abstractmethod
    def get_ERC20_transfers(self, address: str) -> list:
        pass

    @abstractmethod
    def get_ERC721_transfers(self, address: str) -> list:
        pass

    @abstractmethod
    def get_ERC1155_transfers(self, address: str) -> list:
        pass
