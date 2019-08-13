# -*- coding:utf-8 -*-
# Author : 我才是二亮 (unstring@163.com)
import sys, os.path
from FileParserClass import FileParser
from MarkdownBuildClass import MarkDownBuild

def downdir(path):
    md_dir = './md/'
    file_name = 'sql.md'
    file_obj = open(md_dir + file_name, 'a');
    file_obj.write('# 数据库文档\n\n')

    files= os.listdir(path) #得到文件夹下的所有文件名称
    for file in files: #遍历文件夹
        if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
            text = downfile(path+"/"+file); 
            try:
                file_obj = open(md_dir + file_name, 'a')
            except:
                exit('文件创建失败')
            try:
                file_obj.write(text)
            except:
                exit('文件写入失败')
            finally:
                file_obj.close()

    print '数据库文档已经成功创建,文件在md目录下.'

def downfile(file): 

    content = ''

    dir = file
    try:
        file = open(dir)
    except IOError, e:
        exit(e)
    try:
        content = file.read()
    except:
        exit('文件读取失败')
    finally:
        file.close()

    file_parser = FileParser()
    # 将文件分离为每张表
    table_list = file_parser.separatTable(content)
    # 解析出表中表名及表详情
    table_name = file_parser.parserTableName(table_list)
    # 解析出每张表字段情况并与表名表详情组合
    table_data = file_parser.parserColumn(table_list, table_name)

    markdown_build = MarkDownBuild()

    text = markdown_build.buildMarkdown(table_data)
    
    return text

if __name__ == '__main__':

    #print sys.argv[1];
    downdir(sys.argv[1])


