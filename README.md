# MultiSend Script for BSC-USDT Transactions

## Overview

This project contains Python scripts to facilitate the generation of JSON transaction files for BSC-USDT multi-send operations. The scripts read data from an Excel file, process it, and generate JSON files in the required format for multi-send transactions.

## Prerequisites

- Python 3.x
- Pandas library (`pip install pandas`)
- Openpyxl library (`pip install openpyxl`)

## Project Structure

multisend  
├── recipients.xlsx # Excel file with recipient addresses and amounts  
├── generate_usdt_transfer_json.py # Script for USDT multi-send transaction generation  
├── generate_bnb_transfer_json.py # Script for BNB multi-send transaction generation  
└── README.md # Project documentation

## Excel File Format

The Excel file (`recipients.xlsx`) should have the following columns:

- `recipient`: The recipient's wallet address.
- `amount`: The amount to be transferred to the recipient.

Example:

| recipient                                  | amount |
| ------------------------------------------ | ------ |
| 0x6edebeA9D8a00cF3e9F9E3a17D3f9e41dfA82821 | 1E+16  |
| 0xC9C44Ce2Fe370AcF67143749334A48032cB113be | 1E+16  |

## Scripts

### 1. `generate_bnb_transfer_json.py`

This script reads recipient data from the Excel file and generates JSON transaction files for BSC-USDT multi-send operations. The transactions are split into chunks of 500 transactions per file.

#### Usage

1. Place the `recipients.xlsx` file in the same directory as the script.
2. Run the script:
   ```bash
   python generate_bnb_transfer_json.py
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contact us if you have any questions or need further assistance regarding deployment and usage.
