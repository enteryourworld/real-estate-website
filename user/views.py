from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Catalog,Photo
from .forms import CatologForm,PhotoForm
from django.shortcuts import render, redirect, get_object_or_404
def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username= username, password=password)
        if user is not None:
            login(request,user=user)
            return redirect('mainpage')
    return render(request,'user/reg.html')
@login_required
def mainpage(request):
    catalog_items = Catalog.objects.all()  # Получаем все объекты


    cities = ['Солоники', 'Лазаревское', 'Сочи','Сорт участок','Волконка','Сосновый бор','Алексеевское','Татьяновка','Мамедова щель','Аше','Макопсе','Вишнёвка','Тихоновка','Калиновка']  # ,Сорт участок, волконка, салоники, сосновый бор, лазаревское, Алексеевское, Татьяновка, Мамедова щель, Аше, Макопсе, Вишнёвка, Тихоновка, Калиновка.
    types = ['Дом', 'Гостиница', 'Квартира','Земельный участок','Домовладение','Комната']  # Список доступных типов объектов

    city = request.GET.get('city')  # Получаем выбранный город
    type = request.GET.get('type')  # Получаем выбранный тип

    items = Catalog.objects.all()  # Получаем все объекты

# Фильтруем по выбранному городу и типу
    if city:
        items = items.filter(city__iexact=city)  # Фильтруем по городу
    if type:
        items = items.filter(type__iexact=type)  # Фильтруем по типу
    catalog_items = [item.photos.all() for item in items]
    return render(request, 'user/mainpage.html', {'items': items,'catalog_items': catalog_items, 'cities': cities, 'types': types,'catalog_items': catalog_items})

@login_required
def item_create(request):
    if request.method == "POST":
        catalog_form = CatologForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)

        if catalog_form.is_valid() and photo_form.is_valid():
            catalog = catalog_form.save()  # Сохраняем объект Catalog

            # Обрабатываем загруженные изображения
            images = request.FILES.getlist('images')  # Получаем список загруженных файлов
            for img in images:
                Photo.objects.create(catalog=catalog, image=img)  # Создаём объект Photo

            return redirect('mainpage')
    else:
        catalog_form = CatologForm()
        photo_form = PhotoForm()

    return render(request, 'user/createpost.html', {
        'catalog_form': catalog_form,
        'photo_form': photo_form,
    })
@login_required
def item_update(request, pk):
    item = get_object_or_404(Catalog, pk=pk)

    if request.method == "POST":
        catalog_form = CatologForm(request.POST, instance=item)
        photo_form = PhotoForm(request.POST, request.FILES)

        if catalog_form.is_valid() and photo_form.is_valid():
            catalog = catalog_form.save()  # Сохраняем объект Catalog

            # Обрабатываем загруженные изображения
            images = request.FILES.getlist('images')  # Получаем список загруженных файлов
            for img in images:
                Photo.objects.create(catalog=catalog, image=img)  # Создаём объект Photo

            return redirect('mainpage')
    else:
        catalog_form = CatologForm(instance=item)
        photo_form = PhotoForm()

    return render(request, 'user/item_list.html', {
        'catalog_form': catalog_form,
        'photo_form': photo_form,
        'item': item,
    })
@login_required
def item_delete(request, pk):
    item = get_object_or_404(Catalog, pk=pk)
    if request.method == 'POST':
        item.delete()  # Здесь вызывается переопределенный метод delete
        return redirect('mainpage')
    return render(request, 'item_form.html', {'item': item})