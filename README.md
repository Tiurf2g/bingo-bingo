# BINGO BINGO 智慧選號工具

這是可部署版的 Flask Web App。原本 Windows EXE 控制面板邏輯仍保留在 `app.py`，但預設啟動方式改成 Web Server，適合部署到 Render、Railway、Docker 或區域網路讓手機/電腦使用。

## 本機啟動

```powershell
cd "C:\Users\V002811\Documents\Codex\AI工具\bingo-deploy"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

開啟：

```text
http://127.0.0.1:10000
```

同一個 Wi-Fi 的手機也要用時，先查電腦 IP：

```powershell
ipconfig
```

手機瀏覽器開：

```text
http://你的電腦IP:10000
```

若 Windows 防火牆詢問，允許 Python 在私人網路通訊。

## Render 部署

1. 把這個資料夾推到 GitHub repository。
2. Render 建立 Web Service，連到該 repository。
3. Build Command 使用：

```bash
pip install -r requirements.txt
```

4. Start Command 使用：

```bash
gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 180
```

部署完成後，Render 給的網址可直接讓手機或電腦開啟。

## Docker 啟動

```bash
docker build -t bingo-bingo .
docker run --rm -p 10000:10000 bingo-bingo
```

## 桌面控制面板模式

如果還想用原本 Windows 控制面板啟動：

```powershell
$env:BINGO_DESKTOP="1"
python app.py
```

## 部署注意事項

`official_cache/` 是官方資料快取。免費雲端平台通常會重啟並清掉本機檔案，所以第一次進站或手動同步時可能需要重新抓資料。正式長期使用時，建議選有 persistent disk/volume 的方案，或之後把快取改成資料庫/雲端儲存。
