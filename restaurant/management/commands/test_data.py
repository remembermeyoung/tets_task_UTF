from django.core.management import BaseCommand

from restaurant.models import Food, FoodCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        cats_name = ['Напитки', 'Выпечка', 'Мясо', 'Другое']
        cats = [FoodCategory(name_ru=name) for name in cats_name]
        FoodCategory.objects.bulk_create(cats)

        drinks = FoodCategory.objects.get(name_ru='Напитки')
        bakery = FoodCategory.objects.get(name_ru='Выпечка')
        meat = FoodCategory.objects.get(name_ru='Мясо')

        Food.objects.create(category=drinks, name_ru='Чай', description_ru='Описание чая',
                            code=123, cost=100, is_publish=True)
        Food.objects.create(category=drinks, name_ru='Газировка', description_ru='Описание газировки',
                            code=123, cost=200, is_publish=False)

        Food.objects.create(category=bakery, name_ru='Булочка', description_ru='Описание булочки',
                            code=123, cost=100, is_publish=True)
        Food.objects.create(category=bakery, name_ru='Сметанник', description_ru='Описание сметанника',
                            code=123, cost=200, is_publish=False)

        Food.objects.create(category=meat, name_ru='Стейк', description_ru='Описание стейка',
                            code=123, cost=200, is_publish=False)
        Food.objects.create(category=meat, name_ru='Стейк2', description_ru='Описание стейка2',
                            code=123, cost=200, is_publish=False)

        print('Скрипт был запущен')
