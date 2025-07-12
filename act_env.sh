#!/bin/bash
echo "建立虛擬環境..."
python3 -m venv venv

echo "啟用虛擬環境並安裝依賴..."
source venv/bin/activate
pip install -r requirements.txt

echo "完成！"
