from app import app, add, sub, mul, div
import pytest

def test_add():
    assert add(10, 5) == 15

def test_sub():
    assert sub(10, 5) == 5

def test_mul():
    assert mul(10, 5) == 50

def test_div():
    assert div(10, 5) == 2

def test_home_route():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "Calculator API is running!"

def test_calc_route():
    client = app.test_client()
    res = client.get("/calc?a=10&b=5&op=add")
    assert res.status_code == 200
    assert res.json["result"] == 15
