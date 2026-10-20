from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table
from zipfile import ZipFile
import hashlib
import json
import re

SOURCE = Path(r'E:\windows\xwechat_files\wxid_1f569vap2wed22_4a14\temp\RWTemp\2026-10\d2b046a03378019223cdfb7e936d25db\任务目标1：AI基础认知与Agent实操（名词学习+常见Agent对比安装+个人网站搭建）实验.docx')
OUTPUT = Path('references/参考模板-AI基础认知与Agent实操.md')

def escape_cell(text):
    return text.replace('\\', '\\\\').replace('|', '\\|').replace('\n', '<br>')

def convert():
    doc = Document(SOURCE)
    lines = []
    source_texts = []
    tables = 0
    paragraphs = 0
    for child in doc.element.body.iterchildren():
        if child.tag == qn('w:p'):
            p = Paragraph(child, doc)
            text = p.text.strip()
            if not text:
                continue
            paragraphs += 1
            source_texts.append(text)
            if paragraphs == 1:
                lines.extend(['# ' + text, '', '> 转换说明：按原文顺序保留正文与表格；只做 Markdown 排版，不核实或改写原文技术表述。原文件未修改。', ''])
            elif re.match(r'^[一二三四五六七八九十]+、', text):
                lines.extend(['## ' + text, ''])
            else:
                formatted = re.sub(r'^(\d+)\.(?!\s)', r'\1. ', text)
                lines.extend([formatted, ''])
        elif child.tag == qn('w:tbl'):
            table = Table(child, doc)
            rows = [[cell.text.strip() for cell in row.cells] for row in table.rows]
            if not rows:
                continue
            tables += 1
            width = max(map(len, rows))
            rows = [row + [''] * (width-len(row)) for row in rows]
            for row in rows:
                source_texts.extend(t for t in row if t)
            lines.append('| ' + ' | '.join(escape_cell(t) for t in rows[0]) + ' |')
            lines.append('| ' + ' | '.join(['---'] * width) + ' |')
            for row in rows[1:]:
                lines.append('| ' + ' | '.join(escape_cell(t) for t in row) + ' |')
            lines.append('')
    md = '\n'.join(lines).rstrip() + '\n'
    OUTPUT.write_text(md, encoding='utf-8')
    normalized_md = re.sub(r'(\d+)\.\s+', r'\1.', md).replace('<br>', '\n').replace('\\|', '|').replace('\\\\', '\\')
    missing = [t for t in source_texts if t not in normalized_md]
    with ZipFile(SOURCE) as archive:
        media = [n for n in archive.namelist() if n.startswith('word/media/')]
    assert not missing, f'Missing source text: {missing}'
    assert not media, 'This reference contains media requiring separate extraction.'
    report = {
        'source_filename': SOURCE.name,
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'output': str(OUTPUT),
        'nonempty_paragraphs': paragraphs,
        'tables_preserved': tables,
        'source_media_count': len(media),
        'all_source_text_preserved': not missing,
        'source_untouched': True,
    }
    Path('references/参考模板-转换校验.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    convert()
