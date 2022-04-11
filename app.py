import eel
import random
import json


eel.init('web')

# @eel.expose
# def get(data):
#     return data

# @eel.expose
# def distribute():
#     # FreshEnglish
#     Mon34 = 4
#     Mon78 = 3
#     Wed34 = 3
#     Wed56 = 7-3
#     Wed78 = 6-3
#     # Thu34 = 4 試行班
#     Thu78 = 3
#     Fri12 = 4
#     Fri34 = 5

#     Mon34teacher = []
#     Mon78teacher = []
#     Wed34teacher = []
#     Wed56teacher = []
#     Wed78teacher = []
#     Thu78teacher = []
#     Fri12teacher = []
#     Fri34teacher = []

#     # Teacher
#     schoolw = 0.5
#     agew = 0.5

#     # 權重
#     Teacherpriority = {}

#     # 志願序
#     Teacherlist = {}
#     Teacher = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'T13', 'T14', 'T15']
    

#     T1school = 30
#     T1age = 50
#     T1priority = T1school * schoolw + T1age * agew
#     Teacherpriority['T1'] = T1priority
#     T1 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T1'] = T1


#     T2school = 29
#     T2age = 50
#     T2priority = T2school * schoolw + T2age * agew
#     Teacherpriority['T2'] = T2priority
#     T2 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T2'] = T2

#     T3school = 28
#     T3age = 50
#     T3priority = T3school * schoolw + T3age * agew
#     Teacherpriority['T3'] = T3priority
#     T3 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T3'] = T3

#     T4school = 27
#     T4age = 50
#     T4priority = T4school * schoolw + T4age * agew
#     Teacherpriority['T4'] = T4priority
#     T4 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T4'] = T4

#     T5school = 26
#     T5age = 50
#     T5priority = T5school * schoolw + T5age * agew
#     Teacherpriority['T5'] = T5priority
#     T5 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T5'] = T5

#     T6school = 25
#     T6age = 50
#     T6priority = T6school * schoolw + T6age * agew
#     Teacherpriority['T6'] = T6priority
#     T6 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T6'] = T6

#     T7school = 24
#     T7age = 50
#     T7priority = T7school * schoolw + T7age * agew
#     Teacherpriority['T7'] = T7priority
#     T7 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T7'] = T7

#     T8school = 23
#     T8age = 50
#     T8priority = T8school * schoolw + T8age * agew
#     Teacherpriority['T8'] = T8priority
#     T8 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T8'] = T8

#     T9school = 22
#     T9age = 50
#     T9priority = T9school * schoolw + T9age * agew
#     Teacherpriority['T9'] = T9priority
#     T9 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T9'] = T9

#     T10school = 21
#     T10age = 50
#     T10priority = T10school * schoolw + T10age * agew
#     Teacherpriority['T10'] = T10priority
#     T10 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T10'] = T10

#     T11school = 20
#     T11age = 50
#     T11priority = T10school * schoolw + T10age * agew
#     Teacherpriority['T11'] = T11priority
#     T11 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T11'] = T11

#     T12school = 19
#     T12age = 50
#     T12priority = T12school * schoolw + T12age * agew
#     Teacherpriority['T12'] = T12priority
#     T12 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T12'] = T12

#     T13school = 18
#     T13age = 50
#     T13priority = T13school * schoolw + T13age * agew
#     Teacherpriority['T13'] = T13priority
#     T13 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T13'] = T13

#     T14school = 17
#     T14age = 50
#     T14priority = T14school * schoolw + T14age * agew
#     Teacherpriority['T14'] = T14priority
#     T14 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T14'] = T14

#     T15school = 16
#     T15age = 50
#     T15priority = T15school * schoolw + T15age * agew
#     Teacherpriority['T15'] = T15priority
#     T15 = ['Mon34','Mon78', 'Wed34', 'Wed56', 'Wed78', 'Thu78', 'Fri12', 'Fri34']
#     Teacherlist['T15'] = T15


