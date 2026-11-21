"""Quick competitor analysis tool: generates a Yes/No/Note marking form (static HTML).

Usage:
  python -I -X utf8 scripts/make_quick_form.py <input.json> <output.html>
input.json:
{
  "title": "Channel name: quick analysis",
  "summary": ["line 1", "line 2", "..."],
  "items": [
    {"id": "R1", "title": "Short rule", "description": "mechanism and the video where it was seen", "suggestion": "Yes"},
    ...
  ]
}
Output: a single-file HTML (light/dark theme, phone friendly). Every row has Yes/No buttons and a note box;
at the bottom is 'Copy result' (plain text to the clipboard: "1) Title: Yes | NOTE: ..."). Choices stay in the
browser (localStorage). Then publish the HTML file as a shareable page (the <title> must sit within the first 8 KB;
this template does).
"""
import sys, json, html

if len(sys.argv) < 3:
    print(__doc__); sys.exit(1)
d = json.load(open(sys.argv[1], encoding="utf-8"))
title = d.get("title", "Quick analysis")
summary = d.get("summary", [])
items = d.get("items", [])
key = "quick_form_" + "".join(c for c in title.lower() if c.isalnum())[:30]

tpl = """<title>__TITLE__</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
/* Layout: single column; every row is one decision (Yes/No + note); a copyable result at the bottom. */
:root{--bg:#f6f4f7;--surface:#fff;--fg:#241f2b;--muted:#6b6475;--line:#e2dde8;--accent:#8a4f6b;--accent-fg:#fff;--ok:#2f7a55;--no:#a23a3a;
--font:system-ui,-apple-system,'Segoe UI',sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17141b;--surface:#211d27;--fg:#efeaf3;--muted:#a59cb0;--line:#372f40;--accent:#d08aa9;--accent-fg:#1a1220;--ok:#6cc99a;--no:#e48a8a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#17141b;--surface:#211d27;--fg:#efeaf3;--muted:#a59cb0;--line:#372f40;--accent:#d08aa9;--accent-fg:#1a1220;--ok:#6cc99a;--no:#e48a8a;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--font);font-size:15px;line-height:1.5;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:20px 120px}
.wrap{max-width:760px;margin:0 auto}h1{font-size:24px;line-height:1.2;margin:0 0 10px}.summary{color:var(--muted);margin:0 0 16px;padding-left:18px}
.row{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin-bottom:10px;display:flex;flex-direction:column;gap:10px}
.t{font-weight:600}.d{color:var(--muted);font-size:13px;margin-top:2px}.rec{font-size:13px;color:var(--accent);margin-top:4px}
.opts{display:flex;gap:8px}.opts button{font:inherit;padding:8px 18px;border-radius:8px;border:1px solid var(--line);background:var(--bg);color:var(--fg);cursor:pointer;min-height:40px}
.opts button.yes[aria-pressed="true"]{background:var(--ok);border-color:var(--ok);color:var(--surface);font-weight:600}
.opts button.no[aria-pressed="true"]{background:var(--no);border-color:var(--no);color:var(--surface);font-weight:600}
textarea{width:100%;box-sizing:border-box;font:inherit;font-size:14px;background:var(--bg);color:var(--fg);border:1px solid var(--line);border-radius:8px;padding:8px;min-height:44px;resize:vertical}
.out{min-height:200px;font-family:ui-monospace,Consolas,monospace;font-size:13px;background:var(--surface)}
.bar{position:fixed;left:0;right:0;bottom:0;background:var(--surface);border-top:1px solid var(--line);padding:10px max(16px,env(safe-area-inset-right,0px)) calc(10px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));display:flex;align-items:center;gap:12px;justify-content:space-between}
.copy{font:inherit;font-weight:600;padding:9px 16px;border-radius:8px;border:0;background:var(--accent);color:var(--accent-fg);cursor:pointer;min-height:40px}
.msg{font-size:13px;color:var(--accent);min-height:18px}button:focus-visible,textarea:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
</style>
<div class="wrap"><h1>__TITLE__</h1><ul class="summary">__SUMMARY__</ul><div id="list"></div>
<h2>Result</h2><textarea id="out" class="out" readonly aria-label="Result text"></textarea><div class="msg" id="msg" role="status"></div></div>
<div class="bar"><span id="count">0 / 0</span><button class="copy" id="copyBtn" type="button">Copy result</button></div>
<script>
const G=__ITEMS__;const KEY="__KEY__";let S={},N={};
try{const x=JSON.parse(localStorage.getItem(KEY)||"{}");S=x.S||{};N=x.N||{}}catch(e){}
function save(){try{localStorage.setItem(KEY,JSON.stringify({S,N}))}catch(e){}}
G.forEach(it=>{const r=document.createElement("div");r.className="row";const h=document.createElement("div");
h.innerHTML='<div class="t"></div><div class="d"></div><div class="rec"></div>';h.children[0].textContent=it.title;h.children[1].textContent=it.description||"";h.children[2].textContent=it.suggestion?("My suggestion: "+it.suggestion):"";
const o=document.createElement("div");o.className="opts";[["Yes","yes"],["No","no"]].forEach(([l,c])=>{const b=document.createElement("button");b.type="button";b.textContent=l;b.classList.add(c);b.dataset.id=it.id;b.dataset.l=l;b.onclick=()=>{S[it.id]=S[it.id]===l?undefined:l;save();paint()};o.appendChild(b)});
const n=document.createElement("textarea");n.placeholder="Note (optional)";n.value=N[it.id]||"";n.oninput=()=>{N[it.id]=n.value;save();paint()};
r.append(h,o,n);document.getElementById("list").appendChild(r)});
function paint(){document.querySelectorAll(".opts button").forEach(b=>b.setAttribute("aria-pressed",S[b.dataset.id]===b.dataset.l?"true":"false"));
document.getElementById("count").textContent=G.filter(x=>S[x.id]).length+" / "+G.length+" answered";
let t=document.title.toUpperCase()+"\\n\\n";G.forEach((x,k)=>{t+=(k+1)+") "+x.title+": "+(S[x.id]||"NOT ANSWERED")+(N[x.id]?"  | NOTE: "+N[x.id].replace(/\\n/g," "):"")+"\\n"});document.getElementById("out").value=t}
paint();
document.getElementById("copyBtn").onclick=async()=>{const ta=document.getElementById("out"),m=document.getElementById("msg");
try{await navigator.clipboard.writeText(ta.value);m.textContent="Copied. Now paste it into the chat."}catch(e){ta.removeAttribute("readonly");ta.focus();ta.select();m.textContent="Text selected, press Ctrl+C to copy.";ta.setAttribute("readonly","")}};
</script>
"""
out = (tpl.replace("__TITLE__", html.escape(title))
          .replace("__SUMMARY__", "".join("<li>%s</li>" % html.escape(x) for x in summary))
          .replace("__ITEMS__", json.dumps(items, ensure_ascii=False).replace("</", "<\\/"))
          .replace("__KEY__", key))
open(sys.argv[2], "w", encoding="utf-8").write(out)
print("written:", sys.argv[2], len(out), "bytes,", len(items), "items")
