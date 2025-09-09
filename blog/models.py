from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)     # 注意是 = 不是 :
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):                           # 要有 self 參數
        return self.title                        # 這行必須縮排在函式內

