## 1.
# fh = open("pracce.txt", 'rt')   #wrong file name
# contents = fh.read()
# fh.close()
#
# print(contents)


# ## 2.
# fh = open("practice.txt", 'rt')   # read mode
# fh.write("some content")          #writing in read mode
# fh.close()


## 3.
fh = open("practice.txt", 'wt')   # write mode (file will be overwritten)
contents = fh.read()          #reading in write mode
fh.close()
