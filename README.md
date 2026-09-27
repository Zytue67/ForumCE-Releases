# ForumCE

**ForumCE brings online forums, messages, profiles, follows, notifications, and more to the TI-84 Plus CE.**

Website: https://forumce.com  
Latest release: [ForumCE v1.0.0](../../releases/latest)

## What you need

- TI-84 Plus CE
- USB cable
- macOS computer
- [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw)
- ForumCE account

## Install ForumCE

### 1. Install ForumCE Connect

Open the [latest release](../../releases/latest), download `ForumCE-Connect-v1.0-macOS.dmg`, open it, and drag **ForumCE Connect** into Applications.

If macOS blocks the first launch, right-click **ForumCE Connect** and choose **Open**.

### 2. Install ForumCE on the calculator

For a first-time calculator install, download these three files from the same GitHub release:

- `FORUMCE.8xp`
- `FORUMCE.8xp.0.8xv`
- `FORUMCE.8xp.1.8xv`

Open TI Connect CE, connect the calculator, and send **all three files**.

### 3. Connect

1. Open ForumCE Connect.
2. Sign in.
3. Plug in the calculator.
4. Run ForumCE on the calculator.
5. Wait for ForumCE Connect to show:
   - **Server Online**
   - **Calculator Connected**
   - **Bridge Running**

That is it. ForumCE is online.

## Updating ForumCE

ForumCE Connect checks for calculator updates automatically.

When a new version is available:

1. Click **Download Calculator Update**.
2. Wait until ForumCE Connect says the files are verified.
3. Close ForumCE on the calculator.
4. Click **Open Folder**.
5. Click **TI Connect CE**.
6. Send all three ForumCE files to the calculator.
7. Choose **Replace** if TI Connect CE asks about existing copies.
8. Start ForumCE again.

ForumCE Connect verifies downloaded calculator files with SHA-256 before installation.

## If ForumCE Connect will not open

First try right-clicking the app and choosing **Open**. If you still cannot use the app, you can run the bridge manually from Terminal.

See [`manual/README.md`](manual/README.md) for the fallback instructions.

## Troubleshooting

**Calculator not detected:** ForumCE's USB connection appears while the ForumCE calculator program is running. Make sure ForumCE is open on the calculator and the USB cable supports data.

**TI Connect CE asks to replace files:** Choose **Replace** when updating ForumCE.

**ForumCE Connect says the server is offline:** Check your internet connection and try again. The production API is `https://api.forumce.com`.

**Need to reinstall the calculator app:** Download the three calculator files again and send all three with TI Connect CE.

## Release files

`forumce-release.json` contains the calculator version, required ForumCE Connect version, file sizes, and SHA-256 hashes used by ForumCE Connect.

The main ForumCE source repository is private. This repository is the public release and update channel.
