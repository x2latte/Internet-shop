# # fill_db.py
# import random
# import requests
# from app.database import SessionLocal
# from app import models

# # ----------- КОНФИГУРАЦИЯ -----------
# API_KEY = "AIzaSyCMhmw1i024kkQdkU9eX4F7PppihBbw0mQ"  
# CX = "032357b762e5e4e85"                             
# # ------------------------------------

# CATEGORIES = [
#     {"name": "Смартфоны", "description": "Мобильные телефоны и аксессуары"},
#     {"name": "Ноутбуки", "description": "Портативные компьютеры и ультрабуки"},
#     {"name": "Наушники", "description": "Беспроводные, проводные, TWS"},
#     {"name": "Умные часы", "description": "Смарт-часы и фитнес-браслеты"},
#     {"name": "Телевизоры", "description": "Телевизоры, мониторы, проекторы"},
#     {"name": "Бытовая техника", "description": "Холодильники, стиральные машины, пылесосы"},
#     {"name": "Комплектующие", "description": "Процессоры, видеокарты, ОЗУ, SSD"},
#     {"name": "Аудио", "description": "Колонки, плееры, звуковые карты"},
#     {"name": "Фототехника", "description": "Фотоаппараты, объективы, штативы"},
#     {"name": "Игровые приставки", "description": "PlayStation, Xbox, Nintendo Switch"},
#     {"name": "Одежда", "description": "Спортивная и повседневная одежда"},
# ]

# BRANDS = [
#     "Apple", "Samsung", "Xiaomi", "Huawei", "Google", "Microsoft",
#     "Lenovo", "Asus", "Dell", "HP", "Acer", "Logitech",
#     "JBL", "Bose", "Sony", "Beats", "Canon", "Nikon", "GoPro",
#     "Nintendo", "PlayStation", "Xbox", "SteelSeries", "Razer",
#     "Nike", "Adidas", "Puma", "Reebok", "Levi's", "Zara",
# ]

# # Товары: (название, описание, цена, категория (индекс), бренд (индекс или -1))
# PRODUCTS = [
#     # Смартфоны (категория 0)
#     ("iPhone 16 Pro Max", "Флагман с титановым корпусом и AI-чипом", 129900, 0, 0),
#     ("Samsung Galaxy S25 Ultra", "Мощный Android с S Pen", 119900, 0, 1),
#     ("Xiaomi 14T Pro", "Доступный флагман с отличной камерой", 79900, 0, 2),
#     ("Google Pixel 9 Pro", "Лучшая камера и чистый Android", 99900, 0, 4),
#     ("Huawei P60 Pro", "Китайский флагман с крутым зумом", 89900, 0, 3),
#     ("OnePlus 12", "Быстрый и стильный смартфон", 74900, 0, -1),

#     # Ноутбуки (категория 1)
#     ("MacBook Pro 16 M3", "Мощный ноутбук для профессионалов", 249900, 1, 0),
#     ("Dell XPS 15", "Ультрабук с безрамочным экраном", 189900, 1, 6),
#     ("Lenovo ThinkPad X1 Carbon", "Надёжный бизнес-ноутбук", 169900, 1, 5),
#     ("ASUS ROG Zephyrus G14", "Игровой ноутбук с Ryzen 9", 159900, 1, 7),
#     ("HP Spectre x360", "Трансформер с отличным дисплеем", 139900, 1, 8),
#     ("Acer Swift 5", "Лёгкий и тонкий ультрабук", 89900, 1, 9),

#     # Наушники (категория 2)
#     ("Sony WH-1000XM6", "Лучшие наушники с шумодавом", 39900, 2, 12),
#     ("Bose QuietComfort 45", "Комфортные наушники с отличным звуком", 32900, 2, 11),
#     ("Apple AirPods Pro 2", "TWS с активным шумодавом", 24900, 2, 0),
#     ("Samsung Galaxy Buds3 Pro", "TWS с поддержкой 360 аудио", 19900, 2, 1),
#     ("JBL Tune 770NC", "Доступные наушники с шумодавом", 12900, 2, 10),

#     # Умные часы (категория 3)
#     ("Apple Watch Ultra 2", "Спортивные часы с титановым корпусом", 79900, 3, 0),
#     ("Samsung Galaxy Watch 6 Classic", "Элегантные часы с вращающимся безелем", 49900, 3, 1),
#     ("Garmin Fenix 8", "GPS-часы для экстремального спорта", 99900, 3, -1),
#     ("Xiaomi Watch S3", "Бюджетные смарт-часы с AMOLED", 14900, 3, 2),

#     # Телевизоры (категория 4)
#     ("Samsung Neo QLED 85", "8K TV с технологией Mini-LED", 899900, 4, 1),
#     ("Sony OLED XR A95L", "Органический OLED с потрясающим цветом", 799900, 4, 12),
#     ("LG C3 OLED 65", "Популярный OLED-телевизор", 349900, 4, -1),
#     ("TCL Mini-LED 75", "Доступный большой телевизор", 199900, 4, -1),

#     # Бытовая техника (категория 5)
#     ("Samsung Bespoke Refrigerator", "Холодильник с индивидуальным дизайном", 299900, 5, 1),
#     ("LG Styler", "Паровой шкаф для одежды", 69900, 5, -1),
#     ("Dyson V15 Detect", "Мощный беспроводной пылесос", 79900, 5, -1),
#     ("Bosch Serie 8 Dishwasher", "Посудомоечная машина с интеллектом", 89900, 5, -1),

