from datetime import datetime

from django.db import models


class Basic(models.Model):
    data_source = models.IntegerField(verbose_name='取得元')
    name = models.CharField(verbose_name='店舗名', max_length=255)
    lat = models.FloatField(verbose_name='緯度')
    lng = models.FloatField(verbose_name='経度')
    created = models.DateTimeField(verbose_name='作成日')

    def setValues(self, x, data_source=0):
        # 取得元
        self.data_source = data_source
        # 名前
        self.name = x.name
        # 緯度
        self.lat = x.geometry.location.lat
        # 経度
        self.lng = x.geometry.location.lng
        # 作成日
        self.created = datetime.now()


class Google(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    basic_id = models.ForeignKey(Basic, db_column='basic_id', on_delete=models.CASCADE)
    place_id = models.CharField(max_length=255)

    def setBasicValues(self, x):
        # Google ID
        self.id = x.id
        # Google Place ID
        self.place_id = x.place_id
        # Tags
        self.types = []
        for i in range(len(x.types)):
            self.types.append(x.types[i])
        self.types = ','.join(self.types)

        self.created = datetime.now()

        basic = Basic()
        basic.setValues(x, 0)
        self.basic = basic

    def save(self, **kwargs):
        # 重複チェック
        result = Google.objects.filter(id=self.id).first()
        if result is None:
            # 基本IDの最大値+1をキーとする
            self.basic.id = Basic.objects.count() + 1
            # 外部キーの為、オブジェクト格納
            self.basic_id = self.basic
            # 基本情報側を保存
            self.basic.save()
            # 自身の保存
            super(Google, self).save(**kwargs)


class GoogleNearByResponse:
    managed = False

    def __init__(self, x):
        # レスポンス情報
        self.next_page_token = x.next_page_token
        self.status = x.status

        # 基本情報
        self.results = []
        for i in range(len(x.results)):
            google = Google()
            google.setBasicValues(x.results[i])
            self.results.append(google)


class GoogleDetailByResponse:
    managed = False

    def __init__(self, x):
        # レスポンス情報
        self.status = x.status

        # 詳細情報
        google = Google()
        google.setDetailValues(x.result)
        self.result = google

