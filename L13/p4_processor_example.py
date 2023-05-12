from abc import ABC, abstractmethod


class AbstractReader(ABC):

    @abstractmethod
    def read(self):
        pass


class AbstractConverter(ABC):

    @abstractmethod
    def convert(self, data):
        pass


class AbstractWriter(ABC):

    @abstractmethod
    def write(self, data):
        pass


class ConsoleReader(AbstractReader):

    def read(self):
        return input("Input data:")


class FileReader(AbstractReader):

    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

    def read(self):
        with open(self.input_file_path) as f:
            return f.read()


class ConsoleWriter(AbstractWriter):

    def write(self, data):
        print(data)


class FileWriter(AbstractWriter):

    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def write(self, data):
        with open(self.output_file_path, 'w') as f:
            f.write(data)


class AddLengthConverter(AbstractConverter):

    def convert(self, data):
        converted_data = f"{data}\tLEN:{len(data)}"
        return converted_data


class DistinctWordSplitConverter(AbstractConverter):

    def convert(self, data):
        converted_data = "\n".join(set(data.split()))
        return converted_data


class Processor:

    def __init__(self, reader: AbstractReader, converter: AbstractConverter, writer: AbstractWriter):
        self.reader = reader
        self.converter = converter
        self.writer = writer

    def process(self):
        input_data = self.reader.read()
        converted_data = self.converter.convert(input_data)
        self.writer.write(converted_data)


console_length_processor = Processor(ConsoleReader(), AddLengthConverter(), ConsoleWriter())
console_length_processor.process()


distinct_word_split_processor = Processor(FileReader('input.txt'), DistinctWordSplitConverter(), FileWriter('output.txt'))
distinct_word_split_processor.process()