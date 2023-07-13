url= "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=real"
url= "  "
print(url)

#limpeza da url
url = url.replace(" ","")
url = url.strip()


#validação da URL
if url == "":
    raise ValueError("A URL Está vazia")

url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros)

#Separa base e os parametros
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#Busca os valores de um parametro
parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca)+1
indice_e_comercial = url_parametros.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)