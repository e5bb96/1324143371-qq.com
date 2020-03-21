import csv
def main():
    with open (r'C:\Users\e5bb96\Desktop\assets.csv','a',newline='') as csvfile:
        writer = csv.writer(csvfile,dialect='excel')
        header = ['小区名称','地址','建筑年份','楼栋','单元','户室','朝向','面积']
        writer.writerow(header)

    title =input('请输入小区名称：')
    address = input('请输入小区地址：')
    year = input('请输入小区建筑年份：')
    block = input('请输入楼栋号：')

    unti_loop = True
    while unti_loop:
        unit = input ('请输入单元号：')
        start_floor = input('请输入起始楼层：')
        end_floor = input('请输入终止楼层：')

        input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')

        start_floor_rooms = {}
        floor_last_number = []

        while True:
            last_number = input('请输入起始楼层户室的尾号：（如01,02）')
            floor_last_number.append(last_number)
            room_number = int(start_floor + last_number)
            direction = int(input('请输入%d的朝向(南北朝向输入1，东西朝向输入2)：'% room_number))
            area = int(input('请输入{}的面积，单位 m²：'.format(room_number)))
            start_floor_rooms[room_number]=[direction,area]

            continues = input('是否继续输入下一个尾号，按 n 停止输入，按其他任意键继续：')
            if continues == 'n':
                break
            else:
                continue

        unti_rooms = {}
        unti_rooms[start_floor] = start_floor_rooms
        for floor in range(int(start_floor) + 1 , int(end_floor) + 1):
            floor_rooms = {}
            for i in range(len(start_floor_rooms)):
                number = str(floor) + floor_last_number[i]
                info = start_floor_rooms[int(start_floor + floor_last_number[i])]
                floor_rooms[int(number)] = info
            unti_rooms[floor] = floor_rooms

        with open (r'C:\Users\e5bb96\Desktop\assets.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile,dialect='excel')
            for sub_dict in unti_rooms.values():  #字典.values()  遍历字典的名称    
                for room,info in sub_dict.items():  #for a,b in 字典.items() 遍历字典的健值对,a对应健,b对应值
                    dire = ['','南北','东西']
                    writer.writerow([title,address,year,block,unit,room,dire[info[0]],info[1]])

        unti_continue = input('是否需要继续输入下一个单元？按 n 停止，按其他任意键继续')
        if unti_continue == 'n':
            unti_loop = False
        else:
            unti_loop = True

    print('恭喜你，录入完成')
