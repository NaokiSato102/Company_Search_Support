import webbrowser
import urllib.parse


while(1):
	name = input("検索したい企業の名前を入力:")
	name = urllib.parse.quote(name)
	webbrowser.get(using=None).open("https://job.mynavi.jp/21/pc/corpinfo/searchCorpListByGenCond/index?actionMode=searchFw&srchWord="+name)
	webbrowser.get(using=None).open("https://job.rikunabi.com/2021/search/company/result/?fw="+name)
