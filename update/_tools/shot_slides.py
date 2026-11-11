# -*- coding: utf-8 -*-
"""Capture PNG du rendu HTML pour verification visuelle.

Cree _check/shot.html (copie de index.html + saut vers location.hash),
puis capture chaque slide demandee via Chrome headless.

Usage : python shot_slides.py 101 102 113 ...
"""
import os
import re
import io
import sys
import shutil
import subprocess

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\shot.html"
OUTDIR = r"C:\ppt\_check\render"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""

INJECT = r"""
<script>/* shot: saut vers #N */
(function(){
  const m = location.hash.match(/\d+/);
  if(m){ const n = parseInt(m[0],10)-1; const iv = setInterval(()=>{
    try{ if(typeof go==='function'){ go(n); clearInterval(iv);} }catch(e){}
  }, 30); setTimeout(()=>clearInterval(iv), 3000); }
})();
</script>
</body>"""

def main():
    html = open(SRC, encoding="utf-8").read()
    assert "</body>" in html
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    html = html.replace("</body>", INJECT, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)

    os.makedirs(OUTDIR, exist_ok=True)
    for n in sys.argv[1:]:
        out = os.path.join(OUTDIR, "slide%s.png" % n)
        url = "file:///C:/ppt/_check/shot.html#%s" % n
        subprocess.run([CHROME,
                        "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=1",
                        "--window-size=1600,900",
                        "--virtual-time-budget=9000",
                        "--screenshot=" + out, url],
                       capture_output=True, timeout=90)
        ok = os.path.exists(out) and os.path.getsize(out) > 5000
        print(("OK  " if ok else "FAIL") + " slide%s -> %s" % (n, out))

if __name__ == "__main__":
    main()
