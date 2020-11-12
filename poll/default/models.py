from django.db import models

# Create your models here.

class Poll(models.Model):
    # 投票主題文字，至多 200 字
    subject = models.CharField(verbose_name='投票主題', max_length=200)
    description = models.TextField('投票內容說明')
    # 投票建立日期，在建立時若未指定，則自動填入建立時的時間
    date_create  = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ") " + self.subject

class Option(models.Model):
    # 此選項屬於哪一個投票
    poll_id = models.IntegerField('所屬投票主題編號')
    # 選項文字
    title = models.CharField('選項標題', max_length=200)
    # 此選項被投票數
    count = models.IntegerField(default=0)
    def __str__(self):
        return str(self.poll_id) + ": " + self.title