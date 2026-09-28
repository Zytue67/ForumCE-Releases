# ForumCE v1.1.0 Installation Guide

## Fast setup

1. Install [TI Connect CE](https://education.ti.com/en/products/computer-software/ti-connect-ce-sw).
2. Open the [latest ForumCE release](../../releases/latest).
3. Download ForumCE Connect for your computer:
   - `ForumCE-Connect-v1.1-macOS-Apple-Silicon.dmg`
   - `ForumCE-Connect-v1.1-macOS-Intel.dmg`
   - `ForumCE-Connect-v1.1.0-Windows-x64.exe`
4. Download the three calculator files:
   - `FORUMCE.8xp`
   - `FORUMCE.8xp.0.8xv`
   - `FORUMCE.8xp.1.8xv`
5. Use TI Connect CE to send all three files to the TI-84 Plus CE.
6. Close TI Connect CE after the transfer.
7. Open ForumCE Connect and sign in.
8. Connect the calculator and run ForumCE.

ForumCE Connect should show **Server Online**, **Calculator Connected**, and **Bridge Running**.

## macOS first-launch warning

ForumCE Connect is currently ad-hoc signed. If macOS blocks it, right-click **ForumCE Connect**, choose **Open**, and confirm.

## Windows SmartScreen warning

The Windows build is not yet code-signed. Windows may say the app is uncommon or unknown. If you downloaded it from the official ForumCE release, choose **More info → Run anyway**.

No separate Python installation is required on macOS or Windows.

## Updating the calculator

1. Let ForumCE Connect download and verify the newest calculator files.
2. Close ForumCE on the calculator.
3. Click **Open Folder**.
4. Open TI Connect CE.
5. Send all three files.
6. Choose **Replace** if prompted.
7. Start ForumCE again.

Always transfer all three calculator files together.

## macOS manual Terminal fallback

If the Mac app still cannot be used, follow [`manual/README.md`](manual/README.md).
