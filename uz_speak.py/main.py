from playsound import playsound
a = ['sa.mp3', 'al.mp3', 'lo.mp3', 'om.mp3', 'space.mp3', 'me.mp3', 'en.mp3', 'ni.mp3',
     'in.mp3', 'ng.mp3', 'space.mp3', 'is.mp3', 'sm.mp3', 'mi.mp3', 'im.mp3', 'space.mp3', 'zu.mp3', 'uh.mp3', 'hr.mp3', 'ri.mp3', 'id.mp3', 'dd.mp3', 'di.mp3', 'in.mp3']
# for i in a:
#     playsound(i)
b = ['a', 's', 'l', 'o', 'm', 'e', 'n', 'g', 'i', 'z', 'u', 'h', 'r', 'd']

texts = input("Enter the text: ")


def read_text(texts):
    x = ''
    y = ''
    for i in texts:
        if i in b:
            x += i
            y = i
            if len(x) == 2:
                playsound(x + '.mp3')
                x = i
        else:
            x = ''


read_text(texts)