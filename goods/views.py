from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
        'title':'Home- Каталог',
        'goods': [{"image": "images/cover.jpg",
                  "name": "poduchka",
                  "description":"мягкая такая вау",
                  "price": 50.00,


        },

        {"image": "images/наволочка другая.png",
         "name": "наволочка",
         "description": "чистая",
         "price": 150.00,

         },

        {"image": "images/navolochka.png",
        "name": "наволочка другая",
        "description": "чистая тоже",
        "price": 110.00,

     }

    ]
}
    return render(request, 'goods/catalog.html',context)


def product(request):
    return render(request, 'goods/product.html')