import pandas as pd
import json

# 엑셀 파일에서 데이터 읽기 (문자열로 읽기 위해 dtype 지정)
df = pd.read_excel('./data/recipients_20XR_LOCK.xlsx', dtype={'recipient': str, 'amount': str})

# JSON 템플릿 정의
template = {
    "version": "1.0",
    "chainId": "56",
    "createdAt": 1720154651660,
    "meta": {
        "name": "BSC-XR",
        "description": "",
        "txBuilderVersion": "1.16.5",
        "createdFromSafeAddress": "0x825EEf5eE88451A7FDEeE5d55eF41A1627125AB1",
        "createdFromOwnerAddress": "",
        "checksum": "0x0b10d552e93817088d8aba7076de118a6d6ec9836ac95399d23ea58e6e329c15"
    },
    "transactions": []
}

# 500개씩 잘라서 JSON 파일 생성
chunk_size = 500
chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]

for idx, chunk in enumerate(chunks):
    chunk_template = template.copy()
    chunk_template['transactions'] = []

    for index, row in chunk.iterrows():
        transaction = {
            "to": "0x5f78F4BFCb2b43bC174FE16A69a13945CEfA2978",  # XR 토큰 컨트랙트 주소
            "value": "0",
            "data": None,
            "contractMethod": {
                "inputs": [
                    {
                        "name": "to",
                        "type": "address",
                        "internalType": "address"
                    },
                    {
                        "name": "value",
                        "type": "uint256",
                        "internalType": "uint256"
                    }
                ],
                "name": "transfer",
                "payable": False
            },
            "contractInputsValues": {
                "to": row['recipient'],
                "value": row['amount']  # 이미 문자열로 읽었기 때문에 변환 불필요
            }
        }
        chunk_template['transactions'].append(transaction)
    
    # JSON 파일로 저장
    file_name = f'transactions_xr_part_{idx + 1}.json'
    with open(file_name, 'w') as json_file:
        json.dump(chunk_template, json_file, indent=4)
    
    print(f"JSON 파일이 성공적으로 생성되었습니다: {file_name}")
