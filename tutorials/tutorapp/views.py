from django.http import JsonResponse
from . import models
import json


def parse_request(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body


def findall(request):
    if request.method == 'GET':
        jsonn = []
        search = request.GET.get('title')
        if search:
            all_titles = [i[1] for i in models.Tutorial.objects.all().values_list()]
            needed_titles = [i for i in all_titles if search in i]
            for title in needed_titles:
                info = models.Tutorial.objects.filter(title=title)
                for tutorial in info.values_list():
                    jsonn.append({'id': tutorial[0],
                                  'title': tutorial[1],
                                  'description': tutorial[2],
                                  'published': tutorial[3],
                                  'createdAt': tutorial[4],
                                  'updatedAt': tutorial[5]})
            return JsonResponse(jsonn, safe=False)
        else:
            all_tutorials = models.Tutorial.objects.all()
            # 0 - id, 1 - title, 2 - description, 3 - published, 4 - createdAt, 5 - updatedAt
            for tutorial in all_tutorials.values_list():
                jsonn.append({'id': tutorial[0],
                              'title': tutorial[1],
                              'description': tutorial[2],
                              'published': tutorial[3],
                              'createdAt': tutorial[4],
                              'updatedAt': tutorial[5]})
            return JsonResponse(jsonn, safe=False)

    elif request.method == 'POST':
        body = parse_request(request)
        models.Tutorial.objects.create(title=body['title'],
                                       description=body['description'],
                                       published=False).save()
        return JsonResponse({'response':'201'})
    elif request.method == 'DELETE':
        models.Tutorial.objects.all().delete()
        return JsonResponse({'response':'200'})
    else:
        pass


def id_stuff(request, id):
    if request.method == 'GET':
        try:
            exact_tutorial = models.Tutorial.objects.get(id=id)
            jsonn = {'id': exact_tutorial.id,
                      'title': exact_tutorial.title,
                      'description': exact_tutorial.description,
                      'published': exact_tutorial.published,
                      'createdAt': exact_tutorial.createdAt,
                      'updatedAt': exact_tutorial.updatedAt}
            print(jsonn)
            return JsonResponse(jsonn)

        except:
            return JsonResponse({'response':'404'})
    elif request.method == 'PUT':
        body = parse_request(request)
        exact_tutorial = models.Tutorial.objects.get(id=id)
        exact_tutorial.title = body['title']
        exact_tutorial.description = body['description']
        exact_tutorial.published = body['published']
        exact_tutorial.save()
        return JsonResponse({'response': '200'})
    elif request.method == 'DELETE':
        exact_tutorial = models.Tutorial.objects.get(id=id)
        exact_tutorial.delete()
        return JsonResponse({'response': '200'})
    else:
        pass