#     # Комплектующие (категория 6)
#     ("Intel Core i9-14900K", "Флагманский процессор для ПК", 59900, 6, -1),
#     ("AMD Ryzen 9 7950X", "Мощный процессор для энтузиастов", 54900, 6, -1),
#     ("NVIDIA RTX 4090", "Видеокарта для игр и AI", 199900, 6, -1),
#     ("Samsung SSD 990 Pro 2TB", "Скоростной NVMe-накопитель", 24900, 6, 0),
#     ("G.Skill Trident Z DDR5", "Игровая память 32 ГБ", 15900, 6, -1),

#     # Аудио (категория 7)
#     ("Sonos Era 300", "Умная колонка с пространственным звуком", 44900, 7, -1),
#     ("JBL Flip 6", "Водонепроницаемая портативная колонка", 9900, 7, 10),
#     ("FiiO M17", "Высококлассный аудиоплеер", 89900, 7, -1),
#     ("SteelSeries Arctic Nova Pro", "Игровая гарнитура с ANC", 32900, 7, 20),

#     # Фототехника (категория 8)
#     ("Canon EOS R6 Mark II", "Беззеркальная камера для профессионалов", 249900, 8, 14),
#     ("Nikon Z8", "Флагманская беззеркалка", 399900, 8, 15),
#     ("Sony FX30", "Кино-камера для видеографов", 189900, 8, 12),
#     ("GoPro Hero 12 Black", "Экшн-камера для съёмки в движении", 39900, 8, 16),

#     # Игровые приставки (категория 9)
#     ("PlayStation 5 Pro", "Обновлённая версия PS5 с более мощным GPU", 89900, 9, 18),
#     ("Xbox Series X", "Самая мощная игровая консоль", 69900, 9, 19),
#     ("Nintendo Switch OLED", "Гибридная консоль с ярким экраном", 39900, 9, 17),
#     ("Steam Deck OLED", "Портативный ПК для игр", 49900, 9, -1),

#     # Одежда (категория 10)
#     ("Nike Air Max 2025", "Кроссовки с воздушной подушкой", 15900, 10, 21),
#     ("Adidas Ultraboost Light", "Лёгкие беговые кроссовки", 13900, 10, 22),
#     ("Puma Suede Classic", "Классические кеды", 7900, 10, 23),
#     ("Levi's 501 Original", "Джинсы прямого кроя", 9900, 10, 24),
#     ("Zara Oversize Hoodie", "Уютный худи оверсайз", 4500, 10, 25),
# ]

# def get_image_url(query):
#     """Получает первую картинку из Google Images по запросу"""
#     url = "https://www.googleapis.com/customsearch/v1"
#     params = {
#         "key": API_KEY,
#         "cx": CX,
#         "q": query,
#         "searchType": "image",
#         "num": 1,
#     }
#     try:
#         response = requests.get(url, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         if "items" in data and len(data["items"]) > 0:
#             return data["items"][0]["link"]
#         else:
#             return None
#     except Exception as e:
#         print(f"Ошибка при запросе к Google API: {e}")
#         return None

# def fill_db():
#     db = SessionLocal()

#     # 1. Создаём категории
#     category_map = {}
#     for cat in CATEGORIES:
#         existing = db.query(models.Category).filter(models.Category.name == cat["name"]).first()
#         if not existing:
#             new_cat = models.Category(name=cat["name"], description=cat["description"])
#             db.add(new_cat)
#             db.commit()
#             db.refresh(new_cat)
#             category_map[cat["name"]] = new_cat
#         else:
#             category_map[cat["name"]] = existing

#     # 2. Создаём бренды
#     brand_map = {}
#     for name in BRANDS:
#         existing = db.query(models.Brand).filter(models.Brand.name == name).first()
#         if not existing:
#             brand = models.Brand(name=name)
#             db.add(brand)
#             db.commit()
#             db.refresh(brand)
#             brand_map[name] = brand
#         else:
#             brand_map[name] = existing

#     # 3. Добавляем товары
#     cat_list = list(category_map.values())
#     brand_list = list(brand_map.values())

#     for idx, prod_data in enumerate(PRODUCTS):
#         name, desc, price, cat_idx, brand_idx = prod_data
#         category = cat_list[cat_idx] if cat_idx < len(cat_list) else cat_list[0]
#         if brand_idx >= 0 and brand_idx < len(brand_list):
#             brand = brand_list[brand_idx]
#         else:
#             brand = random.choice(brand_list)

#         existing_product = db.query(models.Product).filter(
#             models.Product.name == name,
#             models.Product.brand_id == brand.id,
#             models.Product.category_id == category.id
#         ).first()
#         if existing_product:
#             print(f"Товар '{name}' уже существует, пропускаем.")
#             continue

#         product = models.Product(
#             name=name,
#             description=desc,
#             price=price,
#             category_id=category.id,
#             brand_id=brand.id
#         )
#         db.add(product)
#         db.commit()
#         db.refresh(product)

#         # Ищем картинку по названию товара
#         print(f"Ищем картинку для: {name}...")
#         image_url = get_image_url(name)
#         if image_url:
#             img = models.ProductImage(image_url=image_url, product_id=product.id)
#             db.add(img)
#             print(f"  ✅ Картинка найдена")
#         else:
#             # Заглушка
#             img = models.ProductImage(
#                 image_url="https://via.placeholder.com/400x400?text=No+Image",
#                 product_id=product.id
#             )
#             db.add(img)
#             print(f"  ⚠️ Картинка не найдена, установлена заглушка")
#         db.commit()

