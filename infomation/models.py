from django.db import models

class InfomationModel(models.Model):
    infomation_category = models.CharField(max_length=50, choices=(('infomation', 'お知らせ'),
                                          ('update', 'アップデート'),
                                          ('event', 'イベント告知'),
                                          ('maintenance', 'メンテナンス'),
                                          ('other', 'その他')),
                                          verbose_name="カテゴリー") 
    
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    author = models.CharField(max_length=100, default="admin", verbose_name="投稿者")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Infomation"

class FrequentlyAskedQuestionModel(models.Model):
    question = models.TextField(default="", verbose_name="質問")
    answer = models.TextField(default="", verbose_name="回答")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Frequently Asked Question"