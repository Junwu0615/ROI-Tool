<a href='https://github.com/Junwu0615/ROI-Tool'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/ROI-Tool.svg'> 
<a href='https://github.com/Junwu0615/ROI-Tool'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/6c605b43f1b9dcb93f9c7b6c1a5103ab/raw/ROI-Tool_clone.json&logo=github'> </br>
[![](https://img.shields.io/badge/Project-ROI-blue.svg?style=plastic)](https://github.com/Junwu0615/ROI-Tool) 
[![](https://img.shields.io/badge/Language-Python_3.12.0-blue.svg?style=plastic)](https://www.python.org/) </br>
[![](https://img.shields.io/badge/Package-Pandas_2.1.4-green.svg?style=plastic)](https://pypi.org/project/pandas/) 
[![](https://img.shields.io/badge/Package-Matplotlib_3.8.2-green.svg?style=plastic)](https://pypi.org/project/matplotlib/) 
[![](https://img.shields.io/badge/Package-ArgumentParser_1.2.1-green.svg?style=plastic)](https://pypi.org/project/argumentparser/) 

## STEP.1　CLONE
```python
git clone git@github.com:Junwu0615/ROI-Tool.git
```

## STEP.2　INSTALL PACKAGES
```python
pip install -r requirements.txt
```

## STEP.3　RUN 
```python
python ROI.py -h
```

## STEP.4　HELP
- -h　Help:　Show this help message and exit.
- -w　Work Year:　您預計想要工作多少年 ?
- -y　Year:　您今年幾歲 ?
- -d　Dead:　您想活到幾歲 ?
- -e　Money Month:　您每月能投入股市資金 ?
- -r　ROI:　投資報酬率 ?
- -o　Object Number:　您預期想要達成金額 ?
- -m　Money Once:　您是否有一次性金額，若有則 `填數字`，反之則 `填0` 。


## STEP.5　EXAMPLE
`-w` 預計想要工作30年　|　`-y` 今年26歲　|　`-d` 活到90歲　|　<br/>
`-e` 每月能投入10K資金 |　`-r` ROI : 15%　|　`-o` 預期想達成3E　|　`-m` 一次性金額有300K
```python
python ROI.py -w 30 -y 26 -d 90 -e 10000 -r 15 -o 300000000 -m 300000
```
![範例動圖](sample.gif)
- 執行完畢後會在 `/results/` 生成 `3` 個輸出檔。
  - ROI_result.txt
  - 工作年-每年定存再投入之總資金成長走勢.png
  - <img  height=330 width=460 src="https://github.com/Junwu0615/ROI-Tool/blob/main/results/%E5%B7%A5%E4%BD%9C%E5%B9%B4-%E6%AF%8F%E5%B9%B4%E5%AE%9A%E5%AD%98%E5%86%8D%E6%8A%95%E5%85%A5%E4%B9%8B%E7%B8%BD%E8%B3%87%E9%87%91%E6%88%90%E9%95%B7%E8%B5%B0%E5%8B%A2.png"/>
  - 退休年-每年退休後之被動收入&提領出來之成長走勢.png
  - <img  height=330 width=460 src="https://github.com/Junwu0615/ROI-Tool/blob/main/results/%E9%80%80%E4%BC%91%E5%B9%B4-%E6%AF%8F%E5%B9%B4%E9%80%80%E4%BC%91%E5%BE%8C%E4%B9%8B%E8%A2%AB%E5%8B%95%E6%94%B6%E5%85%A5%26%E6%8F%90%E9%A0%98%E5%87%BA%E4%BE%86%E4%B9%8B%E6%88%90%E9%95%B7%E8%B5%B0%E5%8B%A2.png"/>