#         print(f"✅ Добавлен товар: {product.name} (ID {product.id}), цена {price} ₽")

#     db.close()
#     print("🎉 Заполнение БД завершено!")

# if __name__ == "__main__":
#     fill_db()

# fill_db.py (без Google API)
# fill_db.py (только picsum.photos с seed на основе названия)



# import random
# import hashlib
# import re
# from typing import Optional, Iterable, List
# from urllib.parse import quote

# import requests

# from app.database import SessionLocal
# from app import models

# # -------------------- НАСТРОЙКИ --------------------

# WIKI_API = "https://en.wikipedia.org/w/api.php"
# UA_HEADERS = {
#     "User-Agent": "Mozilla/5.0 (compatible; fill-db/1.0; +https://example.com)"
# }
# REQUEST_TIMEOUT = 10

# # Если реальная картинка не найдена, код всё равно не упадёт.
# # Но лучше, чтобы этот fallback использовался как можно реже.
# FALLBACK_IMAGE = "https://placehold.co/400x400/png?text=No+Image"

# # -------------------- ДАННЫЕ --------------------

# CATEGORIES = [
#     {"name": "Смартфоны", "description": "Мобильные телефоны и аксессуары"},
#     {"name": "Ноутбуки", "description": "Портативные компьютеры и ультрабуки"},
#     {"name": "Наушники", "description": "Беспроводные, проводные, TWS"},
#     {"name": "Умные часы", "description": "Смарт-часы и фитнес-браслеты"},
#     {"name": "Телевизоры", "description": "Телевизоры, мониторы, проекторы"},
#     {"name": "Бытовая техника", "description": "Холодильники, стиральные машины, пылесосы"},
#     {"name": "Комплектующие", "description": "Процессоры, видеокарты, ОЗУ, SSD"},
#     {"name": "Аудио", "description": "Колонки, плееры, звуковые карты"},
#     {"name": "Фототехника", "description": "Фотоаппараты, объективы, штативы"},
#     {"name": "Игровые приставки", "description": "PlayStation, Xbox, Nintendo Switch"},
#     {"name": "Одежда", "description": "Спортивная и повседневная одежда"},
# ]

# BRANDS = [
#     "Apple", "Samsung", "Xiaomi", "Huawei", "Google", "Microsoft",
#     "Lenovo", "Asus", "Dell", "HP", "Acer", "Logitech",
#     "JBL", "Bose", "Sony", "Beats", "Canon", "Nikon", "GoPro",
#     "Nintendo", "PlayStation", "Xbox", "SteelSeries", "Razer",
#     "Nike", "Adidas", "Puma", "Reebok", "Levi's", "Zara",
# ]

# # Товары: (название, описание, цена, категория (индекс), бренд (индекс или -1), ссылка_на_картинку_или_None)
# # Здесь оставляем твои данные, но для части товаров будем автоматически искать реальную картинку.
# PRODUCTS = [
#     # Смартфоны (категория 0)
#     ("iPhone 16 Pro Max", "Флагман с титановым корпусом и AI-чипом", 129900, 0, 0,
#      "https://upload.wikimedia.org/wikipedia/commons/7/7c/IPhone_16_Vector.svg"),
#     ("Samsung Galaxy S25 Ultra", "Мощный Android с S Pen", 119900, 0, 1,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Samsung_Galaxy_S24_Ultra.svg/800px-Samsung_Galaxy_S24_Ultra.svg.png"),
#     ("Xiaomi 14T Pro", "Доступный флагман с отличной камерой", 79900, 0, 2, None),
#     ("Google Pixel 9 Pro", "Лучшая камера и чистый Android", 99900, 0, 4, None),
#     ("Huawei P60 Pro", "Китайский флагман с крутым зумом", 89900, 0, 3, None),
#     ("OnePlus 12", "Быстрый и стильный смартфон", 74900, 0, -1, None),

#     # Ноутбуки (категория 1)
#     ("MacBook Pro 16 M3", "Мощный ноутбук для профессионалов", 249900, 1, 0,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/MacBook_Pro_16%22_Space_Black.svg/800px-MacBook_Pro_16%22_Space_Black.svg.png"),
#     ("Dell XPS 15", "Ультрабук с безрамочным экраном", 189900, 1, 6, None),
#     ("Lenovo ThinkPad X1 Carbon", "Надёжный бизнес-ноутбук", 169900, 1, 5, None),
#     ("ASUS ROG Zephyrus G14", "Игровой ноутбук с Ryzen 9", 159900, 1, 7, None),
#     ("HP Spectre x360", "Трансформер с отличным дисплеем", 139900, 1, 8, None),
#     ("Acer Swift 5", "Лёгкий и тонкий ультрабук", 89900, 1, 9, None),

#     # Наушники (категория 2)
#     ("Sony WH-1000XM6", "Лучшие наушники с шумодавом", 39900, 2, 12, None),
#     ("Bose QuietComfort 45", "Комфортные наушники с отличным звуком", 32900, 2, 11, None),
#     ("Apple AirPods Pro 2", "TWS с активным шумодавом", 24900, 2, 0,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/AirPods_Pro_2.svg/800px-AirPods_Pro_2.svg.png"),
#     ("Samsung Galaxy Buds3 Pro", "TWS с поддержкой 360 аудио", 19900, 2, 1, None),
#     ("JBL Tune 770NC", "Доступные наушники с шумодавом", 12900, 2, 10, None),

