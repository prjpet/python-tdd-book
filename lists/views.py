from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')

    items = Item.objects.all()
# long version of creating a new item in db:
#    item = Item()
#    item.text = request.POST.get('item_text','')
#    item.save()

    return render(request, 'home.html', {'items': items})
