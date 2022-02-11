#Essa é a versão do programa que está no link do colab e que pode ser usado por qualquer pessoa

import requests
from bs4 import BeautifulSoup

palavras_chave = 'Auxiliar Analista'
lista_palavras_chave = palavras_chave.split()
cidade = 'Atibaia'

#O número dentro do range(#) é a quantidade de páginas que serão procuradas. Se quiser olhar mais páginas é só mudar esse valor
for i in range(2):
    #URL e busca das informações do site
    url = r'https://www.atibaiasp.com.br/banco-de-vagas/page/' + str(i+1) + "/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    job_list = soup.find(class_='job-list')
    itens = job_list.find_all(class_='single')

    #Criei algumas condições para garantir que a vaga seja em Atibaia e que as palavras chaves estejam no título da vaga
    for item in itens:
      local = item.find(class_='job-location meta-item')
      if cidade.upper() in local.text.strip().upper():
        titulo = item.find('div', attrs={'class': 'title'})
        for palavra in lista_palavras_chave:
          if palavra.upper() in (palavra_titulo.upper() for palavra_titulo in titulo.text.strip("\n").split()):
            link = titulo.find('a').get('href')
            empresa = item.find('div', attrs={'class': 'company-name'})
            print("Título da vaga: " + titulo.text.strip("\n"))
            print("Empresa contratante: " + empresa.text)
            print(link)
            print('-----------------------------------------------------------------\n')