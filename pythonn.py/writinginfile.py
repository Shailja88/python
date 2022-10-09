# #Writing content in files
# with open("python.txt","r") as f:
#  lines=f.readlines()
#  print


with open("javascript.txt","w") as f:
    lines=["JS is also awesome","\nJS is my second favorite programming language  "]
    f.writelines(lines)
