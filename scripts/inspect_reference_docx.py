from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
import json
from zipfile import ZipFile

source = Path(r'E:\windows\xwechat_files\wxid_1f569vap2wed22_4a14\temp\RWTemp\2026-10\d2b046a03378019223cdfb7e936d25db\任务目标1：AI基础认知与Agent实操（名词学习+常见Agent对比安装+个人网站搭建）实验.docx')
doc = Document(source)
blocks = []
for child in doc.element.body.iterchildren():
    if child.tag == qn('w:p'):
        p = Paragraph(child, doc)
        if p.text.strip():
            blocks.append({'kind': 'paragraph', 'style': p.style.name, 'text': p.text,
                           'numbered': p._p.find(qn('w:pPr')) is not None and p._p.find(qn('w:pPr')).find(qn('w:numPr')) is not None})
    elif child.tag == qn('w:tbl'):
        t = Table(child, doc)
        blocks.append({'kind': 'table', 'rows': [[c.text for c in row.cells] for row in t.rows]})
with ZipFile(source) as z:
    media = [n for n in z.namelist() if n.startswith('word/media/')]
info = {'source': str(source), 'blocks': blocks, 'media': media,
        'section_count': len(doc.sections), 'table_count': len(doc.tables)}
Path('references/参考实验文档-结构.json').write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(info, ensure_ascii=False, indent=2))
