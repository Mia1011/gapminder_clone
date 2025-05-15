200 Countries, 200 Years, 4 Minutes

## 簡介
這個專案復刻的是名聞遐邇的 [Hans Rosling's 200 Countries, 200 Years, 4 Minutes](https://youtu.be/jbkSRLYSojo?si=J721nOUK5bfS5ugY) 資料視覺化，我用 `pandas` 與 `sqlite3` 建立資料庫，並採用 `matplotlib` 進行概念驗證，最後以 `plotly.express` 做出成品。


## 如何重現
- 安裝 [Miniconda](https://youtu.be/jbkSRLYSojo?si=J721nOUK5bfS5ugY)

- 依據 `environment.yml` 建立環境
```shell
conda env create -f environment.yml
```

- 將 `data/` 資料夾中的四個 CSV 檔案置放於工作目錄中的 `data/` 資料夾。

- 啟動環境並執行 `python create_gapminder_db.py` 就能在 `data/` 資料夾中建立 `gapminder.db`

- 啟動環境並執行 `python plot_with_px.py` 就能生成 `gapminder_clone.html`
