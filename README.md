# alchemist-helper

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
   git clone https://github.com/JeffersonQin/alchemist-helper
   ```
2. 脚本赋权
   ```bash
   chmod 777 ./alchemist-helper/deploy.sh
   ```
3. 执行脚本
   ```bash
   ./alchemist-helper/deploy.sh <your-repo-to-clone>
   ```
