from dataHandler.fetcher import DataFetcher
from dataHandler.parser import DatasetParser
from dataHandler.writer import CSVWriter
from dataHandler.loader import DataFrameLoader

url = 'https://www.openml.org/data/download/22102255/dataset'
txt_file_name = 'data/csgo_dataset.txt'
csv_file_name = 'data/df.csv'

downloader = DataFetcher(url, txt_file_name)
downloader.download()

parser = DatasetParser(txt_file_name)
parser.parse()

csv_writer = CSVWriter(csv_file_name)
csv_writer.write(parser.get_columns(), parser.get_data())

loader = DataFrameLoader(csv_file_name, parser.get_columns())
df = loader.load()

print(df.head())
