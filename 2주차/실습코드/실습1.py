bread = ['플랫', '위트', '허니오트', '화이트']
meat = ['미트볼', '소시지', '닭가슴살']
vegtable = ['양상추', '토마토', '오이']
sauce = ['마요네즈', '케찹', '칠리']

for x in bread:
    for y in meat:
        for z in vegtable:
            for r in sauce:
                print(x + '+' + y + '+' + z + '+' + r)