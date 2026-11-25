# -*- coding: utf-8 -*-
"""Test fonctionnel : clic sur une entree de la TOC -> bonne slide + panneau ferme."""
import io
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\toc_test.html"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""
INJECT = r"""
<script>(function(){
  var iv=setInterval(function(){
    try{
      if(typeof openToc!=='function') return;
      openToc();
      var items=document.querySelectorAll('.toc-item');
      items[5].click();  /* 6e entree -> slide 161 */
      clearInterval(iv);
      var r=document.createElement('div'); r.id='TESTRESULT';
      r.textContent='CUR='+document.getElementById('cur').textContent
                    +' OPEN='+document.getElementById('tocPanel').classList.contains('open')
                    +' ITEMS='+items.length;
      document.body.appendChild(r);
    }catch(e){}
  },30); setTimeout(function(){clearInterval(iv);},3000);
})();</script>
</body>"""


def main():
    html = open(SRC, encoding="utf-8").read()
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    html = html.replace("</body>", INJECT, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)
    p = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                        "--virtual-time-budget=6000", "--dump-dom",
                        "file:///C:/ppt/_check/toc_test.html"],
                       capture_output=True, timeout=90, text=True,
                       encoding="utf-8", errors="replace")
    m = re.search(r"CUR=(\d+) OPEN=(true|false) ITEMS=(\d+)", p.stdout)
    print("RESULTAT:", m.group(0) if m else "introuvable")
    if m:
        print("OK" if (m.group(1) == "161" and m.group(2) == "false" and m.group(3) == "8") else "ECHEC")


if __name__ == "__main__":
    main()
