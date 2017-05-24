from django.shortcuts import render


def item_list(request):
    return render(request, 'groceries/item_list.html', {})

