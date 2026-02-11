from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q
from goods.models import Products

def q_search(search_text):
    if search_text.isdigit() and len(search_text) <= 5:
        return Products.objects.filter(id=int(search_text))

    vector = SearchVector('name', 'description')
    query = SearchQuery(search_text)

    result = (
        Products.objects
        .annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by('-rank')
    )

    result = result.annotate(
        headline=SearchHeadline(
            'name',
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel='</span>',
        ),
        bodyline=SearchHeadline(
            'description',
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel='</span>',
        )
    )

    return result
    #keywords=[word for word in query.split() if len(word) > 2]
    #q_object=Q()

    #for token in keywords:
        #q_object |= Q(description__icontains=token)
        #q_object |= Q(name__icontains=token)
    #return Products.objects.filter(q_object)