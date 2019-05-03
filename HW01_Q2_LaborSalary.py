ref = {'general':120, 'level1plus':1.25, 'level2plus':1.5, 'level1':60, 'level2':80}
salary = 0
try:
    lhrs = input("輸入勞動時數: ")
    lhrs = int(lhrs)
    while lhrs > 0:
        if lhrs > ref['level2']:
            salary = (lhrs-ref['level2']) * ref['level2plus']
            lhrs = ref['level2']
        elif lhrs > ref['level1']:
            salary = salary + (lhrs -ref['level1']) * ref['level1plus']
            lhrs = ref['level1']
        elif lhrs <= ref['level1']:
            salary = (salary + lhrs) * ref['general']
            break
    print('薪資計算結果: {0}'.format(salary))
except ValueError or TypeError:
    print("請輸入正確格式資料(正整數，非小數)")