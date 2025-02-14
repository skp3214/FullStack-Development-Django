from django.shortcuts import render


def foodMenuList(request):
    foodmenu = [
        {'itemname': 'biryani', 'price': 100, 'GST': 12,'size':'large','image':'images/coffee.jpg'},
        {'itemname': 'juice', 'price': 100, 'GST': 18,'size':'small','image':'images/coffee.jpg'},
        {'itemname': 'coffee', 'price': 50, 'GST': 5,'size':'medium','image':'images/coffee.jpg'},
        {'itemname': 'tea', 'price': 150, 'GST': 10,'size':'large','image':'images/coffee.jpg'},
    ]
    
    return render(request,'food.html',{'foodmenu':foodmenu})
