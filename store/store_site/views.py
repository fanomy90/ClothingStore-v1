from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, FormView
from .utils import DataMixin
from .models import *

# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
# ]
#Статический контент
# def home(request):
#     storItems = Store.objects.filter(is_published=1)
#     data = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'storItems': storItems,
#         'cat_selected': 0,
#     }
#     return render(request, 'store_site/index.html', context=data)
def index(request):
    #t = render_to_string('news_site/index.html')
    #return HttpResponse(t)
    #data = {'title': 'Главная страница',
    #        'menu': menu,
    #        }
    #return render(request, 'news_site/index.html', context=data)
    return render(request, 'store_site/index.html', {'title': 'Главная страница'})
def about(request):
    return render(request, 'store_site/about.html', {'title': 'О сайте', 'menu': menu})
def contact(request):
    return render(request, 'store_site/contact.html', {'title': 'Контакты'})
def login(request):
    return render(request, 'store_site/login.html', {'title': 'Вход'})
#Динамический контент
# def storeItem(request):
#     return render(request, 'store_site/storeItem.html', {'title': 'Товар'})
# def storeCat(request):
#     return render(request, 'store_site/storeCat.html', {'title': 'Каталог товаров'})

class storeItem(DataMixin, DetailView):
    model = Store
    template_name = 'store_site/storeItem.html'
    slug_url_kwarg = 'storeItem_slug'
    context_object_name = 'storeItem'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #скрываем карусель
        show_slider_header = False
        # Получаем объект новости, для которой пытаемся получить категорию
        storeItem = self.get_object()
        # Теперь, используя объект новости, получаем связанную с ней категорию
        cat_selected = storeItem.cat
        c_def = self.get_user_context(
                title=context['storeItem'],
                cat_selected=cat_selected, # Преобразуем cat_selected в целое число
                show_slider_header=show_slider_header) 
        return dict(list(context.items()) + list(c_def.items()))
        
class storeCat(DataMixin, ListView):
    model = Store
    template_name = 'store_site/index.html'
    context_object_name = 'storeItems'
    # вывод ошибки 404 при обращении к несуществующей статьи
    def get_queryset(self):
        return Store.objects.filter(cat__slug=self.kwargs['storeCat_slug'], is_published=True)
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #показываем карусель
        show_slider_header = True
        # вызываем метод из базового класса DataMixit файла utils
        cat_selected = context['storeItems'][0].cat  # Присваиваем объект категории
        c_def = self.get_user_context(
            title='Категория - '+str(context['storeItems'][0].cat),
            cat_selected=cat_selected,
            show_slider_header=show_slider_header) #добавил кусок после cat_selected
        return dict(list(context.items())+list(c_def.items()))

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")