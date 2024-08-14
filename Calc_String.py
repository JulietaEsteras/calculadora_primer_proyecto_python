import math
from tkinter import *

root= Tk()
num=''
cuenta=''
caracter=''

#append_string=''
label_entrada1= ''

# defino las funciones que voy a ir llamando con la calculadora

def append_string(caracter): 
     global cuenta # permite utilizar la variable global CUENTA dentro de la funcion
     if caracter == 'del': # si el boton que qpreté es del, cuenta debe quedar en la cuenta que está haciendo menos un caracter 
        cuenta= cuenta[:-1]
        global label_entrada1 
        label_entrada1= Label(root, text=cuenta)
        label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))
     elif caracter == 'C': # si apreto el boton 'C', debe borrar lo que hay en ambas pantallas
        cuenta= ''
        label_entrada1= Label(root, text=cuenta)
        label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))
        label_entrada2= Label(root, text=cuenta)
        label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
     elif caracter == 'CE': # si apreto 'CE', debe borrar lo que hay en la pantalla de la cuenta pero no en la del resultado
        cuenta= ''
        label_entrada1= Label(root, text=cuenta)
        label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))
     elif caracter == ',':  
        if ',' in cuenta:
           caracter=''
        else:
            cuenta= cuenta + caracter 
            label_entrada1= Label(root, text=cuenta)
            label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S)) 
           # oportunidad de mejora para seguir calculando con el resultado del string
      #elif caracter == '*':
        

      # cuenta es lo que voy escribiendo en el string y 
      # caracter es cada nuevo boton que qpreto de los que llaman a la funcion append_string
     else: 
        cuenta= cuenta + caracter 
        label_entrada1= Label(root, text=cuenta)
        label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S))

def msj_error():
   label_entrada2= Label(root, text='Error de sintaxis')
   label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))

# defino funciones trigonometricas y matematicas

def funcion_mat(caracter):
      global cuenta
   
      if caracter =='sen':
         try:
            print(cuenta)
            res= math.sin(math.radians(float(cuenta)))   # Convierte int(n1) grados a radianes  
            label_entrada2= Label(root, text=res )
            label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
            cuenta=''
         except:
            msj_error()

      elif caracter == 'cos':
         try:
            ang = math.radians(float(cuenta))  # Convierte int(n1) grados a radiane
            res1 = math.cos(ang)
            label_entrada2= Label(root, text=res1 )
            label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
            cuenta=''
         except:
            msj_error()
      elif caracter == 'tan':
         try:
            ang = math.radians(float(cuenta))  # Convierte int(n1) grados a radiane
            res2 = math.tan(ang)
            label_entrada2= Label(root, text=res2 )
            label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
            cuenta=''
         except:
            msj_error()
      elif caracter =='sqr':   
         try:
            label_entrada2= Label(root, text=math.sqrt(float(cuenta)))
            label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S)) 
         except:
            msj_error()
   
def porcentaje(cuenta):
   if '*' in cuenta:
      try:
         res=(eval(cuenta))/100
         print(cuenta)
         label_entrada2= Label(root, text=res)
         label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
      except:
         msj_error()
   else:
      msj_error()

# calcula mediante eval el string cuenta
def calcular(op):
    
    try:
       print(eval(op))
       label_entrada2= Label(root, text=eval(op))
       label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S))
       global cuenta
       #cuenta=''
    except:
      msj_error()
    
# inicio mi pantalla

root.title('Calculadora')
root.geometry('120x250')
root.resizable(0,0)
root.config(bg='white')



# pantalla donde se escribirán los string al apretar botones 
# que llaman a la funcion append_string 
label_entrada1= Label(root, text= cuenta)
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W,N,E,S),padx=1, pady=1)
# pantalla donde se escribirá el resultado de eval al apretar el boton 
# que llama a la funcion calcular 
label_entrada2= Label(root, text= cuenta)
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W,N,E,S),padx=1, pady=1)

#boton que llama a la funcion porcentaje 
#de la cuenta que se armó con la funciom append_string
boton_porc= Button(root, text='%', command=lambda:porcentaje(cuenta))
boton_porc.grid(column=0, row=3,sticky=(W,N,E,S),padx=1, pady=1)
boton_porc.config(bg='#00aaff')

boton_DEL= Button(root, text='⇐', command=lambda:append_string('del'))
boton_DEL.grid(column=3, row=3, sticky=(W,N,E,S),padx=1, pady=1)
boton_DEL.config(bg='#cccccc')

boton_C= Button(root, text='C', command=lambda:append_string('C'))
boton_C.grid(column=2, row=3, sticky=(W,N,E,S),padx=1, pady=1)
boton_C.config(bg='#eeeeee',fg='#ff0000')

boton_CE= Button(root, text='CE', command=lambda:append_string('CE'))
boton_CE.config(bg='#dddddd')
boton_CE.grid(column=1, row=3, sticky=(W,N,E,S),padx=1, pady=1)

