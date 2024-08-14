import psycopg2
import uuid
from datetime import datetime, timezone
import random


def generate_name():
    # Função fictícia para gerar nomes
    return "John Doe"


def generate_phone_number():
    # Função fictícia para gerar números de telefone
    return "123-456-7890"


def generate_cpf():
    # Função fictícia para gerar CPF
    return "123.456.789-00"


def generate_address():
    # Função fictícia para gerar endereços
    return "123 Main St"


def generate_city():
    # Função fictícia para gerar cidades
    return "Anytown"


def generate_state():
    # Função fictícia para gerar estados
    return "ST"


def generate_zipcode():
    # Função fictícia para gerar CEP
    return "12345-678"


def insert_user_to_db(user, cursor):
    insert_query = """
    INSERT INTO public.management_user (
        id, name, first_name, last_name, created_at, updated_at, password, email, is_superuser, is_staff, is_active, date_joined
    ) VALUES (
        %(id)s, %(name)s, %(first_name)s, %(last_name)s, %(created_at)s, %(updated_at)s, %(password)s, %(email)s, %(is_superuser)s, %(is_staff)s, %(is_active)s, %(date_joined)s
    )
    """
    cursor.execute(insert_query, user)


def insert_firefighter_to_db(firefighter, cursor):
    insert_query = """
    INSERT INTO public.management_firefighter (
        id, user_id, phone, cpf, address, address_number, address_complement, city, state, zipcode
    ) VALUES (
        %(id)s, %(user_id)s, %(phone)s, %(cpf)s, %(address)s, %(address_number)s, %(address_complement)s, %(city)s, %(state)s, %(zipcode)s
    )
    """
    cursor.execute(insert_query, firefighter)


def generate_and_insert_firefighters(n):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="sa-senai-bombeiros_db"
        )
        cursor = connection.cursor()

        now = datetime.now(timezone.utc)

        for i in range(n):
            user_id = str(uuid.uuid4())
            name = generate_name()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
            user = {
                "id": user_id,
                "name": name,
                "first_name": name,
                "last_name": name,
                "created_at": now,
                "updated_at": now,
                "password": "default_password",  # Adiciona um valor padrão para a senha
                # Usa timestamp para garantir unicidade
                "email": f"{timestamp}@example.com",
                "is_superuser": False,  # Adiciona um valor padrão para is_superuser
                "is_staff": False,
                "is_active": True,
                "date_joined": "2021-01-01T00:00:00Z"
            }
            insert_user_to_db(user, cursor)

            firefighter = {
                "id": user_id,
                "user_id": user_id,
                "phone": generate_phone_number(),
                "cpf": generate_cpf(),
                "address": generate_address(),
                "address_number": str(random.randint(1, 9999)),
                "address_complement": "",
                "city": generate_city(),
                "state": generate_state(),
                "zipcode": generate_zipcode()
            }
            insert_firefighter_to_db(firefighter, cursor)
            connection.commit()

    except (Exception, psycopg2.Error) as error:
        print("Error while inserting data into PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


# Gera e insere registros de bombeiros no banco de dados
generate_and_insert_firefighters(100)
