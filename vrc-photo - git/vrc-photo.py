from pathlib import Path
import time
import requests

# =========================
# 設定
# =========================

# VRChatの写真フォルダ（ユーザー名を自動取得）
PHOTO_FOLDER = Path.home() / "Pictures" / "VRChat"

# Webhook URLを別ファイルから読み込む
WEBHOOK_FILE = Path(__file__).with_name("webhook.txt")


def load_webhook():
    if not WEBHOOK_FILE.exists():
        raise FileNotFoundError(
            "webhook.txt が見つかりません。"
            "プログラムと同じフォルダに作成してください。"
        )

    url = WEBHOOK_FILE.read_text(encoding="utf-8").strip()

    if not url.startswith("https://discord.com/api/webhooks/"):
        raise ValueError("webhook.txt のURLを確認してください。")

    return url


# =========================
# Discordへ画像を送信
# =========================

def send_to_discord(image_path, webhook_url):
    try:
        with image_path.open("rb") as image:
            response = requests.post(
                webhook_url,
                files={"file": (image_path.name, image)},
                timeout=30,
            )

        if response.status_code in (200, 204):
            print(f"送信成功: {image_path.name}")
        else:
            print(f"送信失敗: HTTP {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"送信エラー: {image_path.name}: {e}")


# =========================
# 写真フォルダを監視
# =========================

def main():
    if not PHOTO_FOLDER.exists():
        raise FileNotFoundError(
            f"写真フォルダが見つかりません: {PHOTO_FOLDER}"
        )

    webhook_url = load_webhook()

    print("VRChat写真フォルダを監視しています...")
    print(PHOTO_FOLDER)

    # 起動時点ですでに存在する写真は送信しない
    known_files = {
        p for p in PHOTO_FOLDER.rglob("*")
        if p.is_file()
        and p.suffix.lower() in {".png", ".jpg", ".jpeg"}
    }

    print(f"現在の写真: {len(known_files)}枚")
    print("新しい写真を待っています...\n")

    while True:
        for image_path in PHOTO_FOLDER.rglob("*"):
            if not image_path.is_file():
                continue

            if image_path.suffix.lower() not in {
                ".png", ".jpg", ".jpeg"
            }:
                continue

            if image_path in known_files:
                continue

            # 写真の保存が進行中の場合に備えて待つ
            time.sleep(2)

            if not image_path.exists():
                continue

            send_to_discord(image_path, webhook_url)
            known_files.add(image_path)

        time.sleep(2)


if __name__ == "__main__":
    main()
    