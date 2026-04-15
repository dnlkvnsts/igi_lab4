import re
import os
import zipfile
import base.validation as val
import base.output as out
import base.input as inp



CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class ArchiveMixin:
    def create_archive(self, file_to_zip, zip_name):
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
            zf.write(file_to_zip, os.path.basename(file_to_zip))
        return os.path.abspath(zip_name)

    def print_zip_info(self, zip_name):
        with zipfile.ZipFile(zip_name, 'r') as zf:
            for info in zf.infolist():
                out.print_message(f"Archive: {zip_name} | File: {info.filename} | Size: {info.file_size} bytes")



class TextEntity:
    def __init__(self, raw_text):
        self._raw_text = raw_text

    @property
    def raw_text(self):
        return self._raw_text

    @raw_text.setter
    def raw_text(self, value):
        if not value:
            raise ValueError("Text  cannot be empty")
        self._raw_text = value


class Analyzer(TextEntity, ArchiveMixin):
    VERSION = "1.0.0"

    def __init__(self, raw_text):
        super().__init__(raw_text)
        self.results = {}

    def __str__(self):
        return f"Analyzer Object (Text Length: {len(self.raw_text)})"

    def analyze_general(self):
        text = self.raw_text
        
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        self.results['Total Sentences'] = len(sentences)
        
        self.results['Declarative (.)'] = len(re.findall(r'[^.!?]+\.', text))
        self.results['Interrogative (?)'] = len(re.findall(r'[^.!?]+\?', text))
        self.results['Exclamatory (!)'] = len(re.findall(r'[^.!?]+\!', text))

        words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]+\b', text)
        chars_count = sum(len(w) for w in words)
        self.results['Avg Sentence Len (chars)'] = round(chars_count / len(sentences), 2) if sentences else 0
        self.results['Avg Word Len (chars)'] = round(chars_count / len(words), 2) if words else 0

        smiley_pattern = r'[;:][-]*([()\[\]])\1*'
        self.results['Smileys Count'] = len(re.findall(smiley_pattern, text))

    def analyze_variant_6(self):
        text = self.raw_text
        
        self.results['Capital+Digit Words'] = re.findall(r'\b[A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ0-9]*\d[a-zA-Zа-яА-ЯёЁ0-9]*\b', text)
        
        self.results['HTML Colors'] = re.findall(r'#[0-9a-fA-F]{6}', text)
        
        all_words = re.findall(r'\b\w+\b', text)
        if all_words:
            min_len = min(len(w) for w in all_words)
            self.results['Min Len Words Count'] = sum(1 for w in all_words if len(w) == min_len)
        
        self.results['Words before dot'] = re.findall(r'\b(\w+)\.', text)
        
        r_words = re.findall(r'\b\w*[rR]\b', text)
        self.results['Longest word ending in R'] = max(r_words, key=len) if r_words else "None"

    def save_and_archive(self, txt_filename, zip_filename):
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write(f"--- Analysis Report v{self.VERSION} ---\n")
            for k, v in self.results.items():
                f.write(f"{k}: {v}\n")
        
        self.create_archive(txt_filename, zip_filename)
        self.print_zip_info(zip_filename)



def run_task2():
    while True:
        out.print_message("TASK 2 ")
        
        input_file = os.path.join(CURRENT_DIR, "source_text.txt")
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("Привет, World1!!! Как твои дела сегодня?! Цвет #FF0000 — это ярко-красный... А ты знал, что Car1 едет со скоростью 120 км/ч? Вот смайлики для теста: правильные :-))) и ;---[[[, а также 'сломанные' :-)( и ;--. Отличная погода, не правда ли? Да, просто супер!")
        
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        proc = Analyzer(content)
        print(f"[Object Info]: {proc}")
        
        proc.analyze_general()
        proc.analyze_variant_6()

        out.print_analysis_results(proc.results)

        res_txt = os.path.join(CURRENT_DIR, "result_task2.txt")
        res_zip = os.path.join(CURRENT_DIR, "result_task2.zip")
        proc.save_and_archive(res_txt, res_zip)

        if not inp.repeat_task():
            break
