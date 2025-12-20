import pytest


@pytest.mark.asyncio
async def test_create_and_get_book(client):
    login = await client.post(
        "/auth/login",
        params={"email": "dkp@test.com", "password": "dkp123@123"},
    )
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    res = await client.post(
        "/books",
        headers=headers,
        json={
            "title": "Python",
            "author": "Author",
            "genre": "Tech",
            "year_published": 2025,
            "summary": "Test summary",
        },
    )
    assert res.status_code == 200
    book_id = res.json()["id"]

    res = await client.get(f"/books/{book_id}")
    assert res.status_code == 200
