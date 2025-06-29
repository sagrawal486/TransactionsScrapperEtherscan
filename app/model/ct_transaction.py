from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TransactionRecord(BaseModel):
    transaction_hash: str = Field(..., alias="Transaction Hash")
    transaction_time: datetime = Field(..., alias="Date & Time")
    from_address: str = Field(..., alias="From Address")
    to_address: str = Field(..., alias="To Address")
    transaction_type: str = Field(..., alias="Transaction Type")  # ETH, ERC-20, etc.
    asset_contract_address: Optional[str] = Field(None, alias="Asset Contract Address")
    asset_symbol: Optional[str] = Field(None, alias="Asset Symbol / Name")
    token_id: Optional[str] = Field(None, alias="Token ID")
    value: Optional[float] = Field(0.0, alias="Value / Amount")  # In ETH or token units
    gas_fee_eth: Optional[float] = Field(0.0, alias="Gas Fee (ETH)")

    class Config:
        populate_by_name = True 
        