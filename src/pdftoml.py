# Basic usage:  python src/pdftoml.py test out ca
# Script to convert pdf to txt


from pathlib import Path
import sys
import os
import logging
import pdftotext
import re
import time
from sentence_splitter import SentenceSplitter
logging.basicConfig(level=logging.INFO)


def process(pdf, lang):
    logging.info(f"Processing file {pdf}")
    read_file = open(pdf,'rb')
    content_per_page = pdftotext.PDF(read_file)
    content = [page for page in content_per_page]
    content = " ".join(content)

    # recover hyphen-splitter sentences
    pattern_line_break_1 = re.compile(r"-\n")
    # recover sentences split not preceded by a period and followed by lowercase character
    pattern_line_break_2 = re.compile(r"(?<![.?¿!¡º])\s*\n(?=\s*[a-z])")

    content_processed = pattern_line_break_1.sub("",content)
    content_processed = pattern_line_break_2.sub(" ", content_processed)

    # Split lines
    splitter = SentenceSplitter(language=lang)
    split_file = splitter.split(text=content_processed)

    # Remove empty lines
    split_file_clean = [line for line in split_file if re.match('.*[\w].*',line)]

    lines_raw = len(content)
    lines_processed = len(split_file_clean)

    logging.info(f"Raw lines: {lines_raw}, Postprocessed lines: {lines_processed}, "
                 f"Difference: {lines_raw - lines_processed}")

    return "\n".join(split_file_clean)

def main():
    t = time.time()
    data_dir = sys.argv[1]
    output_dir = sys.argv[2]
    lang = sys.argv[3]
    os.makedirs(output_dir, exist_ok=True)
    SUFFIX = ".pdf"
    p = Path(os.path.realpath(data_dir))
    for pdf in list(p.rglob(f"*{SUFFIX}")):
        processed_file = process(pdf,lang)
        out_file = open(output_dir +'/'+pdf.name.replace('.pdf','.txt'),'w')
        out_file.write(processed_file)
    print('Time to process PDFs: {} mins'.format(round((time.time() - t) / 60, 2)))

if __name__ == "__main__":
    main()
