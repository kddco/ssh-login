# ssh暴力破解

## 介紹作品

python3寫的ssh暴力破解嘗試登入程式


## 完成日期

2019/09/25
## 作者

kddchuang 偉恩

## 先安裝套件
sudo apt install python-pip
sudo pip install pexpect

## 作品功能
1.我想嘗試破解ip是127.0.0.1的ssh服務，並嘗試登入root帳號，使用同目錄下的字典檔名稱為10-million-password-list-top-1000000.txt
2.輸入指令
```
python ssh_tryTologin.py 127.0.0.1 root ./passwordlist.txt
```

## 心得感想

我的第一支自製攻擊程式，雖然簡陋但是我做了很久，嘗試從使用別人的工具到自製自己的工具。
