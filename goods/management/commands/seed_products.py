import requests
from random import randint, choice
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from goods.models import Products, Categories


class Command(BaseCommand):
    help = "Створює товари з фото для магазину Теремок"

    def download_image(self, query, filename):
        url = f"https://loremflickr.com/800/600/{query}"

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return ContentFile(response.content, name=filename)
        except Exception:
            return None

        return None

    def handle(self, *args, **kwargs):
        categories = list(Categories.objects.all().order_by("id"))

        if not categories:
            self.stdout.write(self.style.ERROR("Спочатку створи категорії"))
            return

        products = [
            ("Подушка ортопедична", "bedroom"),
            ("Ліжко двоспальне", "bedroom"),
            ("Ковдра зимова", "bedroom"),
            ("Матрац ортопедичний", "bedroom"),
            ("Постільна білизна", "bedroom"),

            ("Рушник банний", "bathroom"),
            ("Дзеркало для ванної", "bathroom"),
            ("Килимок для ванної", "bathroom"),
            ("Дозатор для мила", "bathroom"),
            ("Шафка для ванної", "bathroom"),

            ("Набір тарілок", "kitchen"),
            ("Сковорода антипригарна", "kitchen"),
            ("Чайник електричний", "kitchen"),
            ("Набір каструль", "kitchen"),
            ("Контейнер для продуктів", "kitchen"),

            ("Автомобільний органайзер", "car accessories"),
            ("Автомобільний пилосос", "car accessories"),
            ("Ароматизатор для авто", "car accessories"),

            ("Офісний стілець", "office chair"),
            ("Письмовий стіл", "office desk"),
            ("Настільна лампа", "office lamp"),

            ("Садовий ліхтар", "garden"),
            ("Садова лійка", "garden"),
            ("Садові рукавички", "garden"),

            ("Засіб для миття підлоги", "cleaning product"),
            ("Пральний порошок", "cleaning product"),
            ("Засіб для миття посуду", "cleaning product"),

            ("Шампунь для волосся", "hygiene"),
            ("Гель для душу", "hygiene"),
            ("Зубна паста", "hygiene"),

            ("Конструктор дитячий", "toys"),
            ("М'яка іграшка", "toys"),
            ("Настільна гра", "toys"),
        ]

        for i in range(1, 1001):
            product_name, image_query = products[(i - 1) % len(products)]
            category = categories[(i - 1) % len(categories)]

            product = Products(
                name=product_name,
                slug=f"product-{i}",
                description=f"{product_name} — якісний товар для дому в інтернет-магазині «Теремок».",
                price=randint(100, 15000),
                discount=choice([0, 0, 0, 5, 10, 15]),
                quantity=randint(1, 50),
                category=category,
            )

            image = self.download_image(image_query, f"product-{i}.jpg")

            if image:
                product.image.save(f"product-{i}.jpg", image, save=False)

            product.save()

            self.stdout.write(f"Створено товар {i}: {product_name}")

        self.stdout.write(self.style.SUCCESS("Успішно створено 1000 товарів з фото"))