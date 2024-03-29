MultiTypeConsoleIn
======================
MultiTypeConsoleInはRTミドルウェア開発を支援するRTCです  
ConsoleInを拡張して複数の型のデータを受け取ることができます  
また、CSVファイルを読み込み出力する機能を持っています 

動作確認環境
------
Python:  
2.6.6  

OS:  
Windows 7 64bit / 32bit  
Ubuntu 10.04 LTS / 12.04 LTS 32bit  
 
ファイル構成
------
MultiTypeConsoleIn   
│―MultiTypeConsoleIn.py  
│―csvreader.py  
│―ini   
│　　│―consolein.ini   
│  
│―rtc.conf  

* MultiTypeConsoleIn.py  
RTC本体です  
* csvreader.py   
CSVファイルの読み込みを行なっています
* consolein.ini  
データポートの型や読み込むCSVファイルの設定をすることができます
* rtc.conf  
ポートの設定や動作周期を設定できます

注:本RTCにおいてユーザーが操作すると想定しているファイルのみ説明しています  

RTCの構成
------  
<img src="http://cloud.github.com/downloads/HiroakiMatsuda/MultiTypeConsoleIn/readme_01.png" width="400px" />    
任意のデータ型でデータを受け取り、それをCSVファイルに書き出すことができます  
ファイルの設定はiniファイルを通して行えるので、簡単に設定を変えられます  
iniファイルの設定はInitialize時に読み込むので、設定を変更した場合はRTCを再起動してください  

* data port :OutPort データ型; 任意のデータ型  

TimedXXX型の場合  
[x1]  
1つの指定した型のデータ  

TimedXXXSeq型の場合  
[x1, x2, ..... xN]  
指定した型のN個のデータ

使い方
------
###1. 使用するデータ型を設定する###
1. consolein.iniをテキストエディタなどで開き編集します  
   ```mode = XXX```  
XXXの部分を編集してください。コンソールモードか、CSVモードか選択します  
  ・console: consoleinのような使い方でデータ入力が可能です  
  ・csv: CSVファイルからデータを読み込み送信できます  

   ```num = X```  
Xに一回に送信するデータの数を指定します  
Seq型のデータ型のみ有効な設定です  
例えば4と入力すると[x1, x2, x3, x4]のように4つの連続したデータを送信します  

   ```type = XXX```  
XXXの部分を編集してください。現在対応している型は以下の通りです  
 ・TimedShort  
 ・TimedUShort  
 ・TimedLong  
 ・TimedULong  
 ・TimedFloat  
 ・TimedDouble  
 ・TimedString  
 ・TimedWString  
 ・TimedChar  
 ・TimedWChar  
 ・TimedBool  
 ・TimedOctet  
 ・TimedShortSeq  
 ・TimedUShortSeq  
 ・TimedLongSeq  
 ・TimedULongSeq  
 ・TimedFloatSeq  
 ・TimedDoubleSeq  
 ・TimedStringSeq  
 ・TimedWStringSeq  
 ・TimedCharSeq  
 ・TimedWCharSeq  
 ・TimedOctetSeq  
 ・TimedBoolSeq	  

 注:内部処理における型は以下のようにキャストされています  
 int:  
Short, Long, Octet  
float:  
Float, Double  
str:  
Char, String  
bool:  
Bool  

2. CSVファイルの設定  
   ```delimiter = X   ```  
Xに以下のデリミターから選択し入力してください  
読み込むCSVファイルに合わせて適切なデリミターを設定してください  
・,  
・  (半角スペース)  
・&    

   ``'data_type = XXX   ```  
CSVファイルのデータ型を指定します  
現在対応している型は以下の通りです  
 ・short  
 ・long  
 ・float  
 ・double  
 ・string  
 ・char  
 ・octet  
 ・bool    
 注:内部処理における型は以下のようにキャストされています  
int:  
short, long, octet  
float:  
float, double  
str:  
char, string  
bool:  
bool  

   ```wait = X   ```  
CSVデータ送信時に一行ごとの待ち時間X [msec]を設定します  

   ```loop = X   ```  
CSVデータ送信の繰り返し回数Xを設定します  

   ```csvfilenum = X   ```  
CSVデータはファイルパスを事前に登録する必要があります  
その登録するCSVファイル数Xを設定します  
 
 以下の作業は登録するCSVファイル数だけ繰り返し編集してください  
4つのサーボモータを使用する場合は、連続した値でcsv_4まで指定してください   
  
   ```csv_1 = XXX   ```  

 XXXにはファイルパスを指定します  
サンプルファイルはcsvフォルダ内に入っています  
例：csv_1 = csv\test1.csv  

  
###2. コンソールからデータを出力する###
1. MultiTypeConsoleIn.py起動する  
ダブルクリックするなどして起動してください  
2. データを入力する  
[MultiTypeConsoleOut][cout]などの適当なデータを表示できるRTCを使用してデータを確認します  
データが入力されると入力されたデータがコンソールに表示され出力されます   
例ではTimedLong型のデータを送信しています  
<img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsolein/readme_02.png" width="400px" />  

[cout]: https://github.com/HiroakiMatsuda/MultiTypeConsoleOut

###3. コンソールからSeq型のデータを出力する###
1. MultiTypeConsoleIn.py起動する  
ダブルクリックするなどして起動してください  
2. データを入力する  
[MultiTypeConsoleOut][cout]などの適当なデータを表示できるRTCを使用してデータを確認します  
データが入力されると入力されたデータがコンソールに表示され出力されます   
例ではTimedLongSeq型のデータを送信しています  
4個データ列を送信する場合は、４回続けて入力を行います  
<img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsolein/readme_03.png" width="400px" />  

[cout]: https://github.com/HiroakiMatsuda/MultiTypeConsoleOut

###4. CSVファイルからデータを出力する###
1. MultiTypeConsoleIn.py起動する  
ダブルクリックするなどして起動してください  

2. CSVファイル名を指定する    
入力するCSVファイル名はconsolein.iniに登録したcsv_Xの名前です  

 １番のCSVファイルを送信する場合はcsv_1と入力します   
  
 <img src="https://github.com/downloads/HiroakiMatsuda/MultiTypeConsoleIn/readme_04.png" width="400px" />  


以上が本RTCの使い方となります  

ライセンス
----------
Copyright &copy; 2012 Hiroaki Matsuda  
Licensed under the [Apache License, Version 2.0][Apache]  
Distributed under the [MIT License][mit].  
Dual licensed under the [MIT license][MIT] and [GPL license][GPL].  
 
[Apache]: http://www.apache.org/licenses/LICENSE-2.0
[MIT]: http://www.opensource.org/licenses/mit-license.php
[GPL]: http://www.gnu.org/licenses/gpl.html