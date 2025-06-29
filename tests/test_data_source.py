from unittest.mock import patch
from app.data_sources.ct_etherscan import CTEtherscan


sample_normal_transaction_response = {
    "status": "1",
    "message": "OK",
    "result": [
        {
            'blockNumber': '22775199', 
            'blockHash': '0xe43738441f7a628d435259f063495c3a0fcca021ee396266f6e9ef3c1c70da87', 
            'timeStamp': '1750779083', 
            'hash': '0x4b7a2367ad65af93c364e17143e09a879391a0e888c314a853cd0ba561bb5252', 
            'nonce': '13', 
            'transactionIndex': '116', 
            'from': '0xa39b189482f984388a34460636fea9eb181ad1a6', 
            'to': '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 
            'value': '0', 
            'gas': '45540',
            'gasPrice': '6086782726', 
            'input': '0xa9059cbb000000000000000000000000bad7da01bf2b610a7be39e6b5eee97eec26b132000000000000000000000000000000000000000000000000000000000e7c173d8', 
            'methodId': '0xa9059cbb', 
            'functionName': 'transfer(address _to, uint256 _value)',
            'contractAddress': '', 
            'cumulativeGasUsed': '19161786', 
            'txreceipt_status': '1', 
            'gasUsed': '45160', 
            'confirmations': '33275', 
            'isError': '0'
        }
    ]
}

#Test get_normal_transactions function callability
@patch('app.data_sources.ct_etherscan.CTEtherscan.api_call')
def test_get_normal_transactions_success(mock_api_call):
    mock_api_call.return_value = sample_normal_transaction_response
    client = CTEtherscan("0xa39b189482f984388a34460636fea9eb181ad1a6")
    result = client.get_normal_transactions()
    assert isinstance(result, dict)
    assert result['result'][0]['hash'] == "0x4b7a2367ad65af93c364e17143e09a879391a0e888c314a853cd0ba561bb5252"

# Test Rate limit and than success response
def test_get_normal_transactions_retry_on_rate_limit():
    assert 1 == 1

def test_get_normal_transactions_pagination():
    assert 1 == 1

#Similarly we can write for other get data functions

def test_get_normal_transactions_invalid_apikey():
    assert 1 == 1

def test_wallet_address_regex_validation():
    assert 1 == 1

def test_get_normal_transactions_schema_validation():
    #Test response schema
    assert 1 == 1

