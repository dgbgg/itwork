from django.db import models


class User(models.Model):

    identitys = (
        ('网点负责人',   "网点负责人"),
        ('柜员',        "柜员"),
        ('其他',        "其他"),
    )

    name = models.CharField('姓名', max_length=128, unique=True)
    password = models.CharField('密码', max_length=256)
    email = models.EmailField('邮箱', unique=True)
    outlet = models.CharField('网点号',  max_length=4, default="8888")
    identity = models.CharField('身份', max_length=32, choices=identitys, default="其他")
    c_time = models.DateTimeField('时间', auto_now_add=True)
    has_confirmed = models.BooleanField('是否验证', default=False)

    def __str__(self):
        return self.name

    class Meta:
        #ordering = ["-c_time"]
        ordering = ["name"]
        verbose_name_plural = verbose_name = "用户"

class ConfirmString(models.Model):
    code = models.CharField('确认码', max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE )
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"