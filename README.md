# ForumCE

**ForumCE brings online forums, messages, profiles, follows, notifications, and more to the TI-84 Plus CE.**

Website: https://forumce.com  
Latest release: [ForumCE v1.1.0](../../releases/latest)

## Supported computers

ForumCE Connect v1.1.0 supports:

- macOS — Apple Silicon
- macOS — Intel
- Windows 10/11 — x64

Packaged builds include Python and their required dependencies. Users do not need to install Python separately.

## What you need

- TI-84 Plus CE
- USB data cable
- [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw)
- ForumCE account
- arTIfiCE + CE Libraries on the calculator

## Install ForumCE

### 1. Install ForumCE Connect

Open the [latest release](../../releases/latest) and download the build for your computer:

- `ForumCE-Connect-v1.1-macOS-Apple-Silicon.dmg`
- `ForumCE-Connect-v1.1-macOS-Intel.dmg`
- `ForumCE-Connect-v1.1.0-Windows-x64.exe`

On macOS, the app is currently ad-hoc signed, so you may need to right-click it and choose **Open** on first launch.

On Windows, SmartScreen may warn that the app is uncommon because it is not yet code-signed. Only choose **More info → Run anyway** for the executable downloaded from the official ForumCE release.

### 2. Install ForumCE on the calculator

Download/send all three calculator files together:

- `FORUMCE.8xp`
- `FORUMCE.8xp.0.8xv`
- `FORUMCE.8xp.1.8xv`

Use TI Connect CE to transfer them. Choose **Replace** if prompted.

### 3. Connect

1. Open ForumCE Connect and sign in.
2. Close TI Connect CE after file transfer.
3. Plug in the calculator.
4. Run ForumCE on the calculator.
5. Wait for **Server Online**, **Calculator Connected**, and **Bridge Running**.

## ForumCE v1.1.0

v1.1.0 adds Windows 10/11 x64 support to ForumCE Connect. The calculator client remains v1.0.0 because the calculator protocol did not need to change.

Windows support was verified with a physical TI-84 Plus CE, including forum loading, posts/replies, DMs, reactions/notifications, and USB reconnecting.

## Updating the calculator

ForumCE Connect checks the release channel, downloads the three calculator files, and verifies them with SHA-256 before installation through TI Connect CE.

## macOS manual bridge fallback

If the macOS app cannot be used, see [`manual/README.md`](manual/README.md) for the standalone Terminal bridge.

## Troubleshooting

**Calculator not detected:** Make sure ForumCE is running, close TI Connect CE after file transfer, reconnect the USB cable, and try another USB data port/cable.

**Missing CE library:** Follow the official CE Libraries installation instructions and verify the required library files were actually installed.

**Server offline:** Check your internet connection and https://forumce.com. The production API is `https://api.forumce.com`.

## Release metadata

`forumce-release.json` contains the calculator version, ForumCE Connect version, file sizes, and SHA-256 hashes used by ForumCE Connect.

Source project: https://github.com/Zytue67/ForumCE  
Contact: forumce.dev@gmail.com
