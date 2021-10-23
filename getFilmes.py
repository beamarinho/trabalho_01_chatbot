#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import sys
import requests
import json
def main(dict):
    if dict["titulo"] != "" and dict["ano"] is "":
        query = {
            't': dict["titulo"],
            'plot': 'full'
        }
        print(query)
        resp = requests.get('http://www.omdbapi.com/?apikey=9e984908', params=query).text
        texto = json.loads(resp)
        print(texto)
        return { 'title': texto["Title"],'plot': texto["Plot"],'poster': texto["Poster"], 'year': texto["Year"] }
    
    if dict["titulo"] != "" and dict["ano"] != "" :
        query = {
            't': dict["titulo"],
            'y': dict["ano"],
            'plot': 'full'
        }
        print(query)
        resp = requests.get('http://www.omdbapi.com/?apikey=9e984908', params=query).text
        texto = json.loads(resp)
        print(texto)
        return { 'title': texto["Title"],'plot': texto["Plot"],'poster': texto["Poster"], 'year': texto["Year"] }
    else:
        return { 'message': 'Movie not found!'}