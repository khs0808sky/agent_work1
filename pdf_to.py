import pymupdf
import os

#pdf_file_path = './data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf'
pdf_file_path = './data/K-CON+LA+2022로+본+미국+내+K-Pop+현황+[미국22-06호].pdf'

doc = pymupdf.open(pdf_file_path)

full_text = ''

for page in doc:
    text = page.get_text()
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)
pdf_file_name = os.path.splitext(pdf_file_name)[0]

text_file_path = f"output/{pdf_file_name}.txt"
with open(text_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)