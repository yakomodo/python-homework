import re
import codecs
import os
import unittest

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    cleaned = re.sub(r'<[^>]+>', '', html)
    lines = [line.strip() for line in cleaned.split('\n') if line.strip()]
    
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(lines))

class TestDeleteHtmlTags(unittest.TestCase):
    
    def test_simple_tag(self):
        # Створюємо тест файл
        with codecs.open('test.html', 'w', 'utf-8') as f:
            f.write('<p>Hello</p>')
        
        # Викликаємо функ.
        delete_html_tags('test.html', 'test_result.txt')
        
        # Перевіряємо 
        with codecs.open('test_result.txt', 'r', 'utf-8') as f:
            result = f.read()
        
        self.assertEqual(result, 'Hello')
        
        # Прибираємо файли
        os.remove('test.html')
        os.remove('test_result.txt')
    
    def test_multiple_tags(self):
        with codecs.open('test.html', 'w', 'utf-8') as f:
            f.write('<h1>Title</h1><p>Text</p>')
        
        delete_html_tags('test.html', 'test_result.txt')
        
        with codecs.open('test_result.txt', 'r', 'utf-8') as f:
            result = f.read()
        
        self.assertIn('Title', result)
        self.assertIn('Text', result)
        
        os.remove('test.html')
        os.remove('test_result.txt')
    
    def test_no_tags(self):
        with codecs.open('test.html', 'w', 'utf-8') as f:
            f.write('Just text')
        
        delete_html_tags('test.html', 'test_result.txt')
        
        with codecs.open('test_result.txt', 'r', 'utf-8') as f:
            result = f.read()
        
        self.assertEqual(result, 'Just text')
        
        os.remove('test.html')
        os.remove('test_result.txt')

if __name__ == '__main__':
    # Запускаємо тести
    unittest.main(verbosity=2, exit=False)
    
    # Потім обробляємо файл
    print('\nОбробка draft.html...')
    delete_html_tags('draft.html', 'cleaned.txt')
    print('Готово!')
