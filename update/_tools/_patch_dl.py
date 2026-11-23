# -*- coding: utf-8 -*-
p = r"C:\ppt\update\_tools\download_chosen.py"
s = open(p, encoding="utf-8").read()
old = '''            req = urllib.request.Request(info["thumb"], headers=UA)
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            suffix = "" if idx == 0 else "_b"
            dst = os.path.join(OUT, f"bg_{theme}_online{suffix}.jpg")
            if os.path.exists(dst):
                print(f"{theme}{suffix}: deja present, ignore")
                # still credit? load from chosen.json? skip credit to avoid dup
                continue
            size = process(data, dst)
            print(f"{theme}{suffix}: {size} <- {entry['title']}")'''
new = '''            req = urllib.request.Request(info["thumb"], headers=UA)
            data = None
            for attempt in range(5):
                try:
                    with urllib.request.urlopen(req, timeout=180) as r:
                        data = r.read()
                    break
                except Exception as e:
                    if "429" in str(e):
                        wait = 20 * (attempt + 1)
                        print("   429 download -> attente " + str(wait) + "s")
                        import time as _t
                        _t.sleep(wait)
                        continue
                    raise
            if data is None:
                print("!! download impossible", entry["title"])
                continue
            suffix = "" if idx == 0 else "_b"
            dst = os.path.join(OUT, "bg_" + theme + "_online" + suffix + ".jpg")
            size = process(data, dst)
            print(theme + suffix + ": " + str(size) + " <- " + entry["title"])'''
assert old in s, "old block not found"
s = s.replace(old, new)
open(p, "w", encoding="utf-8").write(s)
print("patched")
PY