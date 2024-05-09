from main_service.cmd import main
from fastapi.testclient import TestClient
from faker import Faker

from main_service.shemas.auth.auth_shemas import AuthRegisterModel

client = TestClient(app=main.app)


def test_register():
    faker = Faker()

    email = faker.email()
    password = faker.password()
    login = faker.name()
    steam = faker.random_int(3, 8)

    user = [
        AuthRegisterModel(
                email=email,
                password=password,
                password2=password,
                login=login,
                steam_id=steam
        ),
    ]

    for i in user:
        resp = client.post("/auth/register", json=i)
        assert resp.status_code == 200