#     # Умные часы (категория 3)
#     ("Apple Watch Ultra 2", "Спортивные часы с титановым корпусом", 79900, 3, 0,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Apple_Watch_Ultra_2.svg/800px-Apple_Watch_Ultra_2.svg.png"),
#     ("Samsung Galaxy Watch 6 Classic", "Элегантные часы с вращающимся безелем", 49900, 3, 1, None),
#     ("Garmin Fenix 8", "GPS-часы для экстремального спорта", 99900, 3, -1, None),
#     ("Xiaomi Watch S3", "Бюджетные смарт-часы с AMOLED", 14900, 3, 2, None),

#     # Телевизоры (категория 4)
#     ("Samsung Neo QLED 85", "8K TV с технологией Mini-LED", 899900, 4, 1, None),
#     ("Sony OLED XR A95L", "Органический OLED с потрясающим цветом", 799900, 4, 12, None),
#     ("LG C3 OLED 65", "Популярный OLED-телевизор", 349900, 4, -1, None),
#     ("TCL Mini-LED 75", "Доступный большой телевизор", 199900, 4, -1, None),

#     # Бытовая техника (категория 5)
#     ("Samsung Bespoke Refrigerator", "Холодильник с индивидуальным дизайном", 299900, 5, 1, None),
#     ("LG Styler", "Паровой шкаф для одежды", 69900, 5, -1, None),
#     ("Dyson V15 Detect", "Мощный беспроводной пылесос", 79900, 5, -1, None),
#     ("Bosch Serie 8 Dishwasher", "Посудомоечная машина с интеллектом", 89900, 5, -1, None),

#     # Комплектующие (категория 6)
#     ("Intel Core i9-14900K", "Флагманский процессор для ПК", 59900, 6, -1, None),
#     ("AMD Ryzen 9 7950X", "Мощный процессор для энтузиастов", 54900, 6, -1, None),
#     ("NVIDIA RTX 4090", "Видеокарта для игр и AI", 199900, 6, -1, None),
#     ("Samsung SSD 990 Pro 2TB", "Скоростной NVMe-накопитель", 24900, 6, 0, None),
#     ("G.Skill Trident Z DDR5", "Игровая память 32 ГБ", 15900, 6, -1, None),

#     # Аудио (категория 7)
#     ("Sonos Era 300", "Умная колонка с пространственным звуком", 44900, 7, -1, None),
#     ("JBL Flip 6", "Водонепроницаемая портативная колонка", 9900, 7, 10, None),
#     ("FiiO M17", "Высококлассный аудиоплеер", 89900, 7, -1, None),
#     ("SteelSeries Arctic Nova Pro", "Игровая гарнитура с ANC", 32900, 7, 20, None),

#     # Фототехника (категория 8)
#     ("Canon EOS R6 Mark II", "Беззеркальная камера для профессионалов", 249900, 8, 14, None),
#     ("Nikon Z8", "Флагманская беззеркалка", 399900, 8, 15, None),
#     ("Sony FX30", "Кино-камера для видеографов", 189900, 8, 12, None),
#     ("GoPro Hero 12 Black", "Экшн-камера для съёмки в движении", 39900, 8, 16, None),

#     # Игровые приставки (категория 9)
#     ("PlayStation 5 Pro", "Обновлённая версия PS5 с более мощным GPU", 89900, 9, 18,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/PlayStation_5_and_DualSense_controller.svg/800px-PlayStation_5_and_DualSense_controller.svg.png"),
#     ("Xbox Series X", "Самая мощная игровая консоль", 69900, 9, 19,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Xbox_Series_X.svg/800px-Xbox_Series_X.svg.png"),
#     ("Nintendo Switch OLED", "Гибридная консоль с ярким экраном", 39900, 9, 17,
#      "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Nintendo_Switch.svg/800px-Nintendo_Switch.svg.png"),
#     ("Steam Deck OLED", "Портативный ПК для игр", 49900, 9, -1, None),

#     # Одежда (категория 10)
#     ("Nike Air Max 2025", "Кроссовки с воздушной подушкой", 15900, 10, 21, None),
#     ("Adidas Ultraboost Light", "Лёгкие беговые кроссовки", 13900, 10, 22, None),
#     ("Puma Suede Classic", "Классические кеды", 7900, 10, 23, None),
#     ("Levi's 501 Original", "Джинсы прямого кроя", 9900, 10, 24, None),
#     ("Zara Oversize Hoodie", "Уютный худи оверсайз", 4500, 10, 25, None),
# ]

# # -------------------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ --------------------

# def get_seed_from_name(name: str) -> int:
#     """Возвращает целое число от 1 до 100000 на основе хеша названия."""
#     hash_obj = hashlib.md5(name.encode("utf-8"))
#     return int(hash_obj.hexdigest(), 16) % 100000 + 1


# def normalize_url(url: str) -> str:
#     """Немного чистит URL."""
#     return url.strip()


# def is_image_url(url: str) -> bool:
#     """
#     Проверяет, что URL реально отвечает картинкой.
#     Сначала HEAD, затем GET (некоторые серверы HEAD не любят).
#     """
#     try:
#         r = requests.head(url, allow_redirects=True, timeout=REQUEST_TIMEOUT, headers=UA_HEADERS)
#         content_type = (r.headers.get("Content-Type") or "").lower()

#         if r.status_code < 400 and ("image/" in content_type or url.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif"))):
#             return True

