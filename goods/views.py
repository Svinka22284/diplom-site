from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
        'title':'Home- Каталог',
        'goods': [{"image": "images/cover.jpg",
                  "name": "Подушка",
                  "description":"М'яка ортопедична подушка",
                  "price": 50.00,


    },


    {
        "image": "images/blanket.png",
        "name": "Ковдра",
        "description": "Тепла зимова ковдра",
        "price": 950.00
    },

    {
        "image": "images/bed.png",
        "name": "Двоспальне ліжко",
        "description": "Ліжко з дерев'яним каркасом",
        "price": 8500.00
    },
    {
        "image": "images/mattress.png",
        "name": "Матрац",
        "description": "Ортопедичний матрац",
        "price": 6200.00
    },

    {
        "image": "images/towel.png",
        "name": "Рушник",
        "description": "Махровий рушник",
        "price": 250.00
    },
    {
        "image": "images/shower_curtain.png",
        "name": "Шторка для душу",
        "description": "Водонепроникна шторка",
        "price": 380.00
    },

    {
        "image": "images/office_chair.png",
        "name": "Офісне крісло",
        "description": "Зручне крісло для роботи",
        "price": 4200.00
    },
    {
        "image": "images/desk_lamp.png",
        "name": "Настільна лампа",
        "description": "Світлодіодна лампа",
        "price": 650.00
    },

    {
        "image": "images/pan.png",
        "name": "Сковорода",
        "description": "Антипригарна сковорода",
        "price": 900.00
    },
    {
        "image": "images/dishes.png",
        "name": "Набір посуду",
        "description": "Столовий набір на 6 персон",
        "price": 2100.00
    },

    {
        "image": "images/storage_box.png",
        "name": "Контейнер для зберігання",
        "description": "Пластиковий контейнер з кришкою",
        "price": 320.00
    },

    {
        "image": "images/curtains.png",
        "name": "Штори",
        "description": "Щільні штори для вітальні",
        "price": 1800.00
    },

    {
        "image": "images/garden_chair.png",
        "name": "Садове крісло",
        "description": "Пластикове крісло для тераси",
        "price": 950.00
    },

    {
        "image": "images/carpet.png",
        "name": "Килим",
        "description": "М'який килим для кімнати",
        "price": 2700.00
    },

    {
        "image": "images/christmas_tree.png",
        "name": "Штучна ялинка",
        "description": "Новорічна ялинка 180 см",
        "price": 3200.00
    },

    {
        "image": "images/air_fryer.png",
        "name": "Аерофрайєр",
        "description": "Фритюрниця без олії",
        "price": 4500.00
    },

    {
        "image": "images/coffee_maker.png",
        "name": "Кавоварка",
        "description": "Крапельна кавоварка",
        "price": 2300.00
    }
    ]
}
    return render(request, 'goods/catalog.html',context)


def product(request):
    return render(request, 'goods/product.html')