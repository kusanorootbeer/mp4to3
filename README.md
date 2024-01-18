# mp4to3
It transform mp4 file into mp3 file.

## Option: 
It make exe file to execute for w/out python environment.
You can distribute mp4to3.exe

# Setup
```bash
pip install -r requirements.txt
```
or
```bash
pip install pyinstaller moviepy
```


# Usage1: Simple transform.
```bash
python mp4to3.py hoge.mp4
```
It makes ```hoge.mp3```

# Usage2: Make exe file which transfom mp4 file to mp3 file.
```bash
pyinstaller mp4to3.py --onefile
```
Then you can find ```./dist/mp4to3.exe```  
You execute mp4 file by mp4to3.exe like below.
The mp4 file be transformed into mp3.

![img](https://github.com/kusanorootbeer/mp4to3/blob/image/image/img.png) 
![img](https://github.com/kusanorootbeer/mp4to3/blob/image/image/img2.png)

Then you can make mp3 file.

# Post Script
弊社に社内利用専用の生成AIサービスが公開されたので使ってみよう思いました．  
文字起こし機能を使いたかったのですが，音声(wav,mp3ファイル)でないとテキスト変換してくれないので動画(mp4ファイル)を音声に変換するプログラムを作りました．  

