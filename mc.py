from PIL import Image as i

im = i.open(r"./3.ico")
im_gray = im.convert("L")
im.close()

points = []
threshold = 128
for y in range(im_gray.height):
    for x in range(im_gray.width):
        if im_gray.getpixel((x,y)) < 128:
            points.append((x,y))
min_x = 1000000
min_y = 1000000
max_x = -1000000
max_y = -1000000
for point in points:
    min_x = min(point[0],min_x)
    min_y = min(point[1],min_y)
    max_x = max(point[0],max_x)
    max_y = max(point[1],max_y)
valid_width = max_x - min_x
valid_height = max_y - min_y
print(valid_width,valid_height)
for i in range(len(points)):
    points[i] = (
        points[i][0]-min_x-valid_width//2,
        points[i][1]-min_y-valid_height//2
    )
def convert_to_mc_command(x,y):
    speed = 0.01
    mc_command_template = 'particle minecraft:end rod ~ ~ ~25 {0} {1} 0 {2} 0 forcel'.format(x,y,speed)
    return mc_command_template
with open("./mc.mcfunction",'w') as f:
    for point in points:
        mc_command = convert_to_mc_command(point[0],point[1])
        f.write(mc_command + "\n")