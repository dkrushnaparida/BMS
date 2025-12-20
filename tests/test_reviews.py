import pytest


@pytest.mark.asyncio
async def test_add_review(client):
    login = await client.post(
        "/auth/login",
        params={"email": "dkp@test.com", "password": "dkp123@123"},
    )
    token = login.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}

    book = await client.post(
        "/books",
        headers=headers,
        json={
            "title": "Review Book",
            "author": "Author",
            "genre": "Tech",
            "year_published": 2024,
            "summary": "Test book for review",
        },
    )

    book_id = book.json()["id"]

    res = await client.post(
        f"/books/{book_id}/reviews",
        headers=headers,
        json={"review_text": "Good book", "rating": 4},
    )
    assert res.status_code == 200
