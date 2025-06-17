from django import template
from typing import Dict

from ..models import MenuModel


register = template.Library()

@register.inclusion_tag('app/menu_template.html', takes_context=True)
def draw_menu(context, menu_name: str) -> Dict[str, any]:
    """
    Генерирует древовидное меню с открытием активного пункта.

    Args:
        context: Контекст шаблона Django, должен содержать объект request
        menu_name: Имя меню для отображения (из поля menu_name модели)

    Returns:
        Словарь с данными для рендеринга шаблона:
        {
            'menu_data': List[Dict] - древовидная структура меню,
            'request': HttpRequest - объект запроса
        }

    Пример использования в шаблоне:
        {% load menu_tags %}
        {% draw_menu 'main_menu' %}
    """
    request = context['request']
    items = MenuModel.objects.filter(
        menu_name=menu_name,
        parent=None,
    ).prefetch_related('children')

    def process_items(items):
        """
        Рекурсивно обрабатывает элементы меню, формируя древовидную структуру.

        Args:
            items: Список элементов меню

        Returns:
            Список узлов меню с дочерними элементами и полями активности
        """
        result = []
        for item in items:
            node = {
                'item': item,  # Оригинальный объект модели
                'is_active': (item.get_url() == request.path_info) ,
                'has_active_children': False,
                'children': []
            }
            
            if item.children.exists():
                node['children'] = process_items(item.children.all())
                node['has_active_children'] = any(
                    child['is_active'] or child['has_active_children']
                    for child in node['children']
                )
            
            result.append(node)
        return result
    
    menu_data = process_items(items)

    return {
        'menu_data': menu_data,
        'request': request
    }