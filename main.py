import os
from time import sleep
"""
PROYECTO 1 : CRUD DE EMPRESAS
NOMBRE : LUIS SALAZAR RIVERO
"""

dic_empresas = {
    '100':{
        'razon_social':'TECSUP',
        'direccion' : 'CALLE PERU 123'
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input('INGRESE OPCIÓN : '))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("INGRESE RUC : ")
        razon_social = input("INGRESE RAZÓN SOCIAL : ")
        direccion = input("INGRESE DIRECCIÓN : ")
        dic_nueva_empresa = {
            'razon_social' : razon_social,
            'direccion' : direccion
        }
        dic_empresas[ruc] = dic_nueva_empresa
        print("EMPRESA REGISTRADA CON ÉXITO")

    elif opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESA")
        print("=" * ANCHO)

        for ruc,info in dic_empresas.items():
            print(f"RUC : {ruc} ")
            print(f"RAZÓN SOCIAL : {info['razon_social']}")
            print(f"DIRECCIÓN : {info['direccion']}")
            print("-" * ANCHO)
            
    elif opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR  EMPRESA")
        print("=" * ANCHO)
        ruc = input("INGRESE RUC DE LA EMPRESA A ACTUALIZAR : ")
        if ruc in dic_empresas:
            print(f'RAZÓN SOCIAL ACTUAL : {dic_empresas[ruc]["razon_social"]}')
            nueva_razon_social = input(f"INGRESE NUEVA RAZÓN SOCIAL ({dic_empresas[ruc]['razon_social']}) :")
            nueva_direccion = input(f"INGRESE NUEVA DIRECCIÓN ({dic_empresas[ruc]['direccion']}) :")
            if nueva_razon_social:
                dic_empresas[ruc]['razon_social'] = nueva_razon_social
            if nueva_direccion:
                dic_empresas[ruc]['direccion'] = nueva_direccion
            print("EMPRESA ACTUALIZADA CON ÉXITO")
        else:
            print("RUC NO ENCONTRADO")
       
    elif opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        
        ruc = input("INGRESE RUC DE LA EMPRESA A ELIMINAR : ")
        if ruc in dic_empresas:
            print(f"EMPRESA({dic_empresas[ruc]['razon_social']}) SE ELIMINARÁ")
            print("-" * ANCHO)    
            del dic_empresas[ruc]
            print(f"EMPRESA ELIMINADA CON ÉXITO")    
        else:
            print("EMPRESA PARA EL RUC QUE INGRESO NO ENCONTRADO")    
    elif opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL PROGRAMA")
        print("=" * ANCHO)
        sleep(2)
        break
    else:
        print("OPCIÓN NO VÁLIDA")
    
    input("Presione ENTER para continuar...")
