# -*- coding: utf-8 -*-
"""Capture le verso d'une carte de quiz apres clic.
Usage: python shot_quiz_back.py SLIDE INDEX (1-based)
"""
import io
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
SLIDE = int(sys.argv[1]) if len(sys.argv) > 1 else 100
IDX = int(sys.argv[2]) if len(sys.argv) > 2 else 4
SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\quiz_back.html"
OUT = r"C:\ppt\_check\render\quiz_back_%d_%d.png" % (SLIDE, IDX)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""
INJECT = """
<script>(function(){
  var iv=setInterval(function(){
    try{
      if(typeof go!=='function') return;
      go(%d);
      var s=document.querySelectorAll('.slide')[%d];
      var it=s.querySelectorAll('.quiz-item')[%d];
      it.querySelector('.quiz-front').click();
      it.querySelector('[data-ok="1"]').click();
      clearInterval(iv);
    }catch(e){}
  },30); setTimeout(function(){clearInterval(iv);},3000);
})();</script>
</body>""" % (SLIDE - 1, SLIDE - 1, IDX - 1)


def main():
    html = open(SRC, encoding="utf-8").read()
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    html = html.replace("</body>", INJECT, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1600,900",
                    "--virtual-time-budget=9000", "--screenshot=" + OUT,
                    "file:///C:/ppt/_check/quiz_back.html"],
                   capture_output=True, timeout=90)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
