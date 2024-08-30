import requests

url = "https://us-central1-gaggle-staging.cloudfunctions.net/send_friend_request_ver2"

headers = {
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImNjNWU0MTg0M2M1ZDUyZTY4ZWY1M2UyYmVjOTgxNDNkYTE0NDkwNWUiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiVEVBTSBDUkVNQSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHaDJsUUZVcUFCUlFja3hSUjhLMmFyUlRPTGc5TEk0ZjllYzRuMD1zOTYtYyIsIkZyZWUiOnRydWUsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9nYWdnbGUtc3RhZ2luZyIsImF1ZCI6ImdhZ2dsZS1zdGFnaW5nIiwiYXV0aF90aW1lIjoxNzI0OTM5NjY3LCJ1c2VyX2lkIjoicmljaldtM2dUWVJwWnRMWFVsSk5rZ1ptMmU5MiIsInN1YiI6InJpY2pXbTNnVFlScFp0TFhVbEpOa2dabTJlOTIiLCJpYXQiOjE3MjUwMjM1NTQsImV4cCI6MTcyNTAyNzE1NCwiZW1haWwiOiJuYWtyb3kyMjEyQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7Imdvb2dsZS5jb20iOlsiMTA3Mzc0ODY2NzI4MjM1MzE3MDkxIl0sImVtYWlsIjpbIm5ha3JveTIyMTJAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZ29vZ2xlLmNvbSJ9fQ.mfSYNe-BR7sTK0v5mvy4z_Y-UEl6FOnx9U0JG7L4pZLuuXMvW9YzyqbxN2m11PvTGXcnwLurvPdtcbN-Yx91CjHNdHFpjJOXy288-LyZwoHMrDrzPBY1LxW6ZlHteFoyxFoi4MiFe9KYN4nG72KcVyKeNpL3E7Uhh7PIGUG8vD1j6Z6BL8Bo4-QwMY6L3eTudZY7DYUv46X4et3JIJzh6X0BMRiMHXHqZQ9ykUaIqTSDIWGvTXq0R9dcuEkqHMPcTy69JXtZPqixfzcozZAZa5XSUfB3lbo-ffKvPvPymFEtrxqceONYYsBAthmX-SwA4QXIq8EdVKmfH07BsXkKMg",
    "Content-Type": "application/json",
    "Host": "us-central1-gaggle-staging.cloudfunctions.net",
    "Accept-Encoding": "gzip, identity",
    "Connection": "Keep-Alive",
    "TE": "identity",
    "User-Agent": "BestHTTP/2 v2.5.4",
    "Content-Length": "401"
}

data = {
    "responderUserTag": "GRATO#2629",
    "pv": "6BB69DBF360666AFDDF54D0BA570BF3F263174C037220F656DBC9F0D493B6F8D86B772C56D2D80045B79CD904714AF613DD47D73DA3B4919A847B26E9E0778E7",
    "uid": "ricjWm3gTYRpZtLXUlJNkgZm2e92",
    "userTag": "VEX#1582",
    "timestamp": "1725023797373",
    "hashedString": "1DD8489570687F2E212E9D0E9D6F70539E9AC9AFD939462CD269AE0CF2FE18F4840928FAB2D96309047C4B747BC537C15CDCE425A0F0821E3C86ADB048D3D87F"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
