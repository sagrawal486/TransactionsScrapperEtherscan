## Project Setup Documentation 

## Setup (on windows)
    - Download and Install python 3.9.5 and add it to the environment variable 
    - python -m venv venv
    - venv\Scripts\activate
    - pip install -r requirements.txt
    - Update the file export path in app_settings.ini 
    - python .\main.py (from TransactionsScrapperEtherscan folder)

## Assumptions
    - Etherscan, Alchemy, Blockscout, Infura - Only 1 source of API is sufficient
    - System able to save csv data for wallet addresses having transaction count < 10000, for heavier wallet it could throw error
    - System only get Ethereum wallet addresses
    - Parallel data fetching of wallet address is not required for this demo
    - Unit Tests implementation is not required, so only included function names to see what tests can be implemented.
    - Full historical data is required.

## Architecture Decisions
    - Interface based implementations instead of inheritance
    - We can easily add 'save into db' functionality besides 'save into csv' which follows open/close principal
    - Separted data fetching, data processing and data saving into different modules to separate concerns
    - Used pydantic models for schema validation   
    - Used retry logic and pagination for full historical data
    