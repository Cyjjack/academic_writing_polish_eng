from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
from xml.etree import ElementTree
import sys,json,re,logging
from pypdf import PdfReader
logging.getLogger("pypdf").setLevel(logging.ERROR)
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path("author_papers") if Path("author_papers").is_dir() else Path(".")
cache=Path("author-corpus-cache")
cache.mkdir(exist_ok=True)
for p in sorted(root.iterdir()):
    ext=p.suffix.lower()
    if ext not in (".pdf",".md",".txt",".docx"): continue
    digest=sha256(p.read_bytes()).hexdigest()
    dest=cache/(digest+".json")
    if not dest.exists():
        if ext==".pdf":
            reader=PdfReader(p)
            pages=[page.extract_text() for page in reader.pages]
        elif ext==".docx":
            with ZipFile(p) as z:
                tree=ElementTree.fromstring(z.read("word/document.xml"))
                pages=["\n".join("".join(n.itertext()) for n in tree.findall(".//{*}p"))]
        else: pages=[p.read_text(encoding="utf-8-sig")]
        tmp=dest.with_suffix(".tmp")
        tmp.write_text(json.dumps(pages,ensure_ascii=False),encoding="utf-8")
        tmp.replace(dest)
    print(digest[:12],p.name)
