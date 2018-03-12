from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from 輸出入 import 通用轉漢字臺羅

# Create your views here.


def thuan5iap8(request):
    return HttpResponse('''
    <form method='post' enctype="multipart/form-data" action="/thong2tai5">
    <input name="trs" type="file">
    <input name="submit" type="submit">
    </form>
    這馬程式是試用階段，閣佇咧改，請看看咧就好，莫commit入去！！
    ''')


@csrf_exempt
def thong2tai5(request):
    thong = request.FILES['trs'].read().decode('utf-8')
    tai = '\r\n'.join(通用轉漢字臺羅.trs2trs(thong))
    
    response = HttpResponse(tai, content_type='application/text')
    response['Content-Length'] = len(tai)
    response['Content-Disposition'] = 'attachment; filename="test.trs"'
    return response
