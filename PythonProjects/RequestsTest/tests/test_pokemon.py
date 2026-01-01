import requests
import json

BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = "ID_TRAINER"

def test_get_trainers_status_code_200():
    """Test 1: Проверяет, что ответ запроса GET /trainers приходит с кодом 200"""
    print("\n" + "="*60)
    print("ЗАПУСК ТЕСТОВ API POKÉMON")
    print("="*60)
    
    print("\n🔍 Тест 1: Проверка GET /trainers (статус 200)")
    
    response = requests.get(f"{BASE_URL}/trainers")
    
    if response.status_code == 200:
        print("✅ Test 1 passed: GET /trainers вернул 200")
        data = response.json()
        print(f"   Найдено тренеров: {len(data['data'])}")
        print(f"   Статус ответа: {data['status']}")
        return True
    else:
        print(f"❌ Test 1 failed: Получен статус {response.status_code}")
        return False

def test_get_trainer_by_id_contains_name():
    """Test 2: Проверяет, что в ответе приходит строчка с именем твоего тренера"""
    print("\n🔍 Тест 2: Проверка тренера по ID")
    
    params = {"trainer_id": TRAINER_ID}
    response = requests.get(f"{BASE_URL}/trainers", params=params)
    
    if response.status_code == 200:
        data = response.json()
        trainers = data["data"]
        
        if len(trainers) > 0:
            trainer = trainers[0]
            print(f"✅ Test 2 passed: Найден тренер {TRAINER_ID}")
            
            # ВАЖНО: Здесь выводится только строка с именем тренера
            print(f"   Имя тренера: {trainer['trainer_name']}")
            
            return True
        else:
            print(f"❌ Test 2 failed: Тренер с ID {TRAINER_ID} не найден")
            return False
    else:
        print(f"❌ Test 2 failed: Получен статус {response.status_code}")
        return False

if __name__ == "__main__":
    # Запускаем оба теста
    test1_result = test_get_trainers_status_code_200()
    test2_result = test_get_trainer_by_id_contains_name()
    
    print("\n" + "="*60)
    
    if test1_result and test2_result:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("⚠️  НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")
    
    print("="*60)