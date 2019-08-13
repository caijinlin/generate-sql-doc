# AutoBuildDocFromDB

基于2liang/AutoBuildDocFromDB开发，使用SQL文件自动生成markdown格式的数据库文档。

## 使用说明

1. 使用git克隆该项目

2. 从数据库中导出sql文件，请尽量导出只有表结构无表数据的sql文件

3. 在项目目录下运行：`python build.py sql_dir`，其中sql_dir为您的sql文件夹路径

4. 生成成功的md文件，在项目的md文件夹中