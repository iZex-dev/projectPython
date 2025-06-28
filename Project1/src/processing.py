from typing import List, Dict, Optional

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.
    Возвращает новый список, где 'state' == state.
    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    По умолчанию сортировка по убыванию (descending=True).
    """
    return sorted(data, key=lambda x: x.get('date', ''), reverse=descending)