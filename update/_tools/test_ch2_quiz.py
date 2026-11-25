# -*- coding: utf-8 -*-
"""Test fonctionnel des quiz 69/70 et de la TOC apres ajout des 2 slides."""
import io
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

SRC = r"C:\ppt\index.html"
SHOT = r"C:\ppt\_check\quiz_test.html"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

INJECT_HEAD = r"""<base href="file:///C:/ppt/">"""
INJECT = r"""
<script>(function(){
  var iv=setInterval(function(){
    try{
      if(typeof go!=='function') return;
      go(68);  /* slide 69 */
      var s=document.querySelectorAll('.slide')[68];
      var items=s.querySelectorAll('.quiz-item');
      var ok=s.querySelectorAll('[data-ok="1"]').length;
      var it=items[0];
      it.querySelector('.quiz-front').click();
      var flipped=it.classList.contains('flip');
      var opts=it.querySelectorAll('.q-opt');
      opts[0].click();           /* mauvaise reponse */
      var bad=opts[0].classList.contains('bad');
      var v1=it.querySelector('.q-verdict').textContent;
      opts[2].click();           /* bonne reponse */
      var good=opts[2].classList.contains('good');
      var v2=it.querySelector('.q-verdict').textContent;
      var def=it.querySelector('.q-def').classList.contains('show');

      var toc=document.querySelectorAll('.toc-item');
      toc[2].click();            /* chapitre 3 -> slide 71 (inchange) */
      var cur=document.getElementById('cur').textContent;

      var r=document.createElement('div'); r.id='TESTRESULT';
      r.textContent='ITEMS='+items.length+' OK='+ok+' FLIP='+flipped
        +' BAD='+bad+' V1='+v1+' GOOD='+good+' V2='+v2+' DEF='+def+' TOC='+cur;
      document.body.appendChild(r);
      clearInterval(iv);
    }catch(e){ document.title='ERR '+e.message; clearInterval(iv); }
  },30); setTimeout(function(){clearInterval(iv);},3000);
})();</script>
</body>"""


def main():
    html = open(SRC, encoding="utf-8").read()
    html = html.replace("<head>", "<head>" + INJECT_HEAD, 1)
    html = html.replace("</body>", INJECT, 1)
    open(SHOT, "w", encoding="utf-8", newline="\n").write(html)
    p = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                        "--virtual-time-budget=7000", "--dump-dom",
                        "file:///C:/ppt/_check/quiz_test.html"],
                       capture_output=True, timeout=90, text=True,
                       encoding="utf-8", errors="replace")
    m = re.search(r"ITEMS=(\d+) OK=(\d+) FLIP=(true|false) BAD=(true|false) V1=(.*?) GOOD=(true|false) V2=(.*?) DEF=(true|false) TOC=(\d+)", p.stdout)
    if not m:
        print("RESULTAT introuvable", p.stdout[-300:])
        return
    vals = m.groups()
    print("RESULTAT:", m.group(0))
    ok = (vals[0] == "6" and vals[1] == "6" and vals[2] == "true" and vals[3] == "true"
          and "❌" in vals[4] and vals[5] == "true" and "✅" in vals[6]
          and vals[7] == "true" and vals[8] == "71")
    print("OK" if ok else "ECHEC")


if __name__ == "__main__":
    main()