#         r = requests.get(url, allow_redirects=True, timeout=REQUEST_TIMEOUT, headers=UA_HEADERS, stream=True)
#         content_type = (r.headers.get("Content-Type") or "").lower()

#         return r.status_code < 400 and ("image/" in content_type or url.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif")))
#     except requests.RequestException:
#         return False


# def wiki_page_image(title: str) -> Optional[str]:
#     """
#     Пытается получить основную картинку статьи через MediaWiki API.
#     Сначала ищет саму страницу, потом вытаскивает pageimages.
#     """
#     try:
#         # 1) Поиск страницы
#         search_params = {
#             "action": "query",
#             "format": "json",
#             "list": "search",
#             "srsearch": title,
#             "srlimit": 1,
#             "srprop": "",
#             "utf8": 1,
#         }
#         search_resp = requests.get(WIKI_API, params=search_params, headers=UA_HEADERS, timeout=REQUEST_TIMEOUT)
#         search_resp.raise_for_status()
#         search_data = search_resp.json()

#         search_results = search_data.get("query", {}).get("search", [])
#         if not search_results:
#             return None

#         page_title = search_results[0]["title"]

#         # 2) Получение картинки страницы
#         image_params = {
#             "action": "query",
#             "format": "json",
#             "prop": "pageimages|images",
#             "titles": page_title,
#             "piprop": "thumbnail|original",
#             "pithumbsize": 800,
#             "pilicense": "any",
#             "imlimit": 10,
#             "redirects": 1,
#             "utf8": 1,
#         }
#         image_resp = requests.get(WIKI_API, params=image_params, headers=UA_HEADERS, timeout=REQUEST_TIMEOUT)
#         image_resp.raise_for_status()
#         data = image_resp.json()

#         pages = data.get("query", {}).get("pages", {})
#         for _, page in pages.items():
#             # Сначала original, потом thumbnail
#             if "original" in page and page["original"].get("source"):
#                 return page["original"]["source"]
#             if "thumbnail" in page and page["thumbnail"].get("source"):
#                 return page["thumbnail"]["source"]

#         return None
#     except (requests.RequestException, ValueError, KeyError):
#         return None


# def commons_file_url(file_name: str) -> str:
#     """
#     Формирует стабильную ссылку на файл Wikimedia Commons.
#     Подходит для SVG/PNG, если файл на Commons точно существует.
#     """
#     safe_name = quote(file_name)
#     return f"https://commons.wikimedia.org/wiki/Special:FilePath/{safe_name}"


# def resolve_image_url(product_name: str, explicit_url: Optional[str] = None) -> str:
#     """
#     Главная логика выбора картинки:
#     1) Проверяем явную ссылку из PRODUCTS.
#     2) Пробуем вернуть картинку из Wikipedia.
#     3) Если не получилось — fallback.
#     """
#     candidates: List[str] = []

#     if explicit_url:
#         candidates.append(normalize_url(explicit_url))

#     # Дополнительный шанс для файлов с Commons, если они были в виде upload.wikimedia...
#     # Берём название файла из URL, если оно там есть.
#     if explicit_url and "upload.wikimedia.org" in explicit_url:
#         filename = explicit_url.split("/")[-1]
#         candidates.append(commons_file_url(filename))

#     # Пробуем найти реальную картинку по статье товара
#     wiki_url = wiki_page_image(product_name)
#     if wiki_url:
#         candidates.append(wiki_url)

#     # Проверяем все кандидаты по очереди
#     for url in candidates:
#         if url and is_image_url(url):
#             return url

#     # Последний запасной вариант
#     return FALLBACK_IMAGE


# def get_or_create_category_map(db):
#     category_map = {}
#     for cat in CATEGORIES:
#         existing = db.query(models.Category).filter(models.Category.name == cat["name"]).first()
#         if not existing:
#             new_cat = models.Category(name=cat["name"], description=cat["description"])
#             db.add(new_cat)
#             db.commit()
#             db.refresh(new_cat)
#             category_map[cat["name"]] = new_cat
#         else:
#             category_map[cat["name"]] = existing
#     return category_map


# def get_or_create_brand_map(db):
#     brand_map = {}
#     for name in BRANDS:
#         existing = db.query(models.Brand).filter(models.Brand.name == name).first()
#         if not existing:
#             brand = models.Brand(name=name)
#             db.add(brand)
#             db.commit()
#             db.refresh(brand)
#             brand_map[name] = brand
#         else:
#             brand_map[name] = existing
#     return brand_map

# # -------------------- ОСНОВНАЯ ФУНКЦИЯ --------------------

# def fill_db():
#     db = SessionLocal()

#     try:
#         # 1. Категории
#         category_map = get_or_create_category_map(db)

#         # 2. Бренды
#         brand_map = get_or_create_brand_map(db)

#         cat_list = list(category_map.values())
#         brand_list = list(brand_map.values())

#         # 3. Товары
#         for item in PRODUCTS:
#             if len(item) == 6:
#                 name, desc, price, cat_idx, brand_idx, image_url = item
#             else:
#                 name, desc, price, cat_idx, brand_idx = item
#                 image_url = None

#             category = cat_list[cat_idx] if 0 <= cat_idx < len(cat_list) else cat_list[0]

#             if 0 <= brand_idx < len(brand_list):
#                 brand = brand_list[brand_idx]
#             else:
#                 brand = random.choice(brand_list)

#             existing_product = db.query(models.Product).filter(
#                 models.Product.name == name,
#                 models.Product.brand_id == brand.id,
#                 models.Product.category_id == category.id
#             ).first()

