from pathlib import Path
import hashlib
import json
import re
from docx import Document
from docx.oxml.ns import qn

root = Path.cwd()
reference = json.loads((root/'references/参考模板-转换校验.json').read_text(encoding='utf-8'))
source = Path(r'E:\windows\xwechat_files\wxid_1f569vap2wed22_4a14\temp\RWTemp\2026-10\d2b046a03378019223cdfb7e936d25db\任务目标1：AI基础认知与Agent实操（名词学习+常见Agent对比安装+个人网站搭建）实验.docx')
assert hashlib.sha256(source.read_bytes()).hexdigest() == reference['source_sha256']
md = (root/'deliverables/Java基础巩固到SpringBoot教学目标方案.md').read_text(encoding='utf-8-sig')
assert len(re.findall(r'^## ', md, re.M)) == 8
assert '12周路线的验收映射' in md
assert '关卡C移到第12周' in md
assert '不要求商品类、集合、价格、数据库、Maven或新语法' in md
assert '\ufffd' not in md
word = Document(root/'deliverables/Java基础巩固到SpringBoot教学目标方案.docx')
for table in word.tables:
    assert table.rows[0]._tr.get_or_add_trPr().find(qn('w:tblHeader')) is not None
    for row in table.rows:
        assert row._tr.get_or_add_trPr().find(qn('w:cantSplit')) is not None
notes = '''# 交付检查记录

- 原Word转Markdown：50个非空正文段落与3张表格均已保留；源文件SHA-256未变，原件未改。
- 教学方案：沿用参考文档8个栏目，包含16周讨论路线、第一周步骤与9项自测、12周降载及对应验收口径。
- 读者检查：已检查学生起点、周次未确认、时间合计、AI限制、个人关卡和栏目完整性；补齐12周B/C关卡映射。
- Markdown转Word：全文文字保留；8个一级栏目与11张表格；OOXML和ZIP结构有效；表头重复和整行跨页控制已设置。
- 第一周时长：75+60+75+60+60+30=360分钟=6小时。
- 限制：尚未用Word或其他排版引擎渲染实际页面；不声称页面视觉复核完成。具体版本、课时和日期仍需教师确认。
'''
(root/'deliverables/交付检查记录.md').write_text(notes, encoding='utf-8')
print('Reference unchanged; 8 sections; 11 tables; timing and 12-week gate mapping verified.')
