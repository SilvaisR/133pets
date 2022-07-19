import csv

import pytest  # motor  /  engine
import requests  # bilioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2'  # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão    no formato json


def ler_dados_scv():
    dados_csv = []  # Criamos uma lista vazia.
    nome_arquivo = r'C:\Users\silva\PycharmProjects\pythonProject133pets\vendors\csv\pets_positivo.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
            return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha não prevista: {fail}')


def testar_incluir_pet():
    # Configura
    # Dados de entrada: virão do pet1.json
    # Resultado esperado
    status_code_esperado = 200
    nome_pet_esperado = 'Alfredo'
    tag_esperada = 'Vacinado'

    # Executa
    resultado_obtido = requests.post(
        url=base_url + '/pet',
        data=open(r'C:\Users\silva\PycharmProjects\pythonProject133pets\vendors\json\pet1.json'),
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    response_body = resultado_obtido.json()  # Extrai o json da response
    print(response_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert response_body['name'] == nome_pet_esperado
    assert response_body['tags'][0]['name'] == tag_esperada


def testar_consultar_pet():
    # 1.0 - Configura

    # 1.1 - Dados de entrada

    pet_id = 420409

    # 1.2 - Resultado esperado

    status_code_esperado = 200
    nome_pet_esperado = 'Alfredo'
    tag_esperada = 'Vacinado'

    # Executa

    resultado_obtido = requests.get(
        url=base_url + '/pet/' + str(pet_id),
        headers=headers
    )
    # Valida
    print(resultado_obtido)
    response_body = resultado_obtido.json()
    print(response_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert response_body['name'] == nome_pet_esperado
    assert response_body['tags'][0]['name'] == tag_esperada


def testar_alterar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Alfredo'
    status_esperado = 'Sold'

    resultado_obtido = requests.put(
        url=base_url + '/pet/',
        data=open(r'C:\Users\silva\PycharmProjects\pythonProject133pets\vendors\json\pet2.json', 'rb'),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    response_body = resultado_obtido.json()
    print(response_body)
    assert response_body['name'] == nome_pet_esperado
    assert response_body['status'] == status_esperado


def testar_excluir_pet():
    pet_id = 420409
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = str(pet_id)

    resultado_obtido = requests.delete(
        url=base_url + '/pet/' + str(pet_id),
        headers=headers
    )

    assert resultado_obtido.status_code == status_code_esperado
    response_body = resultado_obtido.json()
    assert response_body['code'] == code_esperado
    assert response_body['type'] == type_esperado
    assert response_body['message'] == message_esperada


@pytest.mark.parametrize('pet_id,category_id,category_name,name,tags_id,tags_name,status,status_code', ler_dados_scv())
def testar_incluir_pet_json_dinamico(pet_id, category_id, category_name, name, tags_id, tags_name, status, status_code):
    # configura - Os dados e o resultado esperado.
    # 1.1 - Dados de entrada
    # Utilizará o arquivo pets_positivo.csv

    # 1.2 - Resultado esperado
    # Utilizará o arquivo pets_positivo.csv

    # 1.3 - Extra - montar o json dinamicamento a partir do csv
    corpo_json = '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '  "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": {category_name}'
    corpo_json += '},'
    corpo_json += f'"name": {name},'
    corpo_json += '"photoUrls": ['
    corpo_json += '"string"'
    corpo_json += '],'
    corpo_json += '"tags": ['
    corpo_json += '{'
    corpo_json += f'    "id": {tags_id},'
    corpo_json += f'    "name": {tags_name}'
    corpo_json += '}'
    corpo_json += '],'
    corpo_json += f'"status": {status}'
    corpo_json += '}'

    print(corpo_json)
    # executa
    resultado_obtido = requests.post(
        url=base_url + '/pet',
        data=corpo_json,
        headers=headers
    )

    # valida
    assert resultado_obtido.status_code == status_code
    corpo_da_resposta = resultado_obtido.json()
    print(corpo_da_resposta)
    assert corpo_da_resposta['id'] == pet_id
    assert corpo_da_resposta['category'][0]['id'] == category_id
    assert corpo_da_resposta['category'][0]['name'] == category_name
    assert corpo_da_resposta['name'] == name
    assert corpo_da_resposta['tags'][0]['id'] == tags_id
    assert corpo_da_resposta['tags'][0]['name'] == tags_name
    assert corpo_da_resposta['status'] == status
