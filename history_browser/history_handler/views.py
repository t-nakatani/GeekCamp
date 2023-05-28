from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

def write_text_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('Hello! GET method detected!')
    elif request.method == 'POST':
        data = json.loads(request.body)
        urls = data.get('urls')
        titles = data.get('titles')

        file_path = 'urls.txt'  # 書き出すファイルのパス
        content = '\n'.join(urls)
        write_text_file(file_path, content)

        file_path = 'titles.txt'  # 書き出すファイルのパス
        content = '\n'.join(titles)
        write_text_file(file_path, content)

        return JsonResponse({'message': 'Success'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
