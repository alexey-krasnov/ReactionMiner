import os
import json
from os.path import join
from pathlib import Path
from pdf2text.generalParser import parseFile
from segmentation.segmentor import TopicSegmentor
from extraction.extractor import ReactionExtractor

pdf_path = "pdf_files/Synthesis_of_Fluorinated_Amines.pdf"

# Stage I: pdf to text
# The results will be automatically saved to pdf2text/results
print("########## Stage I: PDF-to-Text ##########")

result = parseFile(pdf_path)
full_text = result['fullText']  # Text without paragraph information
paragraphs = result['contents']  # Text with paragraph boundaries

# Stage II: text segmentation
print("########## Stage II: Text Segmentation ##########")
segmentor = TopicSegmentor()
seg_texts = segmentor.segment(paragraphs)

# Stage III: reaction extraction
print("########## Stage III: Reaction Extraction ##########")
extractor = ReactionExtractor('7b')
reactions = extractor.extract(seg_texts)

# Save the extracted chemical reactions
write_path = 'extraction/results'
os.makedirs(write_path, exist_ok=True)

pdf_stem = Path(pdf_path).stem
full_path = f'{write_path}/{pdf_stem}.json'

with open(full_path, 'w', encoding='utf-8') as f:
    json.dump(reactions, f, indent=4, ensure_ascii=False)
print(f"The results are stored in {full_path}")
