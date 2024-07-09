import requests

class DataFetcher:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name


    def download(self):
        try:
            response = requests.get(self.url, allow_redirects=True)
            with open(self.file_name, 'wb') as file:
                file.write(response.content)
            print(f"Arquivo {self.file_name} baixado com sucesso.")
            return response
        except Exception as exc:
            raise exc
        


