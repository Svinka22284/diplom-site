import os
from random import randint, choice

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from goods.models import Products, Categories


class Command(BaseCommand):
    help = "Створює товари з локальними фото для магазину Теремок"

    def handle(self, *args, **kwargs):
        images_dir = settings.BASE_DIR / "media" / "demo_products"

        if not images_dir.exists():
            self.stdout.write(self.style.ERROR("Створи папку media/demo_products і додай туди фото"))
            return

        images = [
            file for file in os.listdir(images_dir)
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".jfif"))
        ]

        if not images:
            self.stdout.write(self.style.ERROR("У папці media/demo_products немає фото"))
            return

        products = {
            "Спальня": ["Подушка ортопедична", "Ліжко двоспальне", "Ковдра зимова", "Матрац ортопедичний", "Постільна білизна"],
            "Ванна": ["Рушник банний", "Дзеркало для ванної", "Килимок для ванної", "Дозатор для мила", "Шафка для ванної"],
            "Кухня": ["Набір тарілок", "Сковорода антипригарна", "Чайник електричний", "Набір каструль", "Контейнер для продуктів"],
            "Автотовари": ["Автомобільний органайзер", "Автомобільний пилосос", "Ароматизатор для авто", "Автомобільний компресор", "Чохол на кермо"],
            "Офіс": ["Офісний стілець", "Письмовий стіл", "Настільна лампа", "Органайзер для документів", "Полиця для книг"],
            "Для саду": ["Садовий ліхтар", "Садова лійка", "Садові рукавички", "Садовий шланг", "Секатор садовий"],
            "Побутова хімія": ["Засіб для миття підлоги", "Пральний порошок", "Засіб для миття посуду", "Засіб для скла", "Універсальний очищувач"],
            "Гігієна та догляд": ["Шампунь для волосся", "Гель для душу", "Зубна паста", "Рідке мило", "Бальзам для волосся"],
            "Іграшки для дітей": ["Конструктор дитячий", "М'яка іграшка", "Настільна гра", "Іграшковий автомобіль", "Лялька дитяча"],
        }

        created_count = 0

        for category_name, product_list in products.items():
            try:
                category = Categories.objects.get(name=category_name)
            except Categories.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Категорію '{category_name}' не знайдено. Пропускаю."))
                continue

            for i in range(1, 101):
                product_name = product_list[(i - 1) % len(product_list)]

                image_name = images[(created_count) % len(images)]
                image_path = images_dir / image_name

                product = Products(
                    name=product_name,
                    slug=f"{slugify(product_name)}-{category.id}-{i}",
                    description=f"{product_name} — якісний товар для дому.",
                    price=randint(100, 15000),
                    discount=choice([0, 0, 0, 5, 10, 15]),
                    quantity=randint(1, 50),
                    category=category,
                )

                with open(image_path, "rb") as img:
                    product.image.save(
                        f"product-{category.id}-{i}-{image_name}",
                        File(img),
                        save=False
                    )

                product.save()
                created_count += 1

                self.stdout.write(f"Створено товар {created_count}: {product_name}")

        self.stdout.write(self.style.SUCCESS(f"Успішно створено {created_count} товарів з локальними фото"))