# from scapy.all import *
# from scapy.layers.inet import IP
# import pcap
# def Callback(packet):
#     print('src:%s----->dst:%s'%(packet[IP].src, packet[IP].dst))
#     print('TTL:%s'%packet[IP].ttl)
#     wrpcap('data.pcap', packet)
#     print(packet.time)  #内置的show()函数打印数据包内容
#
# # IFACES = ifaces = NetworkInterfaceDict()  #NetworkInterfaceDict的无参构造函数不包含任何有用信息
# # IFACES.load()
# # print(ifaces)
# print("sddd")
# sniff(filter='src host 192.168.63.24 && dst port 80',iface=conf.route.route("192.168.40.1")[0], prn=Callback,count=0)
# 候选字
# coding:utf-8
chars_male ='汤道耕艾芜塔塔木林萧乾朱自清自华字佩弦号秋实朱光潜孟实周作人号星灼原名櫆寿自号起孟笔名仲密开明周遐寿独应等周祖式周而复周扬周起应周树藩绿原赵平福柔石章炳麟字牧敏号太炎张乃莹萧红张恨水张心远余鹤林叶紫叶绍钧字圣陶姚莘农姚克杨瑞麟扬村彬孙树勋孙犁苏汶杜衡舒庆春字舒老舍沈乃熙沈端先夏衍沈从文沈岳焕笔名休芸芸甲辰上官碧璇若森堡任钧'

chars_female = '嘉琼桂叶璧璐娅琦晶妍茜秋珊锦青婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚婕馨瑗琰韵园艺咏卿澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢柔竹霭凝晓欢霄枫芸菲宜可舒影思丽安秀娟多英高华慧飞巧美乐静淑惠珠行翠雅芝玉萍红玲芬芳燕春珍贞莉兰洁梅琳素云莲真雪爱家妹霞香月莺艳瑞凡佳寻言子自墨上见如南北紫远清音林久苏吴睛雨舟闻宝景洛夏乡文'

while True:
    gender = input('请选择您的性别 ( 1-女 2-男 ) ：')
    if gender!='1' and gender!='2':
        print('输入错误请重新输入')
    else:
        break

chars = chars_female if gender == '1' else chars_male

from random import randint
max = len(chars)
while True:
    idx1,idx2 = randint(0,max-1), randint(0,max-1)
    print(f'{chars[idx1]}{chars[idx2]}',end='')
    # 直接回车继续输入其他按键回车退出
    key = input('')
    if key :
        break