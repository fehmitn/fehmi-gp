# -*- coding: utf-8 -*-
"""Capture PNG du panneau Table des matieres ouvert, pour verification visuelle."""
import io
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\toc_check.html"
OUT = r"C:\ppt\_check\render\toc_open.png"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""
INJECT = r"""
<script>(function(){
  var iv=setInterval(function(){
    try{ if(typeof openToc==='function'){ openToc(); clearInterval(iv);} }catch(e){}
  },30); setTimeout(function(){clearInterval(iv);},3000);
})();</script>
</body>"""


def main():
    html = open(SRC, encoding="utf-8").read()
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    html = html.replace("</body>", INJECT, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1600,900",
                    "--virtual-time-budget=9000", "--screenshot=" + OUT,
                    "file:///C:/ppt/_check/toc_check.html"],
                   capture_output=True, timeout=90)
    ok = os.path.exists(OUT) and os.path.getsize(OUT) > 5000
    print(("OK  " if ok else "FAIL") + " -> " + OUT)


if __name__ == "__main__":
    main()