# botones que llaman a las funciones trigonometricas, def funcion_mat
boton_sen=Button(root, text= 'sen', command= lambda:funcion_mat('sen'))
boton_sen.grid(column=0, row=9, sticky=(W,N,E,S),padx=1, pady=1)
boton_sen.config(bg='#00ccff')

boton_cos=Button(root, text= 'cos', command= lambda:funcion_mat('cos'))
boton_cos.grid(column=1, row=9, sticky=(W,N,E,S),padx=1, pady=1)
boton_cos.config(bg='#00ccff')

boton_tan=Button(root, text= 'tan', command= lambda:funcion_mat('tan'))
boton_tan.grid(column=2, row=9, sticky=(W,N,E,S),padx=1, pady=1)
boton_tan.config(bg='#00ccff')

boton_sqr= Button(root, text='√', command=lambda:funcion_mat('sqr'))
boton_sqr.grid(column=2, row=4, sticky=(W,N,E,S),padx=1, pady=1)
boton_sqr.config(bg='#00aaff')

boton_1= Button(root, text='1', command=lambda:append_string('1'))
boton_1.grid(column=0, row=7, sticky=(W,N,E,S),padx=1, pady=1)
boton_1.config(bg='black', fg='white')
boton_2= Button(root, text='2', command=lambda:append_string('2'))
boton_2.grid(column=1, row=7, sticky=(W,N,E,S),padx=1, pady=1)
boton_2.config(bg='black', fg='white')
boton_3= Button(root, text='3', command=lambda:append_string('3'))
boton_3.grid(column=2, row=7, sticky=(W,N,E,S),padx=1, pady=1)
boton_3.config(bg='black', fg='white')
boton_4= Button(root, text='4', command=lambda:append_string('4'))
boton_4.grid(column=0, row=6, sticky=(W,N,E,S),padx=1, pady=1)
boton_4.config(bg='black', fg='white')
boton_5= Button(root, text='5', command=lambda:append_string('5'))
boton_5.grid(column=1, row=6, sticky=(W,N,E,S),padx=1, pady=1)
boton_5.config(bg='black', fg='white')
boton_6= Button(root, text='6', command=lambda:append_string('6'))
boton_6.grid(column=2, row=6, sticky=(W,N,E,S),padx=1, pady=1)
boton_6.config(bg='black', fg='white')
boton_7= Button(root, text='7', command=lambda:append_string('7'))
boton_7.grid(column=0, row=5, sticky=(W,N,E,S),padx=1, pady=1)
boton_7.config(bg='black', fg='white')
boton_8= Button(root, text='8', command=lambda:append_string('8'))
boton_8.grid(column=1, row=5, sticky=(W,N,E,S),padx=1, pady=1)
boton_8.config(bg='black', fg='white')
boton_9= Button(root, text='9', command=lambda:append_string('9'))
boton_9.grid(column=2, row=5, sticky=(W,N,E,S),padx=1, pady=1)
boton_9.config(bg='black', fg='white')
boton_0= Button(root, text='0', command=lambda:append_string('0'))
boton_0.grid(column=1, row=8, sticky=(W,N,E,S),padx=1, pady=1)
boton_0.config(bg='black', fg='white')

boton_suma= Button(root, text='+', command=lambda:append_string('+'))
boton_suma.grid(column=3, row=4, sticky=(W,N,E,S),padx=1, pady=1)
boton_suma.config(bg='#77ddff')

boton_resta= Button(root, text='-', command=lambda:append_string('-'))
boton_resta.grid(column=3, row=5, sticky=(W,N,E,S),padx=1, pady=1)
boton_resta.config(bg='#77ddff')

boton_multiplicacion= Button(root, text='*', command=lambda:append_string('*'))
boton_multiplicacion.grid(column=3, row=6, sticky=(W,N,E,S),padx=1, pady=1)
boton_multiplicacion.config(bg='#77ddff')

boton_division= Button(root, text='/', command=lambda:append_string('/'))
boton_division.grid(column=3, row=7, sticky=(W,N,E,S),padx=1, pady=1)
boton_division.config(bg='#77ddff')

boton_par1= Button(root, text='(',command=lambda:append_string('('))
boton_par1.config(bg='#ffaa00')
boton_par1.grid(column=0, row=4, sticky=(W,N,E,S),padx=1, pady=1)

boton_par2= Button(root, text=')', command=lambda:append_string(')'))
boton_par2.config(bg='#ffaa00')
boton_par2.grid(column=1, row=4, sticky=(W,N,E,S),padx=1, pady=1)

boton_neg=Button(root, text='+/-')#falta
boton_neg.config(bg='#AAAAAA')
boton_neg.grid(column=0, row=8, sticky=(W,N,E,S),padx=1, pady=1)

boton_coma=Button(root, text=',', command=lambda:append_string(','))
boton_coma.grid(column=2, row=8, sticky=(W,N,E,S),padx=1, pady=1)
boton_coma.config(bg='#AAAAAA')

boton_igual= Button(root, text='=', command=lambda:calcular(cuenta))
boton_igual.grid(column=3, row=8, rowspan=2, sticky=(W,N,E,S),padx=1, pady=1)






root.mainloop()