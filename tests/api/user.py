import pytest  # motor
import requests  # Biblioteca para comunicar APIs

base_url = 'https://petstore.swagger.io/v2'  # Endereço da API
headers = {'content-type': 'application/json'}  # headers passa o formato da comunicação


def testar_incluir_usuario():
    # Configura
    status_code_esperado = 200
    message_esperada = '2220409'

    # Executa
    resultado_obtido = requests.post(
        url=base_url + '/user',
        data=open(r'C:\Users\silva\PycharmProjects\pythonProject133pets\vendors\json\user1.json'),
        headers=headers
    )

    # valida
    print(resultado_obtido)
    print('=' * 40)
    response_body = resultado_obtido.json()  # extrai o json da response
    print(response_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert response_body['message'] == message_esperada


def testar_consultar_usuario():
    # configura
    status_code_esperado = 200
    username = 'Cica013'
    id_esperado = 2220409
    firstname_esperado = 'Silvanis'
    phone_esperado = '988060409'
    status_code_esperado = 200

    # executa
    resultado_obtido = requests.get(
        url=base_url + '/user/' + username,
        headers=headers
    )

    # valida
    assert resultado_obtido.status_code == status_code_esperado
    print(resultado_obtido)
    print('=' * 30)
    response_body = resultado_obtido.json()  # Estou extraindo o json da response
    print(response_body)
    assert response_body["username"] == username
    assert response_body["id"] == id_esperado
    assert response_body["firstName"] == firstname_esperado
    assert response_body["phone"] == phone_esperado


def testar_alterar_usuario():
    # configura
    username = 'Cica013'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = '1110409'

    # executa
    resultado_obtido = requests.put(
        url=base_url + '/user/' + username,
        data=open(r'C:\Users\silva\PycharmProjects\pythonProject133pets\vendors\json\user2.json'),
        headers=headers
    )

    # valida
    response_body = resultado_obtido.json()  # Extraindo json do resultado obtido
    print(resultado_obtido)
    print('=' * 30)
    print(response_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert response_body["code"] == code_esperado
    assert response_body["type"] == type_esperado
    assert response_body["message"] == message_esperada


def testar_deletar_usuario():
    # configura
    username = 'Cica013'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    message_esperada = 'Cica013'

    # executa
    resultado_obtido = requests.delete(
        url=base_url + '/user/' + username,
        headers=headers
    )

    # valida
    print(resultado_obtido)
    print('='*30)
    response_body = resultado_obtido.json()
    print(response_body)
    assert resultado_obtido.status_code == status_code_esperado
    assert response_body['code'] == code_esperado
    assert response_body['type'] == type_esperado
    assert response_body['message'] == message_esperada
