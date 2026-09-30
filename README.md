[README.md](https://github.com/user-attachments/files/32857947/README.md)
# vrc-photo

VRChatで撮った写真を、自動でDiscordに送信するPythonスクリプトです。

## 必要なもの

- Windows
- Python 3.9 以上
- Discordのwebhook URL

## セットアップ

1. このリポジトリをダウンロード（またはclone）する
2. 必要なライブラリを入れる
   ```
   pip install -r requirements.txt
   ```
3. `webhook.example.txt` をコピーして `webhook.txt` にリネームし、中身をあなたのwebhook URLに書き換える
4. 画像フォルダのパスが違う場合は `vrc-photo.py` 内の設定を変更する
   （VRChatの写真は通常 `ピクチャ\VRChat` に保存されます。OneDriveを使っている場合などで場所が違うときは、`vrc-photo.py` の `PHOTO_FOLDER` を書き換えてください）

### webhook URLの作り方

Discordのサーバー設定 → 連携サービス → ウェブフック → 「新しいウェブフック」→ URLをコピー

## 使い方

```
python vrc-photo.py
```

起動したままVRChatで写真を撮ると、自動でDiscordに送信されます。

## 自動起動（任意）

1. `Win + R` → `shell:startup` でスタートアップフォルダを開く
2. `start-vrc-photo.bat` のショートカットをそこに入れる

PC起動時にバックグラウンドで自動的に動きます。

## 注意

- `webhook.txt` は **絶対に公開しないでください**（`.gitignore` 済み）。URLが漏れた場合はDiscordでwebhookを削除して作り直してください。
- 送信した写真にはワールドやフレンドが写っていることがあります。送信先チャンネルには注意してください。

## ライセンス

MIT License
