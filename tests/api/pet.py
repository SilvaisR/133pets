import pytest  # motor  /  engine
import requests  # bilioteca para comunicar com APIs

base_url = 'https://petstore.swagger.io/v2'  # endereço da API
headers = {'Content-Type': 'application/json'}  # os dados serão    no formato json


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
