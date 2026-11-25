# -*- coding: utf-8 -*-
"""Capture et recadre le coin bas-gauche (compteur + zone jump + bouton TOC)."""
import io
import os
import subprocess
import sys

from PIL import Image

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\counter_check.html"
OUT = r"C:\ppt\_check\render\counter.png"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""


def main():
    html = open(SRC, encoding="utf-8").read()
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", "--window-size=1600,900",
                    "--virtual-time-budget=6000", "--screenshot=" + OUT,
                    "file:///C:/ppt/_check/counter_check.html"],
                   capture_output=True, timeout=90)
    im = Image.open(OUT)
    im.crop((0, im.height - 130, 560, im.height)).save(OUT)
    print("OK ->", OUT, Image.open(OUT).size)


if __name__ == "__main__":
    main()
