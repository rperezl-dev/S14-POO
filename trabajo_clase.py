def leer():
    with open('nombres.txt','r', encoding='UTF-8') as f:
        nombre = [line[:-1]for line in f]
        print(nombre)
def escribir():
    nombres = ['Juan','Pablo','Jesús','Maria']
    nombres2 =  ['Fernanda','Lola','Esperanza','Esther','Lucas']

    with open('nombres.txt','w',encoding='UTF-8') as f:
        for nombre in nombres2:
            f.write(nombre)
            f.write('\n')
def run():
    escribir()
    leer()
if __name__=='__main__':
    run()
    
