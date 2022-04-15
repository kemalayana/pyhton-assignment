command = ['right 10', 'left 30', 'up 30', 'down 40']
horizontal = []
vertical = []
for i in command:
    if 'right' in i or 'left' in i:
        horizontal.append(i)
    else:
        vertical.append(i)

new_list_hor = []
for j in horizontal:
    new_list_hor.append((j.replace('right', '+')).replace('left', '-'))
new_list_ver = []
for t in vertical:
    new_list_ver.append((t.replace('up', '+')).replace('down', '-'))

ver_position = eval(''.join(new_list_ver))
hor_position = eval(''.join(new_list_hor))
x = 0
y = 0

position_initial = (x, y)
position_final = (x + hor_position, y + ver_position)
print(position_final)
