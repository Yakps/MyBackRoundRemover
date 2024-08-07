from rembg import remove
input_path = "image.jpg"            #added picture name
output_path = "output.png"          #added outpt.png

with open(input_path,'rb') as i:
    with open(output_path,'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)

