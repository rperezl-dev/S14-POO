archivo, f='datos.txt',''
docentes=[{'nombre': 'Daniel','edad':50, 'fac':'Ingenieria'},
    {'nombre':'Juan','edad':30,'fac':'Salud'},
    {'nombre':'Yady','edad':40,'fac':'Administrativa'}]

#Escribir archivo: w - a:write - writeline
with open(archivo,'w') as writer:
    for i in range(len(docentes)):
        linea=''
        for clave, valor in docentes[i].items():
            if clave == 'fac':
                linea=linea + (str(valor) if type(valor)==int else valor) + '\n'
            else:
                linea=linea + (str(valor) if type(valor)==int else valor) + ';'
        writer.writelines(linea)

#Leer archivo: r: read - readline - readlines - in
try:
    f=open(archivo, 'r')
    for linea in f:
        print(linea[:-1])
except Exception as e:
    print('Error de archivo: '+str(e))
finally:
    f.close()