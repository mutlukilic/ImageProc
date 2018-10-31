my_hash[2] += 5
for i in my_hash.keys():
    print(i," ",(my_hash[i]+1))
	
	import Image,ImageOps
def my_Func():
    filename = 'deneme.jpg'
    image = Image.open(filename)
    size = width,height = image.size
    
    if(image.mode = 'RGBA'):
        image.load()
        r,g,b,a = image.split()
    
    image = ImageOps.posterize(image,1)
    image.save("modified_"+filename)
    del image
