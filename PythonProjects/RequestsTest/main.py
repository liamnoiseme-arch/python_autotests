import requests

TRAINER_TOKEN = "ddb041aaa640ecfa024494a94bcac5e5"
BASE_URL = "https://api.pokemonbattle.ru/v2"
headers = {"Content-Type": "application/json", "trainer_token": TRAINER_TOKEN}

print("POKEMON API TESTS")
print("="*50)

# 1. Create Pokemon
print("\n1. CREATING POKEMON...")
resp1 = requests.post(f"{BASE_URL}/pokemons", headers=headers, json={"name": "generate", "photo_id": -1})
print(f"Status: {resp1.status_code}")

if resp1.status_code == 201:
    pokemon = resp1.json()
    print(f"SUCCESS: {pokemon.get('message')}")
    print(f"Pokemon ID: {pokemon.get('id')}")
    pokemon_id = pokemon.get('id')
    
    # 2. Rename Pokemon
    print("\n2. RENAMING POKEMON...")
    resp2 = requests.put(f"{BASE_URL}/pokemons", headers=headers, json={
        "pokemon_id": pokemon_id,
        "name": "Nana",
        "photo_id": 452
    })
    print(f"Status: {resp2.status_code}")
    
    if resp2.status_code == 200:
        print(f"SUCCESS: {resp2.json().get('message')}")
        
        # 3. Catch in Pokeball
        print("\n3. CATCHING IN POKEBALL...")
        resp3 = requests.post(f"{BASE_URL}/trainers/add_pokeball", headers=headers, json={
            "pokemon_id": pokemon_id
        })
        print(f"Status: {resp3.status_code}")
        
        if resp3.status_code == 200:
            print(f"SUCCESS: {resp3.json().get('message')}")
            print(f"ID: {resp3.json().get('id')}")
            print("\n" + "="*50)
            print("ALL 3 TESTS PASSED!")
            print("="*50)
        else:
            print(f"ERROR: {resp3.text}")
    else:
        print(f"ERROR: {resp2.text}")
else:
    print(f"ERROR: {resp1.text}")