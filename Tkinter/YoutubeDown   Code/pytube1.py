import pytube


def show(url):
    num = 1
    r1 = ''
    r2 = []
    yt = pytube.YouTube(f'{url}')
    yt = yt.streams.filter(progressive='True')
    for m in yt:
        r1 += (f'{num}. Sifat:  ')
        for i in str(m)[46:55]:
            if i.isdigit():
                r1 += str(i)
        r2.append(r1)
        r1 = ''
        num += 1
    return r2


def down(url, index, fileas):
    yt = pytube.YouTube(f'{url}')
    yt = list(yt.streams.filter(progressive='True'))[int(index)-1]
    yt.download(output_path=fileas)


# url = input('Kontent linkini kiriting: ')
# show(url)
# index = input('Kontent raqamini kiriting:  ')
# down(url, index)
# input("Saqlandi...")