#     #print(Teacherpriority)
#     #print(Teacherlist)

#     # 權重排序
#     sort_orders = sorted(Teacherpriority.items(), key=lambda x: x[1], reverse=True)
#     #print(sort_orders)
#     # for i in sort_orders:
#     #     print(i[0], i[1])


#     Finished = (Mon34 == 0 and Mon78 == 0 and Wed34 == 0 and Wed56 == 0 and Wed78 == 0 and Thu78 == 0 and Fri12 == 0 and Fri34 == 0)

#     # 分發第一輪
#     while(Finished is not True):
#         for name in sort_orders:
#             #print("這輪的優先序:" + str(sort_orders))
#             for classes in Teacherlist[name[0]]:
#                 #print('name:'+str(name)+'classes:'+str(classes))
#                 if classes == 'Mon34' and Mon34 > 0:
#                     Mon34 -= 1
#                     Mon34teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Mon34')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Mon78' and Mon78 > 0:
#                     Mon78 -= 1
#                     Mon78teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Mon78')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Wed34' and Wed34 > 0:
#                     Wed34 -= 1
#                     Wed34teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Wed34')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Wed56' and Wed56 > 0:
#                     Wed56 -= 1
#                     Wed56teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Wed56')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Wed78' and Wed78 > 0:
#                     Wed78 -= 1
#                     Wed78teacher.append(name[0])        
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Wed78')
#                     #print(Teacherlist[name[0]])
#                     break
#                 # elif classes == 'Thu34' and Thu34 > 0:
#                 #     Thu34 -= 1
#                 #     Thu34teacher.append(name[0])
#                 #     #print(Teacherlist[name[0]])
#                 #     Teacherlist[name[0]].remove('Thu34')
#                 #     #print(Teacherlist[name[0]])
#                 #     break
#                 elif classes == 'Thu78' and Thu78 > 0:
#                     Thu78 -= 1
#                     Thu78teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Thu78')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Fri12' and Fri12 > 0:
#                     Fri12 -= 1
#                     Fri12teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Fri12')
#                     #print(Teacherlist[name[0]])
#                     break
#                 elif classes == 'Fri34' and Fri34 > 0:
#                     Fri34 -= 1
#                     Fri34teacher.append(name[0])
#                     #print(Teacherlist[name[0]])
#                     Teacherlist[name[0]].remove('Fri34')
#                     #print(Teacherlist[name[0]])
#                     break
#         # print('Mon34:'+str(Mon34teacher))
#         # print('Mon78:'+str(Mon78teacher))
#         # print('Wed34:'+str(Wed34teacher))
#         # print('Wed56:'+str(Wed56teacher))
#         # print('Wed78:'+str(Wed78teacher))
#         # #print('Thu34:'+str(Thu34teacher))
#         # print('Thu78:'+str(Thu78teacher))
#         # print('Fri12:'+str(Fri12teacher))
#         # print('Fri34:'+str(Fri34teacher))
#         # print()
#         # 反轉順序
#         sort_orders = sorted(Teacherpriority.items(), key=lambda x: x[1])
#         Finished = (Mon34 == 0 and Mon78 == 0 and Wed34 == 0 and Wed56 == 0 and Wed78 == 0 and Thu78 == 0 and Fri12 == 0 and Fri34 == 0)
        
#     Final = {}
#     Final['Mon34teacher'] = Mon34teacher
#     Final['Mon78teacher'] = Mon78teacher
#     Final['Wed34teacher'] = Wed34teacher
#     Final['Wed56teacher'] = Wed56teacher
#     Final['Wed78teacher'] = Wed78teacher
#     Final['Thu78teacher'] = Thu78teacher
#     Final['Fri12teacher'] = Fri12teacher
#     Final['Fri34teacher'] = Fri34teacher
        
#     print(Final)
#     print(json.dumps(Final))
#     return json.dumps(Final)

# @eel.expose    
# def ran_int():
#     return random.randint(0,100)

eel.start('main.html')