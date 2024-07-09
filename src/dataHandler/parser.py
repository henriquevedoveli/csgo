class DatasetParser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.columns = []
        self.data = []

    def parse(self):
        with open(self.file_name, 'r') as file:
            for line in file.read().split("\n"):
                if line.startswith("@ATTRIBUTE"):
                    self.columns.append(line.split(" ")[1])
                if line.startswith("@") or line.startswith("%") or line == "":
                    continue
                self.data.append(line)
        print(f"Arquivo {self.file_name} parseado com sucesso.")

    def get_columns(self):
        return self.columns

    def get_data(self):
        return self.data