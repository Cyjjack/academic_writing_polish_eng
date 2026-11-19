from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E
import json,hashlib,collections,re
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
def inspect(p):
    with ZipFile(p) as z:
        root=E.fromstring(z.read('word/document.xml'))
        com={}
        if 'word/comments.xml' in z.namelist():
            for c in E.fromstring(z.read('word/comments.xml')):
                com[c.get(W+'id')]={'author':c.get(W+'author'),'date':c.get(W+'date'),'text':''.join(n.text or '' for n in c.iter(W+'t')),'anchor':''}
        pars=[]; active=set()
        for para in root.iter(W+'p'):
            old=[];new=[];ed=[];ids=set(active)
            def walk(n,kind='normal'):
                tag=n.tag.split('}')[-1]
                if tag in ('ins','del','moveFrom','moveTo'):
                    kind=tag
                    ed.append([kind,n.get(W+'author'),n.get(W+'date'),''.join(x.text or '' for x in n.iter() if x.tag in (W+'t',W+'delText'))])
                if tag in ('commentRangeStart','commentRangeEnd','commentReference'):
                    cid=n.get(W+'id');ids.add(cid)
                    if tag=='commentRangeStart':active.add(cid)
                    if tag=='commentRangeEnd':active.discard(cid)
                if tag in ('t','delText'):
                    t=n.text or ''
                    if kind not in ('ins','moveTo'):old.append(t)
                    if kind not in ('del','moveFrom'):new.append(t)
                    for cid in active:
                        if cid in com:com[cid]['anchor']+=t
                for child in n:walk(child,kind)
            walk(para)
            pars.append(dict(before=''.join(old),after=''.join(new),edits=ed,comments=sorted(ids)))
        return dict(file=p.name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),parts=[n for n in z.namelist() if 'comment' in n.lower()],comments=com,paragraphs=pars)
if __name__=='__main__':
    out=Path('revision-study');out.mkdir(exist_ok=True)
    for p in sorted(Path('.').glob('*.docx')):
        d=inspect(p);(out/(p.stem+'.json')).write_text(json.dumps(d,ensure_ascii=False),encoding='utf8')
        print(p.name,[(i,a['after'][:110]) for i,a in enumerate(d['paragraphs'][:4])],len(d['comments']),collections.Counter(e[1] for a in d['paragraphs'] for e in a['edits']))
