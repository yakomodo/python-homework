import re
import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = re.sub(r'<[^>]+>', '', html)
    
    # Додаткове: Прибираємо порожні
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))

delete_html_tags('draft.html', 'cleaned.txt')
print('Готово!')