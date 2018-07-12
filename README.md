# 使い方

- 1 .envの作成

docker-composeが使う.envの作成を行います。

.envは.env.sampleをコピーして以下の内容で作成してください。

```
SLACK_WEBHOOK="<slackのwebhookのURL>"
MATTERMOST_WEBHOOK="<mattermostのwebhookのURL>"
```

webhookを利用しない場合は空文字列を指定してください。

- 2 cronの設定

`scrapy/cron`にサンプルが置いてあります。このままでも動きますが、必要に応じて編集してください。

- 3 起動

```
# プロキシのない環境用
docker-compose up -d

# プロキシ環境
docker-compose up -f docker-compose-proxy.yml -d
```


















