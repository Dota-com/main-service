from main_service.cmd import main
from fastapi.testclient import TestClient


client = TestClient(app=main.app)

TOKEN = [
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImRvbG9yaW5AbWFpbC5ydSIsImV4dCI6MTcxNDU5ODA1OCwidWlkIjo5fQ.HCknruQjoku0kkf6sw_9l00heE151SrBHppiuPEapOI"},
        "result": {
            "email": "dolorin@mail.ru",
            "ext": 1714598058,
            "uid": 9
        }
    },
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IndhbGxhY2VoYXJ2ZXlAamVyZGUuY29tIiwiZXh0IjoxNzE0NTk4MTAzLCJ1aWQiOjEwfQ.iXgWNvVAoxS5-PoLRAXH5pWukWanEW_kcXDsE4pnFb0"},
        "result": {
            "email": "wallaceharvey@jerde.com",
            "ext": 1714598103,
            "uid": 10
        }},
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imlzc2FjcnVzc2VsQGdyZWVuLmluZm8iLCJleHQiOjE3MTQ1OTgzMjEsInVpZCI6MTJ9.eKSrI3q4WWDgwbmT_0MRC1I8rpu3xXq09DF4xNPPIEI", },
        "result": {
            "email": "issacrussel@green.info",
            "ext": 1714598321,
            "uid": 12
        }
    },
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImxpbHlzd2FuaWF3c2tpQGJyYWR0a2UuaW5mbyIsImV4dCI6MTcxNDU5ODQwOSwidWlkIjoxMX0.CRHqROswGQtnXPNNlfhWM99kC4QD41-eGf8oiey1Ai0", },
        "result": {
            "email": "lilyswaniawski@bradtke.info",
            "ext": 1714598409,
            "uid": 11
        }
    },
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Imdlbm5hcm9tb3JhckBiZWllci5uYW1lIiwiZXh0IjoxNzE0NjgwNTY3LCJ1aWQiOjEzfQ.w1KTNJrhFRFfb14N0PRFKiqIxFyhxefQ_cQS___kvGA", },
        "result": {
            "email": "gennaromorar@beier.name",
            "ext": 1714680567,
            "uid": 13
        }
    },
    {
        "query": {
            "text": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InhkMTJAbWFpbC5ydSIsImV4dCI6MTcxNTA4NDY5NSwidWlkIjoxOX0.Zhhc7cnuXP-DQ66i-3T829EverlISqOXX0y_a_WQ5-s"},
        "result": {
            "email": "xd12@mail.ru",
            "ext": 1715084695,
            "uid": 19
        }
    },
]


def test_register():
    for i in TOKEN:
        response = client.post("/auth/register",
                               params=i["query"])
        assert response.status_code == 200
        assert response.json() == i["result"]
