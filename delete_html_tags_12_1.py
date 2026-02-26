import re
import codecs
import os

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = re.sub(r'<[^>]+>', '', html)
    
    # Додаткове: прибираємо порожні
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))

# тест
def test_delete_html_tags():
    # Тест 1: простий HTML
    test_html = '<p>Hello World</p>'
    with codecs.open('test_input.html', 'w', 'utf-8') as f:
        f.write(test_html)
    
    delete_html_tags('test_input.html', 'test_output.txt')
    
    with codecs.open('test_output.txt', 'r', 'utf-8') as f:
        result = f.read()
    
    assert result == 'Hello World', f'Test 1 failed: {result}'
    print('✓ Test 1 passed: Simple HTML tag removal')
    
    # Тест 2: множинні теги
    test_html2 = '<div><h1>Title</h1><p>Content</p></div>'
    with codecs.open('test_input.html', 'w', 'utf-8') as f:
        f.write(test_html2)
    
    delete_html_tags('test_input.html', 'test_output.txt')
    
    with codecs.open('test_output.txt', 'r', 'utf-8') as f:
        result = f.read()
    
    assert 'Title' in result and 'Content' in result, f'Test 2 failed: {result}'
    assert '<' not in result and '>' not in result, 'Test 2 failed: Tags still present'
    print('✓ Test 2 passed: Multiple tags removal')
    
    # Тест 3: порожні рядки прибрані
    test_html3 = '<p>Line1</p>\n\n\n<p>Line2</p>'
    with codecs.open('test_input.html', 'w', 'utf-8') as f:
        f.write(test_html3)
    
    delete_html_tags('test_input.html', 'test_output.txt')
    
    with codecs.open('test_output.txt', 'r', 'utf-8') as f:
        result = f.read()
    
    lines = result.split('\n')
    assert all(line.strip() for line in lines), 'Test 3 failed: Empty lines present'
    print('✓ Test 3 passed: Empty lines removed')
    
    # видаляєм тестові файли
    os.remove('test_input.html')
    os.remove('test_output.txt')
    
    print('\n✅ All tests passed!')

# запускаєм
if __name__ == '__main__':
    test_delete_html_tags()
    
    print('\nОбробка draft.html...')
    delete_html_tags('draft.html', 'cleaned.txt')
    print('Готово!')
