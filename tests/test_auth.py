import pytest


@pytest.mark.asyncio
async def test_register_and_login(client):
    res = await client.post(
        "/auth/register",
        json={
            "email": "dkp@test.com",
            "password": "dkp123@123",
            "role": "Admin",
        },
    )
    assert res.status_code == 200

    res = await client.post(
        "/auth/login",
        params={
            "email": "dkp@test.com",
            "password": "dkp123@123",
        },
    )
    assert res.status_code == 200
    assert "access_token" in res.json()
