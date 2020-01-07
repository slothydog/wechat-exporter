# Wechat Exporter(未完成)

> 微信聊天记录导出、分析工具 For iOS

> Another Modification of [Wechat Explorer](https://github.com/humiaozuzu/wechat-explorer).
> Extended From [Wechat Exporter](https://github.com/jieyaoke/wechat-exporter).


## 说明

前置项目[Wechat Explorer](https://github.com/humiaozuzu/wechat-explorer)由于微信的数据表结构发生了变化，所以已经无法再使用了。
本项目主要对相应的变化进行了调整，并想加入几个新功能。

同时完善README，更好地帮助大家使用这个工具。

## 使用说明

### 从iOS备份文件中提取WeChat数据

#### 可用工具

- iMazing
- iPhone Backup Extractor
- iExplorer

#### 导出数据文件
导出com.tencent.xin中的Documents文件夹。

其中无规则字串文件夹就是对应不同WXID的微信号(经过MD5 Hash)。

![iMazing](https://raw.githubusercontent.com/Duerxin/wechat-exporter/master/README_Images/iMazing.png)

### WXID
获得wxid，目前我没有找到比较简单的方法。

目前我是在其他微信账号的数据库，查找个人的wxid。

### 使用方法

#### 安装
下载解压后
```bash
python setup.py build
python setup.py install
```

#### 使用
``` bash
cd Path/To/Documents
(Available) wxep list_chatrooms ../Documents your_user_id
(Available) wxep list_friends ../Documents your_user_id
wxep get_chatroom_stats ../Documents user_id chatroom_id@chatroom 2015-08-01 2020-01-01
(Available) wxep export_chatroom_records ../Documents your_user_id chatroom_id@chatroom 2015-10-01 2020-01-01 ../
wxep get_friend_label_stats ../Documents your_user_id
```

#### 卸载
```bash
pip uninsatll wechat-exporter
```

## 原理

由于 iOS 本身的限制，是拿不到任何数据的。我们只能从 iTunes 的备份中，导出微信 App 的数据，然后通过分析数据，实现一系列的功能（比如导出聊天记录，数据计算等等）。

### 直接使用
1. 下载软件 [DB Browser for SQLite](https://sqlitebrowser.org/dl/), 并安装;

2. 
- 打开 Path/To/Documents/MD5(Your WXID)/DB/WCDB_Contact.sqlite (通讯录)
- 打开 Path/To/Documents/MD5(Your WXID)/DB/MM.sqlite （聊天数据）

3. 选择"浏览数据"
- WCDB_Contact.sqlite -> [Table]Friends
- MM.sqlite -> [Table]Chat_XXXXX( MD5(WXID)/MD5(chatroom_id@chatroom_id) )

4. 导出表为Json/Csv, 再利用其它软件处理


## References
- [手把手教你用Python分析微信聊天内容](https://www.cnblogs.com/guohaojintian/p/11608716.html)


