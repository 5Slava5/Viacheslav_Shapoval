# Програма очищує строки від знаків пунктуації
class TextProcessor:
    def __init__(self):
        self._punctuation = "!?.,:;*"

    def __is_punctuation(self, char):
        return char in self._punctuation

    def get_clean_string(self, text):
        clean = ""
        for char in text:
            if self.__is_punctuation(char):
                continue
            clean += char
        return clean


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print(f' It is a clean string: {self.__clean_string}')
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_text(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


obj = DataInterface()
t = ['! Hello, we. are? from: Ukraine!', ':We? like; Python* World,']
out = obj.process_texts(t)
