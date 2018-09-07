import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'alte.settings'

if __name__ == '__main__':   

    send_mail(
        '邮件主题subject',
        '邮件具体内容',
        'shzsxabc@sina.com',    # 邮件发送方
        ['wangweiguosx@abchina.com','zhangxiaotaoshzsx@abchina.com'],  # 接受方的邮件地址列表
    )