# Manual ForumCE Bridge — macOS fallback

Use this only if ForumCE Connect cannot run on your Mac. The normal ForumCE Connect app is easier and is the recommended setup.

## 1. Download the manual bridge

Open the latest ForumCE release and download:

`ForumCE-Bridge-macOS-v1.0.zip`

Extract the ZIP and open Terminal in that folder.

## 2. Set it up once

Run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 bridge.py
```

The first run asks for your ForumCE username and password. The bridge saves a local ForumCE login token in `.forumce_token` so you do not need to enter your password every time.

## 3. Connect the calculator

1. Connect the TI-84 Plus CE by USB.
2. Run ForumCE on the calculator.
3. Leave the Terminal window open while using ForumCE.

Stop the bridge with:

```text
Control + C
```

## Start it again later

From the same folder:

```bash
source .venv/bin/activate
python3 bridge.py
```

## Reset the saved login

```bash
rm .forumce_token
python3 bridge.py
```

## Problems

**`python3: command not found`** — install Python 3 for macOS, then retry.

**Calculator never connects** — make sure ForumCE is actually running on the calculator. The ForumCE USB serial connection appears while the calculator program is running.

**Server offline** — check your internet connection and verify `https://api.forumce.com/health` opens in a browser.
