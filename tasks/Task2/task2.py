"""
The task number 2

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 17.04.2026
"""


import re
import os
import zipfile
import base.output as out
import base.input as inp


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class ArchiveMixin:
    """
    A mixin class providing utility methods for working with ZIP archives.
    """
    def create_archive(self, file_to_zip, zip_name):
        """
        Creates a ZIP archive and adds a specified file to it.

        Args:
            file_to_zip (str): Path to the source file to be compressed.
            zip_name (str): Name/path of the resulting ZIP archive.

        Returns:
            str: The absolute path to the created ZIP archive.
            
        Raises:
            FileNotFoundError: If the source file does not exist.
            PermissionError: If there are permission issues.
            zipfile.BadZipFile: If the zip file is corrupted.
        """
        try:
            if not os.path.exists(file_to_zip):
                raise FileNotFoundError(f"Source file '{file_to_zip}' not found")
                
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
                zf.write(file_to_zip, os.path.basename(file_to_zip))
            return os.path.abspath(zip_name)
            
        except FileNotFoundError as e:
            out.print_message(f"Error: {e}")
            raise
        except PermissionError as e:
            out.print_message(f"Permission denied: {e}")
            raise
        except zipfile.BadZipFile as e:
            out.print_message(f"Bad zip file error: {e}")
            raise
        except Exception as e:
            out.print_message(f"Unexpected error creating archive: {e}")
            raise

    def print_zip_info(self, zip_name):
        """
        Reads a ZIP archive and prints metadata about the files contained within.

        Args:
            zip_name (str): Path to the ZIP archive to inspect.
        """
        try:
            if not os.path.exists(zip_name):
                raise FileNotFoundError(f"Zip file '{zip_name}' not found")
            
            with zipfile.ZipFile(zip_name, 'r') as zf:
                for info in zf.infolist():
                    out.print_message(f"Archive: {zip_name} | File: {info.filename} | Size: {info.file_size} bytes")
                
        except FileNotFoundError as e:
            out.print_message(f"Error: {e}")
        except PermissionError as e:
            out.print_message(f"Permission denied reading zip: {e}")
        except zipfile.BadZipFile as e:
            out.print_message(f"Error: Corrupted zip file - {e}")
        except Exception as e:
            out.print_message(f"Unexpected error reading zip: {e}")
        
class TextEntity:
    """
    A base class representing a text entity with raw content.
    """
    def __init__(self, raw_text):
        """
        Initializes the TextEntity with raw text content.

        Args:
            raw_text (str): The initial text content.
            
        Raises:
            ValueError: If the provided text is empty.
        """
        try:
            if not raw_text:
                raise ValueError("Text cannot be empty")
            self._raw_text = raw_text
        except ValueError as e:
            out.print_message(f"Error initializing TextEntity: {e}")
            raise

    @property
    def raw_text(self):
        """
        Gets or sets the raw text content. Validates that the input is not empty.

        Returns:
            str: The raw text content.

        Raises:
            ValueError: If the provided text value is empty.
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, value):
        """
        Sets the raw text content.

        Args:
            value (str): The new text content.
        """
        if not value:
            raise ValueError("Text cannot be empty")
        self._raw_text = value


class Analyzer(TextEntity, ArchiveMixin):
    """
    A class for performing linguistic and pattern-based analysis on text.
    Inherits from TextEntity and ArchiveMixin.

    Attributes:
        VERSION (str): The version of the analyzer logic.
        results (dict): A dictionary storing results of various analyses.
    """
    VERSION = "1.0.0"

    def __init__(self, raw_text):
        """
        Initializes the Analyzer with text and an empty results dictionary.

        Args:
            raw_text (str): The text content to be analyzed.
        """
        super().__init__(raw_text)
        self.results = {}

    def __str__(self):
        """
        Returns a string representation of the Analyzer object.

        Returns:
            str: Summary including text length.
        """
        return f"Analyzer Object (Text Length: {len(self.raw_text)})"

    def analyze_general(self):
        """
        Performs general text analysis including sentence counts, average lengths, and smileys.
        Uses regular expressions to identify patterns.
        """
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

        smiley_pattern = r'[;:]-*[()\[\]]+'
        self.results['Smileys Count'] = len(re.findall(smiley_pattern, text))

    def analyze_variant_6(self):
        """
        Performs specific analysis tasks based on 'Variant 6' requirements.
        Identifies capitalized words with digits, HTML colors, shortest words, and specific word endings.
        """
        text = self.raw_text
        
        capital_digit_words = re.findall(r'\b[A-ZА-ЯЁ][a-zA-Zа-яА-ЯёЁ0-9]*\d[a-zA-Zа-яА-ЯёЁ0-9]*\b', text)
    
    
        filtered_words = []
        for word in capital_digit_words:
        
            if not (len(word) == 6 and re.match(r'^[0-9A-F]{6}$', word)):
                filtered_words.append(word)
    
        self.results['Capital+Digit Words'] = filtered_words
        
        self.results['HTML Colors'] = re.findall(r'#[0-9a-fA-F]{6}', text)
        
        all_words = re.findall(r'\b\w+\b', text)
        if all_words:
            word_lengths = [len(w) for w in all_words]
            min_len = min(word_lengths)
            self.results['Min Len Words Count'] = sum(1 for length in word_lengths if length == min_len)

        self.results['Words before dot'] = re.findall(r'\b(\w+)\.', text)

        r_words = re.findall(r'\b\w*[rR]\b', text)
        if r_words:
            self.results['Longest word ending in R'] = max(r_words, key=len)
        else:
            self.results['Longest word ending in R'] = "None"
            
    def save_and_archive(self, txt_filename, zip_filename):
        """
        Saves analysis results to a text file and then compresses it into a ZIP archive.

        Args:
            txt_filename (str): Path for the report text file.
            zip_filename (str): Path for the resulting ZIP archive.
        """
        try:
            with open(txt_filename, 'w', encoding='utf-8') as f:
                f.write(f"--- Analysis Report v{self.VERSION} ---\n")
                for k, v in self.results.items():
                    f.write(f"{k}: {v}\n")
        except PermissionError:
            out.print_message(f"Permission denied to write '{txt_filename}'")
        except IOError as e:
            out.print_message(f"Error writing to file: {e}")
        
        try:
            self.create_archive(txt_filename, zip_filename)
            out.print_message(f"Archive created: {zip_filename}")
        except Exception as e:
            out.print_message(f"Failed to create archive: {e}")
            return
    
        try:
            self.print_zip_info(zip_filename)
        except Exception as e:
            out.print_message(f"Failed to read zip info: {e}")


def run_task2():
    """
    The main execution function for Task 2.
    Handles file input/creation, runs the analyzer, and manages output reporting.
    """
    while True:
        out.print_message("TASK 2 ")
        
        input_file = os.path.join(CURRENT_DIR, "source_text.txt")
        if not os.path.exists(input_file):
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write("Hello, World1!!! How are you today?! The color #FF0000 is bright red... Did you know that Car1 is driving at 120 km/h? Here are some smileys for testing: correct :-))) and ;---[[[, also 'broken' :-)( and ;--. Nice weather, isn't it? Yes, just super!")
        
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            out.print_message(f"File '{input_file}' not found")
        except PermissionError:
            out.print_message(f"Permission denied to read '{input_file}'")
        except UnicodeDecodeError:
            out.print_message(f"Encoding error in '{input_file}'")
        except IOError as e:
            out.print_message(f"IO error: {e}")

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
