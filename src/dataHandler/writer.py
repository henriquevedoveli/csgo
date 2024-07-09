class CSVWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, columns, data):
        with open(self.file_name, 'w') as file:
            file.write(",".join(columns))
            file.write("\n")
            file.write("\n".join(data))
        print(f"Arquivo {self.file_name} salvo com sucesso.")