#             if existing_product:
#                 print(f"Товар '{name}' уже существует, пропускаем.")
#                 continue

#             product = models.Product(
#                 name=name,
#                 description=desc,
#                 price=price,
#                 category_id=category.id,
#                 brand_id=brand.id
#             )
#             db.add(product)
#             db.commit()
#             db.refresh(product)

#             # 4. Картинка
#             resolved_url = resolve_image_url(name, image_url)

#             img = models.ProductImage(
#                 image_url=resolved_url,
#                 product_id=product.id
#             )
#             db.add(img)
#             db.commit()

#             if resolved_url == FALLBACK_IMAGE:
#                 print(f"  ⚠️ Для '{name}' не нашлась реальная картинка, поставлен fallback.")
#             else:
#                 print(f"  📷 Картинка найдена для: {name}")

#             print(f"✅ Добавлен товар: {product.name} (ID {product.id}), цена {price} ₽")

#     finally:
#         db.close()

#     print("🎉 Заполнение БД завершено!")

# if __name__ == "__main__":
#     fill_db()


import random
import hashlib
import re
from typing import Optional
from urllib.parse import quote_plus

import requests

from app.database import SessionLocal
from app import models

# -------------------- НАСТРОЙКИ --------------------
UA_HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; fill-db/3.0; +https://example.com)"
}
REQUEST_TIMEOUT = 8

# -------------------- ДАННЫЕ --------------------
CATEGORIES = [
    {"name": "Смартфоны", "description": "Мобильные телефоны и аксессуары"},
    {"name": "Ноутбуки", "description": "Портативные компьютеры и ультрабуки"},
    {"name": "Наушники", "description": "Беспроводные, проводные, TWS"},
    {"name": "Умные часы", "description": "Смарт-часы и фитнес-браслеты"},
    {"name": "Телевизоры", "description": "Телевизоры, мониторы, проекторы"},
    {"name": "Бытовая техника", "description": "Холодильники, стиральные машины, пылесосы"},
    {"name": "Комплектующие", "description": "Процессоры, видеокарты, ОЗУ, SSD"},
    {"name": "Аудио", "description": "Колонки, плееры, звуковые карты"},
    {"name": "Фототехника", "description": "Фотоаппараты, объективы, штативы"},
    {"name": "Игровые приставки", "description": "PlayStation, Xbox, Nintendo Switch"},
    {"name": "Одежда", "description": "Спортивная и повседневная одежда"},
]

BRANDS = [
    "Apple", "Samsung", "Xiaomi", "Huawei", "Google", "Microsoft",
    "Lenovo", "Asus", "Dell", "HP", "Acer", "Logitech",
    "JBL", "Bose", "Sony", "Beats", "Canon", "Nikon", "GoPro",
    "Nintendo", "PlayStation", "Xbox", "SteelSeries", "Razer",
    "Nike", "Adidas", "Puma", "Reebok", "Levi's", "Zara",
]

