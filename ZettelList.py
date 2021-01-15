
import os
import sys
from Zettel import Zettel


class ZettelList:

    def __init__(self, uri_zettels) -> None:
        file_list = [file for file in os.listdir(uri_zettels) if file.endswith(".md")]

        text_list = list()

        for file_name in file_list:
            with open(uri_zettels + "/" + file_name, "r") as f:
                text = f.read()
                text_list.append({
                    "text": text,
                    "name": file_name
                })

        self.list = [ Zettel(**element)
            for element in text_list
        ]


        super().__init__()

    def search(self, search_term):
        return [zettel
            for zettel in self.list
            if search_term in zettel.text
        ]

    