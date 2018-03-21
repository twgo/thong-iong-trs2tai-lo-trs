from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from 輸出入 import 通用轉漢字臺羅

# Create your views here.


def thuan5iap8(request):
    return HttpResponse('''
    <h3>原本trs，轉做，臺羅、華語字幕</h3>
    <form method='post' enctype="multipart/form-data" action="/thong2tai5">
    <input name="trs" type="file">
    <input name="submit" type="submit">
    </form>
    這馬程式是試用階段，可能會當用
    <h3>原本trs，轉做，漢字、臺羅、華語字幕</h3>
    <form method='post' enctype="multipart/form-data" action="/thong2tai5han3">
    <input name="trs" type="file">
    <input name="submit" type="submit">
    </form>
    這馬程式是試用階段，閣佇咧改，請看看咧就好，莫commit入去！！
    ''')


@csrf_exempt
def thong2tai5(request):
    thong = request.FILES['trs'].read().decode('utf-8')
    tai = '\r\n'.join(通用轉漢字臺羅.trs2trs('tai5-hua5', thong, 愛漢字=False))

    response = HttpResponse(tai, content_type='application/text')
    response['Content-Length'] = len(tai.encode(encoding='utf_8'))
    response['Content-Disposition'] = 'attachment; filename="test.trs"'
    return response


@csrf_exempt
def thong2tai5han3(request):
    thong = request.FILES['trs'].read().decode('utf-8')
    tai = '\r\n'.join(通用轉漢字臺羅.trs2trs('sann-pan', thong, 愛漢字=True))

    response = HttpResponse(tai, content_type='application/text')
    response['Content-Length'] = len(tai.encode(encoding='utf_8'))
    response['Content-Disposition'] = 'attachment; filename="test.trs"'
    return response