# Товары: (название, описание, цена, индекс категории, индекс бренда, url_или_None)
PRODUCTS = [
    # Смартфоны (0)
    ("iPhone 16 Pro Max", "Флагман с титановым корпусом и AI-чипом", 129900, 0, 0,
     "https://upload.wikimedia.org/wikipedia/commons/7/7c/IPhone_16_Vector.svg"),
    ("Samsung Galaxy S25 Ultra", "Мощный Android с S Pen", 119900, 0, 1,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Samsung_Galaxy_S24_Ultra.svg/800px-Samsung_Galaxy_S24_Ultra.svg.png"),
    ("Xiaomi 14T Pro", "Доступный флагман с отличной камерой", 79900, 0, 2, None),
    ("Google Pixel 9 Pro", "Лучшая камера и чистый Android", 99900, 0, 4, None),
    ("Huawei P60 Pro", "Китайский флагман с крутым зумом", 89900, 0, 3, None),
    ("OnePlus 12", "Быстрый и стильный смартфон", 74900, 0, -1, None),

    # Ноутбуки (1)
    ("MacBook Pro 16 M3", "Мощный ноутбук для профессионалов", 249900, 1, 0,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/MacBook_Pro_16%22_Space_Black.svg/800px-MacBook_Pro_16%22_Space_Black.svg.png"),
    ("Dell XPS 15", "Ультрабук с безрамочным экраном", 189900, 1, 6, None),
    ("Lenovo ThinkPad X1 Carbon", "Надёжный бизнес-ноутбук", 169900, 1, 5, None),
    ("ASUS ROG Zephyrus G14", "Игровой ноутбук с Ryzen 9", 159900, 1, 7, None),
    ("HP Spectre x360", "Трансформер с отличным дисплеем", 139900, 1, 8, None),
    ("Acer Swift 5", "Лёгкий и тонкий ультрабук", 89900, 1, 9, None),

    # Наушники (2)
    ("Sony WH-1000XM6", "Лучшие наушники с шумодавом", 39900, 2, 12, None),
    ("Bose QuietComfort 45", "Комфортные наушники с отличным звуком", 32900, 2, 11, None),
    ("Apple AirPods Pro 2", "TWS с активным шумодавом", 24900, 2, 0,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/AirPods_Pro_2.svg/800px-AirPods_Pro_2.svg.png"),
    ("Samsung Galaxy Buds3 Pro", "TWS с поддержкой 360 аудио", 19900, 2, 1, None),
    ("JBL Tune 770NC", "Доступные наушники с шумодавом", 12900, 2, 10, None),

    # Умные часы (3)
    ("Apple Watch Ultra 2", "Спортивные часы с титановым корпусом", 79900, 3, 0,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Apple_Watch_Ultra_2.svg/800px-Apple_Watch_Ultra_2.svg.png"),
    ("Samsung Galaxy Watch 6 Classic", "Элегантные часы с вращающимся безелем", 49900, 3, 1, None),
    ("Garmin Fenix 8", "GPS-часы для экстремального спорта", 99900, 3, -1, None),
    ("Xiaomi Watch S3", "Бюджетные смарт-часы с AMOLED", 14900, 3, 2, None),

    # Телевизоры (4)
    ("Samsung Neo QLED 85", "8K TV с технологией Mini-LED", 899900, 4, 1, None),
    ("Sony OLED XR A95L", "Органический OLED с потрясающим цветом", 799900, 4, 12, None),
    ("LG C3 OLED 65", "Популярный OLED-телевизор", 349900, 4, -1, None),
    ("TCL Mini-LED 75", "Доступный большой телевизор", 199900, 4, -1, None),

    # Бытовая техника (5)
    ("Samsung Bespoke Refrigerator", "Холодильник с индивидуальным дизайном", 299900, 5, 1, None),
    ("LG Styler", "Паровой шкаф для одежды", 69900, 5, -1, None),
    ("Dyson V15 Detect", "Мощный беспроводной пылесос", 79900, 5, -1, None),
    ("Bosch Serie 8 Dishwasher", "Посудомоечная машина с интеллектом", 89900, 5, -1, None),

    # Комплектующие (6)
    ("Intel Core i9-14900K", "Флагманский процессор для ПК", 59900, 6, -1, None),
    ("AMD Ryzen 9 7950X", "Мощный процессор для энтузиастов", 54900, 6, -1, None),
    ("NVIDIA RTX 4090", "Видеокарта для игр и AI", 199900, 6, -1, None),
    ("Samsung SSD 990 Pro 2TB", "Скоростной NVMe-накопитель", 24900, 6, 0, None),
    ("G.Skill Trident Z DDR5", "Игровая память 32 ГБ", 15900, 6, -1, None),

    # Аудио (7)
    ("Sonos Era 300", "Умная колонка с пространственным звуком", 44900, 7, -1, None),
    ("JBL Flip 6", "Водонепроницаемая портативная колонка", 9900, 7, 10, None),
    ("FiiO M17", "Высококлассный аудиоплеер", 89900, 7, -1, None),
    ("SteelSeries Arctic Nova Pro", "Игровая гарнитура с ANC", 32900, 7, 20, None),

    # Фототехника (8)
    ("Canon EOS R6 Mark II", "Беззеркальная камера для профессионалов", 249900, 8, 14, None),
    ("Nikon Z8", "Флагманская беззеркалка", 399900, 8, 15, None),
    ("Sony FX30", "Кино-камера для видеографов", 189900, 8, 12, None),
    ("GoPro Hero 12 Black", "Экшн-камера для съёмки в движении", 39900, 8, 16, None),

    # Игровые приставки (9)
    ("PlayStation 5 Pro", "Обновлённая версия PS5 с более мощным GPU", 89900, 9, 18,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/PlayStation_5_and_DualSense_controller.svg/800px-PlayStation_5_and_DualSense_controller.svg.png"),
    ("Xbox Series X", "Самая мощная игровая консоль", 69900, 9, 19,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Xbox_Series_X.svg/800px-Xbox_Series_X.svg.png"),
    ("Nintendo Switch OLED", "Гибридная консоль с ярким экраном", 39900, 9, 17,
     "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Nintendo_Switch.svg/800px-Nintendo_Switch.svg.png"),
    ("Steam Deck OLED", "Портативный ПК для игр", 49900, 9, -1, None),

    # Одежда (10)
    ("Nike Air Max 2025", "Кроссовки с воздушной подушкой", 15900, 10, 21, None),
    ("Adidas Ultraboost Light", "Лёгкие беговые кроссовки", 13900, 10, 22, None),
    ("Puma Suede Classic", "Классические кеды", 7900, 10, 23, None),
    ("Levi's 501 Original", "Джинсы прямого кроя", 9900, 10, 24, None),
    ("Zara Oversize Hoodie", "Уютный худи оверсайз", 4500, 10, 25, None),
]

# -------------------- УТИЛИТЫ ДЛЯ КАРТИНОК --------------------
def get_seed_from_name(name: str) -> int:
    h = hashlib.md5(name.encode("utf-8")).hexdigest()
    return int(h, 16) % 100000 + 1


def is_image_url(url: str) -> bool:
    """Быстрая проверка, что URL отдаёт картинку (HEAD-запрос)"""
    try:
        r = requests.head(url, allow_redirects=True, timeout=REQUEST_TIMEOUT, headers=UA_HEADERS)
        ct = (r.headers.get("Content-Type") or "").lower()
        if r.status_code < 400 and ("image/" in ct or url.lower().endswith((".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif"))):
            return True
    except Exception:
        pass
    return False


def clean_name(name: str) -> str:
    """Убирает годы и лишние спецсимволы для поиска"""
    name = re.sub(r'\b20\d{2}\b', '', name)      # удалить годы
    name = re.sub(r'[®™]', '', name)             # удалить символы
    return ' '.join(name.split())                # убрать лишние пробелы


# --- 1. DummyJSON (умный перебор) ---
def get_dummyjson_image(product_name: str, brand_name: str = "") -> Optional[str]:
    queries = [product_name]
    if brand_name:
        queries.append(f"{brand_name} {product_name.split()[-1]}" if len(product_name.split()) > 1 else brand_name)
        queries.append(brand_name)
    # чистые варианты
    queries = list(dict.fromkeys([clean_name(q) for q in queries if q.strip()]))  # уникальные, без пустых

    for q in queries:
        try:
            resp = requests.get(
                "https://dummyjson.com/products/search",
                params={"q": q, "limit": 5},
                timeout=REQUEST_TIMEOUT
            )
            if resp.status_code != 200:
                continue
            products = resp.json().get("products", [])
            for p in products:
                img = p.get("thumbnail")
                if img and is_image_url(img):
                    return img
        except Exception:
            continue
    return None


# --- 2. Wikipedia (умный) ---
def get_wikipedia_image(product_name: str) -> Optional[str]:
    queries = [product_name, clean_name(product_name)]
    # ещё только первое слово (бренд)
    parts = product_name.split()
    if parts:
        queries.append(parts[0])
    queries = list(dict.fromkeys([q for q in queries if q.strip()]))

    for q in queries:
        try:
            # поиск статьи
            sr = requests.get(
                "https://en.wikipedia.org/w/api.php",
                params={"action": "query", "list": "search", "srsearch": q, "format": "json"},
                timeout=REQUEST_TIMEOUT
            )
            pages = sr.json().get("query", {}).get("search", [])
            if not pages:
                continue
            title = pages[0]["title"]

            # изображение
            ir = requests.get(
                "https://en.wikipedia.org/w/api.php",
                params={
                    "action": "query", "prop": "pageimages",
                    "titles": title, "piprop": "thumbnail",
                    "pithumbsize": 800, "format": "json"
                },
                timeout=REQUEST_TIMEOUT
            )
            for p in ir.json().get("query", {}).get("pages", {}).values():
                thumb = p.get("thumbnail")
                if thumb and thumb.get("source"):
                    src = thumb["source"]
                    if is_image_url(src):
                        return src
        except Exception:
            continue
    return None


# --- 3. Lorem Picsum (100% надёжно) ---
def get_picsum_image(name: str) -> str:
    seed = get_seed_from_name(name)
    return f"https://picsum.photos/seed/{seed}/600/600"


# --- ГЛАВНЫЙ РЕЗОЛВЕР ---
def resolve_image_url(product_name: str, original_url: Optional[str] = None,
                      brand_name: str = "") -> str:
    print(f"  Поиск картинки для: {product_name}")

    # 0. Явная ссылка
    if original_url and is_image_url(original_url):
        print("    ✅ Явная ссылка")
        return original_url

    # 1. DummyJSON
    url = get_dummyjson_image(product_name, brand_name)
    if url:
        print("    ✅ DummyJSON")
        return url

    # 2. Wikipedia
    url = get_wikipedia_image(product_name)
    if url:
        print("    ✅ Wikipedia")
        return url

    # 3. Picsum (всегда работает)
    url = get_picsum_image(product_name)
    print("    ✅ Picsum")
    return url


# -------------------- ЗАПОЛНЕНИЕ БД --------------------
def fill_db():
    db = SessionLocal()
    try:
        # Категории
        cat_map = {}
        for c in CATEGORIES:
            existing = db.query(models.Category).filter(models.Category.name == c["name"]).first()
            if not existing:
                new_cat = models.Category(name=c["name"], description=c["description"])
                db.add(new_cat)
                db.commit()
                db.refresh(new_cat)
                cat_map[c["name"]] = new_cat
            else:
                cat_map[c["name"]] = existing
        cat_list = list(cat_map.values())

        # Бренды
        brand_map = {}
        for b_name in BRANDS:
            existing = db.query(models.Brand).filter(models.Brand.name == b_name).first()
            if not existing:
                brand = models.Brand(name=b_name)
                db.add(brand)
                db.commit()
                db.refresh(brand)
                brand_map[b_name] = brand
            else:
                brand_map[b_name] = existing
        brand_list = list(brand_map.values())

        # Товары
        for item in PRODUCTS:
            name, desc, price, cat_idx, brand_idx, *rest = item
            img_url_candidate = rest[0] if rest else None

            category = cat_list[cat_idx] if 0 <= cat_idx < len(cat_list) else cat_list[0]

            if 0 <= brand_idx < len(brand_list):
                brand = brand_list[brand_idx]
            else:
                brand = random.choice(brand_list)

            # Проверка на дубликат
            existing_product = db.query(models.Product).filter(
                models.Product.name == name,
                models.Product.brand_id == brand.id,
                models.Product.category_id == category.id
            ).first()
            if existing_product:
                print(f"⏩ Товар '{name}' уже существует, пропущен.")
                continue

            product = models.Product(
                name=name,
                description=desc,
                price=price,
                category_id=category.id,
                brand_id=brand.id
            )
            db.add(product)
            db.commit()
            db.refresh(product)

            # Получение и сохранение картинки
            final_url = resolve_image_url(name, img_url_candidate, brand_name=brand.name)
            img = models.ProductImage(image_url=final_url, product_id=product.id)
            db.add(img)
            db.commit()

            print(f"✅ {product.name} — {price} ₽")

    finally:
        db.close()

    print("\n🎉 База данных успешно заполнена!")


if __name__ == "__main__":
    fill_db()