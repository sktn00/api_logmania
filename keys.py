import secrets

for i in range(3):
    print(f"SERVICE{i+1}_API_KEY={secrets.token_urlsafe(16)}")