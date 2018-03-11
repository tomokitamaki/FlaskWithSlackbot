# 概要
slackBOTにメンションで話しかけるとそれに応じた返信をしてくれる。
- tenki と話しかける  
明日と明後日の天気とそれぞれの最高気温,最低気温を教えてくれる。
- どこ と話しかける  
家に置いてあるよく忘れがちなものの場所を教えてくれる。  
https://qiita.com/txt_only/items/9e28ec815d487d36865e

# どうしてFlaskも使うの？
slackbotのモジュールだけでもできるけど、  
flaskも使った方がslackを介さなくても使えるものができるので  
便利いいかなぁって思ったからです。  
今の天気とかならあれだけど、例えばredmineにチケットを作るとか  
redashから取得した情報をどうこうするとかそういった事をする場合、  
slackを介さないでもできた方がなんか潰しが効きそうだなぁって感じ。

# 使いかた
## 前提条件
- Dockerがインストールされている  
```
$ docker -v
Docker version 17.12.0-ce, build c97c6d6
```
- docker-composeがインストールされている  
```
$ docker-compose -v
docker-compose version 1.18.0, build 8dd22a9
```
- git が使える  
```
$ git --version
git version 2.14.3 (Apple Git-98)
```
- slackbotのAPIキーを用意しておく  
https://qiita.com/ykhirao/items/3b19ee6a1458cfb4ba21

## 使いかた
1. このリポジトリをgit clone する  
`https://github.com/tomokitamaki/FlaskWithSlackbot.git`
2. APIトークンが書かれたファイルを作る。  
`FlaskWithSlackbot/slackbotroot_dir/slackbotdir` に slack_APITOKEN.py というファイル名でファイルを作る。  
内容は `API_TOKEN = "APIトークン"` という感じ。  
```
ex) API_TOKEN = "asdfghjklqwertyuiozxcvbnm"
```
3. buildする  
コンテナで使用するイメージをbuildする  
```
docker-compose -f dockercompose_slackbotwith_Flask.yml build
```
4. upする  
コンテナを起動させる。  
```
docker-compose -f dockercompose_slackbotwith_Flask.yml up -d
```
5. slackでbotに話しかける。  
メンション付きで話しかける。  
```
@bot名 tenki
```
