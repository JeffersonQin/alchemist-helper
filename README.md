# alchemist-helper

<a href="https://colab.research.google.com/gist/JeffersonQin/fee89976e6c15cc2828a682baf693621/easyclone.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

炼丹助手，用于快速部署到各大白嫖平台：

* Colab
* Kaggle
* 极市平台

## 内容简介

* 将 repo clone 到当前目录
* 大部分平台都是 Python 3.7 的环境，所以会执行脚本禁用掉某些 typing

## 使用方法

1. clone 本 repo
   ```bash
   !git clone https://github.com/JeffersonQin/alchemist-helper
   ```
2. 脚本赋权
   ```bash
   !chmod 777 ./alchemist-helper/deploy.sh
   ```
3. 执行脚本
   ```bash
   !./alchemist-helper/deploy.sh <your-repo-to-clone>
   ```

# 其他 Cheatsheet

## Notebook

禁用 `warning`:

```python
import warnings
warnings.filterwarnings("ignore")
```

## Kaggle

下载 Google Drive 文件，先安装 `gdown`:

```
!pip install gdown
```

下载文件：

```
!gdown --id <id>
```

显示文件链接

```python
from IPython.display import FileLink, display
display(FileLink('./path/to/file'))
```

## Google Drive 压缩文件

随便进一个 Colab 的环境然后 Mount Google Drive

Mount 的代码：

```python
from google.colab import drive
drive.mount('/content/drive')
```

打 tar 包（建议将路径直接切换到打包目录前，否则解压的时候够呛）：

```
!tar cvf FileName.tar path/to/folder
```

解 tar 包：

```
!tar xvf FileName.tar
```
