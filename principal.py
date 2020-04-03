from tkinter import ttk
from tkinter import *
from tkinter import messagebox

distintosTipos = ("Papeleria", "Supermercado", "Drogueria")

IVA_papel=16/100
IVA_supermercado=4/100
IVA_drogueria=12/100

producto1="Lapiz"
tipo_producto1=distintosTipos[0]
cant_minima1=5
cant_bodega1=18
valor1=20
cant_ventas1=0
ventas1=0

producto2="Aspirina"
tipo_producto2=distintosTipos[2]
cant_minima2=8
cant_bodega2=25
valor2=80
cant_ventas2=0
ventas2=0

producto3="Borrador"
tipo_producto3=distintosTipos[0]
cant_minima3=10
cant_bodega3=30
valor3=10
cant_ventas3=0
ventas3=0

producto4="Pan"
tipo_producto4=distintosTipos[1]
cant_minima4=20
cant_bodega4=15
valor4=70
cant_ventas4=0
ventas4=0

nombres = ("Lapiz", "Borrador", "Aspirina", "Pan")

window = Tk()
window.geometry("800x630")
window.title("Trabajo Practico I Sistema Stock Valdez")
window.configure(bg="Green")


Esquina_inf_izquierda=Canvas(window,width=395,height=190, borderwidth=2, relief="groove")
Esquina_inf_izquierda.create_rectangle(0,0,900,900)
Esquina_inf_izquierda.place(x=0,y=335)

Esquina_sup_izquierda=Canvas(window,width=395,height=230, borderwidth=2, relief="raised")
Esquina_sup_izquierda.create_rectangle(0,0,900,900)
Esquina_sup_izquierda.place(x=0,y=65)

Esquina_sup_derecha=Canvas(window,width=395,height=230, borderwidth=2, relief="raised")
Esquina_sup_derecha.create_rectangle(0,0,900,900)
Esquina_sup_derecha.place(x=400,y=65)

Esquina_inf_derecha=Canvas(window,width=395,height=190, borderwidth=2, relief="groove")
Esquina_inf_derecha.create_rectangle(0,0,900,900)
Esquina_inf_derecha.place(x=400,y=335)

imageExLapiz = PhotoImage(file='Captura(5).PNG')
Label(window, image=imageExLapiz)\
    .place(x=10, y=180)


imageExAspirina=PhotoImage(file='Captura(1).PNG')
Label(window, image=imageExAspirina)\
    .place(x=420, y=170)

imageExBorrador = PhotoImage(file='Captura(2).PNG')
Label(window, image=imageExBorrador)\
    .place(x=1, y=430)

imageExLapiz = PhotoImage(file='Captura(3).PNG')
Label(window, image=imageExLapiz)\
    .place(x=410, y=440)


#Funciones de abastecer
def abastecer_lapiz_IzqSup():
    global cant_minima1
    global cant_bodega1
    def guardar_abastecimiento_1():
        global cant_bodega1
        cant_bodega1+=int(cantAbastecer.get())
        cantidad_bodega_EsquinaSupIzquierda.configure(text=cant_bodega1)
        messagebox.showinfo("Informacion", "Guardado de manera exitosa")
        abastecimiento.destroy()
    if cant_bodega1>cant_minima1:
        messagebox.showinfo("Informacion","Aun no se ha acabado el stock")
    elif cant_bodega1 < cant_minima1:
        abastecimiento = Tk()
        abastecimiento.geometry("350x100")
        abastecimiento.title("Abastecimiento")
        cantidad_para_abastecer=Label(abastecimiento, text="Cantidad a abastecer:", font=("Times New Roman",12))
        cantidad_para_abastecer.place(x=0,y=10)
        cantAbastecer=Entry(abastecimiento,width=21)
        cantAbastecer.place(x=200,y=11)
        button_cant_abastecimiento=Button(abastecimiento,text="Cambiar", font=("Times New Roman",12),width=13, command=guardar_abastecimiento_1)
        button_cant_abastecimiento.place(x=0,y=40)


        abastecimiento.mainloop()




def abastecer_aspirina_DerSup():
    global cant_minima2
    global cant_bodega2
    def guardar_abastecimiento_2():
        global cant_bodega2
        cant_bodega2+=int(cantAbastecer.get())
        cantidad_bodega_EsquinaSupDerecha.configure(text=cant_bodega2)
        messagebox.showinfo("Informacion", "Guardado de manera exitosa")
        abastecimiento.destroy()
    if cant_bodega2>cant_minima2:
        messagebox.showinfo("Informacion", "Aun no se ha acabado el stock")
    elif cant_bodega2 < cant_minima2:
        abastecimiento = Tk()
        abastecimiento.geometry("350x100")
        abastecimiento.title("Abastecimiento")
        cantidad_para_abastecer=Label(abastecimiento, text="Cantidad a abastecer:", font=("Times New Roman",12))
        cantidad_para_abastecer.place(x=0,y=10)
        cantAbastecer=Entry(abastecimiento,width=21)
        cantAbastecer.place(x=200,y=11)
        button_cant_abastecimiento=Button(abastecimiento,text="Cambiar", font=("Times New Roman",12),width=13, command=guardar_abastecimiento_2)
        button_cant_abastecimiento.place(x=0,y=40)

        abastecimiento.mainloop()

def abastecer_borrador_IzqInf():
    global cant_minima3
    global cant_bodega3
    def guardar_abastecimiento_3():
        global cant_bodega3
        cant_bodega3+=int(cant_abastecer.get())
        cantidad_bodega_EsquinaInfIzquierda.configure(text=cant_bodega3)
        messagebox.showinfo("Informacion", "Guardado de manera exitosa")
        abastecimiento.destroy()
    if cant_bodega3>cant_minima3:
        messagebox.showinfo("Informacion", "Aun no se ha acabado el stock")
    elif cant_bodega3 < cant_minima3:
        abastecimiento = Tk()
        abastecimiento.geometry("350x100")
        abastecimiento.title("Abastecimiento")
        cantidad_para_abastecer=Label(abastecimiento, text="Cantidad a abastecer:", font=("Times New Roman",12))
        cantidad_para_abastecer.place(x=0,y=10)
        cant_abastecer=Entry(abastecimiento,width=21)
        cant_abastecer.place(x=200,y=11)
        button_cant_abastecimiento=Button(abastecimiento,text="Cambiar", font=("Times New Roman",12),width=13, command=guardar_abastecimiento_3)
        button_cant_abastecimiento.place(x=0,y=40)

        abastecimiento.mainloop()


def abastecer_pan_DerInf():
    global cant_minima4
    global cant_bodega4
    def guardar_abastecimiento_4():
        global cant_bodega4
        cant_bodega4+=int(cant_abastecer.get())
        cantidad_bodega_EsquinaInfDerecha.configure(text=cant_bodega4)
        messagebox.showinfo("Informacion", "Guardado de manera exitosa")
        abastecimiento.destroy()
    if cant_bodega4>cant_minima4:
        messagebox.showinfo("Informacion", "Aun no se ha acabado el stock")
    elif cant_bodega4 < cant_minima4:
        abastecimiento = Tk()
        abastecimiento.geometry("350x100")
        abastecimiento.title("Abastecimiento")
        cantidad_para_abastecer=Label(abastecimiento, text="Cantidad a abastecer:", font=("Times New Roman",12))
        cantidad_para_abastecer.place(x=0,y=10)
        cant_abastecer=Entry(abastecimiento,width=21)
        cant_abastecer.place(x=200,y=11)
        button_cant_abastecimiento=Button(abastecimiento,text="Cambiar", font=("Times New Roman",12),width=13, command=guardar_abastecimiento_4)
        button_cant_abastecimiento.place(x=0,y=40)

        abastecimiento.mainloop()


#Funcion de vender lapiz
def vender_lapiz_IzqSup():
    global cant_bodega1
    global cant_minima1
    global cant_ventas1
    def guardar_vender_1():
        global cant_ventas1
        global cant_bodega1
        cant_ventas1+=int(cantidad_venta.get())
        venta.destroy()
        if tipo_producto1==distintosTipos[0]:
            ventas1=int(cant_ventas1*(valor1+IVA_papel))
        elif tipo_producto1==distintosTipos[1]:
            ventas1=int(cant_ventas1*(valor1+IVA_supermercado))
        else:
            ventas1=int(cant_ventas1*(valor1+IVA_drogueria))
        if cant_bodega1>cant_minima1:
            cant_bodega1=int(cant_bodega1-cant_ventas1)
        else:
            cant_bodega1=int(cant_ventas1-cant_bodega1)
        cantidad_bodega_EsquinaSupIzquierda.configure(text=cant_bodega1)
        valor_U_EsquinaSupIzquierda.configure(text=(f"$ {ventas1}"))
        vendido_EsqSupIzq.configure(text=cant_ventas1)
        messagebox.showinfo(title="Informacion",message=("Se guardo con exito"))
    if cant_bodega1<cant_minima1:
        messagebox.showinfo(title="Informacion",message=("Es menor la cantidad de bodega que la cantidad minima, por ello no se puede realizar la venta"))
    else:
        venta=Tk()
        venta.title("Vender")
        venta.geometry("400x90")

        cantVenta=Label(venta, text="Cantidad a vender:", font=("Times New Roman",12))
        cantVenta.place(x=0,y=10)
        cantidad_venta=Entry(venta,width=21)
        cantidad_venta.place(x=200,y=11)
        button_cant_venta=Button(venta,text="Vender", font=("Times New Roman",12),width=13, command=guardar_vender_1)
        button_cant_venta.place(x=0,y=40)

        venta.mainloop()

#Funcion venta de la aspirina
def vender_aspirina_DerSup():
    global cant_bodega2
    global cant_minima2
    global cant_ventas2
    def guardar_vender_2():
        global cant_ventas2
        global cant_bodega2
        cant_ventas2+=int(cantidad_venta.get())
        venta.destroy()
        if tipo_producto2==distintosTipos[0]:
            ventas2=int(cant_ventas2*(valor2+IVA_papel))
        elif tipo_producto1==distintosTipos[1]:
            ventas2=int(cant_ventas2*(valor2+IVA_supermercado))
        else:
            ventas2=int(cant_ventas2*(valor2+IVA_drogueria))
        if cant_bodega2>cant_minima2:
            cant_bodega2=int(cant_bodega2-cant_ventas2)
        else:
            cant_bodega2=int(cant_ventas2-cant_bodega2)
        cantidad_bodega_EsquinaSupDerecha.configure(text=cant_bodega2)
        valor_U_EsquinaSupDerecha.configure(text=(f"$ {ventas2}"))
        vendido_EsqSupDer.configure(text=cant_ventas2)
        messagebox.showinfo(title="Informacion",message=("Se guardo con exito"))
    if cant_bodega2<cant_minima2:
        messagebox.showinfo(title="Informacion",message=("Es menor la cantidad de bodega que la cantidad minima, por ello no se puede realizar la venta"))
    else:
        venta=Tk()
        venta.title("Vender")
        venta.geometry("400x90")

        cantVenta=Label(venta, text="Cantidad a vender:", font=("Times New Roman",12))
        cantVenta.place(x=0,y=10)
        cantidad_venta=Entry(venta,width=21)
        cantidad_venta.place(x=200,y=11)
        button_cant_venta=Button(venta,text="Vender", font=("Times New Roman",12),width=13, command=guardar_vender_2)
        button_cant_venta.place(x=0,y=40)

        venta.mainloop()

#Funcion venta del borrador
def vender_borrador_IzqInf():
    global cant_bodega3
    global cant_minima3
    global cant_ventas3
    def guardar_vender_3():
        global cant_ventas3
        global cant_bodega3
        cant_ventas3+=int(cantidad_venta.get())
        if tipo_producto1==distintosTipos[0]:
            ventas3=int(cant_ventas3*(valor3+IVA_papel))
        elif tipo_producto3==distintosTipos[1]:
            ventas3=int(cant_ventas3*(valor3+IVA_supermercado))
        else:
            ventas3=int(cant_ventas3*(valor3+IVA_drogueria))
        if cant_bodega3>cant_minima3:
            cant_bodega3=int(cant_bodega3-cant_ventas3)
        else:
            cant_bodega3=int(cant_ventas3-cant_bodega3)
        cantidad_bodega_EsquinaInfIzquierda.configure(text=cant_bodega3)
        valor_U_EsquinaInfIzquierda.configure(text=(f"$ {ventas3}"))
        vendido_EsqInfIzq.configure(text=cant_ventas3)
        messagebox.showinfo(title="Informacion",message=("Se guardo con exito"))
    if cant_bodega3<cant_minima3:
        messagebox.showinfo(title="Informacion",message=("Es menor la cantidad de bodega que la cantidad minima, por ello no se puede realizar la venta"))
    else:
        venta=Tk()
        venta.title("Vender")
        venta.geometry("400x90")

        cantVenta=Label(venta, text="Cantidad a vender:", font=("Times New Roman",12))
        cantVenta.place(x=0,y=10)
        cantidad_venta=Entry(venta,width=21)
        cantidad_venta.place(x=200,y=11)
        button_cant_venta=Button(venta,text="Vender", font=("Times New Roman",12),width=13, command=guardar_vender_3)
        button_cant_venta.place(x=0,y=40)

        venta.mainloop()

#Funcion venta del pan
def vender_pan_DerInf():
    global cant_bodega4
    global cant_minima4
    global cant_ventas4
    def guardar_vender_4():
        global cant_ventas4
        global cant_bodega4
        cant_ventas4+=int(cantidad_venta.get())
        if tipo_producto2==distintosTipos[0]:
            ventas4=int(cant_ventas4*(valor4+IVA_papel))
        elif tipo_producto1==distintosTipos[1]:
            ventas4=int(cant_ventas4*(valor4+IVA_supermercado))
        else:
            ventas4=int(cant_ventas4*(valor4+IVA_drogueria))
        if cant_bodega4>cant_minima4:
            cant_bodega4=int(cant_bodega4-cant_ventas4)
        else:
            cant_bodega4=int(cant_ventas4-cant_bodega4)
        cantidad_bodega_EsquinaInfDerecha.configure(text=cant_bodega4)
        valor_U_EsquinaInfDerecha.configure(text=(f"$ {ventas4}"))
        vendido_EsqInfDer.configure(text=cant_ventas4)
        messagebox.showinfo(title="Informacion",message=("Se guardo con exito"))
    if cant_bodega4<cant_minima4:
        messagebox.showinfo(title="Informacion",message=("Es menor la cantidad de bodega que la cantidad minima, por ello no se puede realizar la venta"))
    else:
        venta=Tk()
        venta.title("Vender")
        venta.geometry("400x90")

        cantVenta=Label(venta, text="Cantidad a vender:", font=("Times New Roman",12))
        cantVenta.place(x=0,y=10)
        cantidad_venta=Entry(venta,width=21)
        cantidad_venta.place(x=200,y=11)
        button_cant_venta=Button(venta,text="Vender", font=("Times New Roman",12),width=13, command=guardar_vender_4)
        button_cant_venta.place(x=0,y=40)
        venta.destroy()
        venta.mainloop()


#Funciones para los cambios

#Cambio Esquina Izquierda Superior
def cambiar_Izquierda_Superior():
    cambios=Tk()
    cambios.title("Cambio de Producto")
    cambios.geometry("400x150")

    nuevo_nombre_prod=Label(cambios, text="Nuevo nombre", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_nombre_prod.place(x=0, y=0)
    newNameProd=Entry(cambios, width=20)
    newNameProd.place(x=230, y=0)

    nuevo_tipo_producto=Label(cambios, text="Tipo producto", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_tipo_producto.place(x=0, y=20)
    newTypeProd=ttk.Combobox(cambios, width=20)
    newTypeProd.place(x=230, y=20)
    newTypeProd["values"]=distintosTipos

    valor_unitario_nuevo_producto=Label(cambios, text="Valor Unitario", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    valor_unitario_nuevo_producto.place(x=0, y=40)
    valorUNuevoProd=Entry(cambios, width=20)
    valorUNuevoProd.place(x=230, y=40)

    cantidad_bodega_nuevo_producto=Label(cambios, text="Cantidad Bodega", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_bodega_nuevo_producto.place(x=0, y=60)
    cantBodNewProd=Entry(cambios, width=20)
    cantBodNewProd.place(x=230, y=60)

    cantidad_minima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_minima_nuevo_producto.place(x=0, y=80)
    cantMinNewProd=Entry(cambios, width=20)
    cantMinNewProd.place(x=230, y=80)
    def guardar_cambios():
        prodLapiz.configure(newNameProd.get()) #Nombre del nuevo producto
        tipo_EsqIzqSup.configure(newTypeProd.get()) #Variable de tipo
        valor_U_EsquinaSupIzquierda.configure(valorUNuevoProd.get()) #Valor unitario
        cantidad_bodega_EsquinaSupIzquierda.configure(cantBodNewProd.get()) #Cantidad en bodega
        minimo_EsqSupIzq.configure(cantMinNewProd.get()) #Cantidad minima
        messagebox.showinfo(text="Cambios", message="Se realizaron los cambios correctamente")
        cambios.destroy()

    button_guardar_cambios=Button(cambios, text="Guardar cambios", font=("Times New Roman", 13), width=25, command=guardar_cambios)
    button_guardar_cambios.place(x=0, y=115)

    cambios.mainloop()


#Cambio esquina derecha superior
def cambiar_Derecha_Superior():
    cambios=Tk()
    cambios.title("Cambio de Producto")
    cambios.geometry("400x150")


    nuevo_nombre_prod=Label(cambios, text="Nuevo nombre", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_nombre_prod.place(x=0, y=0)
    newNameProd=Entry(cambios, width=20)
    newNameProd.place(x=230, y=0)

    nuevo_tipo_producto=Label(cambios, text="Tipo producto", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_tipo_producto.place(x=0, y=20)
    newTypeProd=ttk.Combobox(cambios, width=20)
    newTypeProd.place(x=230, y=20)
    newTypeProd["values"]=distintosTipos

    valor_unitario_nuevo_producto=Label(cambios, text="Valor Unitario", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    valor_unitario_nuevo_producto.place(x=0, y=40)
    valorUNuevoProd=Entry(cambios, width=20)
    valorUNuevoProd.place(x=230, y=40)

    cantidad_bodega_nuevo_producto=Label(cambios, text="Cantidad Bodega", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_bodega_nuevo_producto.place(x=0, y=60)
    cantBodNewProd=Entry(cambios, width=20)
    cantBodNewProd.place(x=230, y=60)

    cantidad_minima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Times New Roman", 13), borderwidth=2, width=30, relief="raised")
    cantidad_minima_nuevo_producto.place(x=0, y=80)
    cantMinNewProd=Entry(cambios, width=20)
    cantMinNewProd.place(x=230, y=80)


    def guardar_cambios():
        prodAspirina.configure(newNameProd.get()) #Nombre del nuevo producto
        tipo_EsqDerSup.configure(newTypeProd.get()) #Variable de tipo
        valor_U_EsquinaSupDerecha.configure(valorUNuevoProd.get()) #Valor unitario
        cantidad_bodega_EsquinaSupDerecha.configure(cantBodNewProd.get()) #Cantidad en bodega
        minimo_EsqSupDer.configure(cantMinNewProd.get()) #Cantidad minima
        messagebox.showinfo(text="Cambios", message="Se realizaron los cambios correctamente")
        cambios.destroy()

    button_guardar_cambios=Button(cambios, text="Guardar cambios", font=("Times New Roman", 13), width=25, command=guardar_cambios)
    button_guardar_cambios.place(x=0, y=100)

    cambios.mainloop()



#Cambio esquina inferior izquierda
def cambiar_Izquierda_Inferior():
    cambios=Tk()
    cambios.title("Cambio de Producto")
    cambios.geometry("400x150")

    nuevo_nombre_prod=Label(cambios, text="Nuevo nombre", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_nombre_prod.place(x=0, y=0)
    newNameProd=Entry(cambios, width=20)
    newNameProd.place(x=230, y=0)

    nuevo_tipo_producto=Label(cambios, text="Tipo producto", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_tipo_producto.place(x=0, y=20)
    newTypeProd=ttk.Combobox(cambios, width=20)
    newTypeProd.place(x=230, y=20)
    newTypeProd["values"]=distintosTipos

    valor_unitario_nuevo_producto=Label(cambios, text="Valor Unitario", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    valor_unitario_nuevo_producto.place(x=0, y=40)
    valorUNuevoProd=Entry(cambios, width=20)
    valorUNuevoProd.place(x=230, y=40)

    cantidad_bodega_nuevo_producto=Label(cambios, text="Cantidad Bodega", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_bodega_nuevo_producto.place(x=0, y=60)
    cantBodNewProd=Entry(cambios, width=20)
    cantBodNewProd.place(x=230, y=60)

    cantidad_minima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_minima_nuevo_producto.place(x=0, y=80)
    cantMinNewProd=Entry(cambios, width=20)
    cantMinNewProd.place(x=230, y=80)

    def guardar_cambios():
        prodBorrador.configure(newNameProd.get()) #Nombre del nuevo producto
        tipo_EsqInfIzq.configure(newTypeProd.get()) #Variable de tipo
        valor_U_EsquinaInfIzquierda.configure(valorUNuevoProd.get()) #Valor unitario
        cantidad_bodega_EsquinaInfIzquierda.configure(cantBodNewProd.get()) #Cantidad en bodega
        minimo_EsqInfIzq.configure(cantMinNewProd.get()) #Cantidad minima
        messagebox.showinfo(text="Cambios", message="Se realizaron los cambios correctamente")
        cambios.destroy()

    button_guardar_cambios=Button(cambios, text="Guardar cambios", font=("Times New Roman", 13), width=25, command=guardar_cambios)
    button_guardar_cambios.place(x=0, y=100)

    cambios.mainloop()



#Cambio esquina inferior derecha
def cambiar_Derecha_Inferior():
    cambios=Tk()
    cambios.title("Cambio de Producto")
    cambios.geometry("400x150")

    nuevo_nombre_prod=Label(cambios, text="Nuevo nombre", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_nombre_prod.place(x=0, y=0)
    newNameProd=Entry(cambios, width=20)
    newNameProd.place(x=230, y=0)

    nuevo_tipo_producto=Label(cambios, text="Tipo producto", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    nuevo_tipo_producto.place(x=0, y=20)
    newTypeProd=ttk.Combobox(cambios, width=20)
    newTypeProd.place(x=230, y=20)
    newTypeProd["values"]=distintosTipos

    valor_unitario_nuevo_producto=Label(cambios, text="Valor Unitario", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    valor_unitario_nuevo_producto.place(x=0, y=40)
    valorUNuevoProd=Entry(cambios, width=20)
    valorUNuevoProd.place(x=230, y=40)

    cantidad_bodega_nuevo_producto=Label(cambios, text="Cantidad Bodega", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_bodega_nuevo_producto.place(x=0, y=60)
    cantBodNewProd=Entry(cambios, width=20)
    cantBodNewProd.place(x=230, y=60)

    cantidad_minima_nuevo_producto=Label(cambios, text="Cantidad Minima", font=("Times New Roman", 13), borderwidth=2, width=20, relief="groove")
    cantidad_minima_nuevo_producto.place(x=0, y=80)
    cantMinNewProd=Entry(cambios, width=20)
    cantMinNewProd.place(x=230, y=80)
    def guardar_cambios():
        prodPan.configure(newNameProd.get()) #Nombre del nuevo producto
        tipo_EsqInfDer.configure(newTypeProd.get()) #Variable de tipo
        valor_U_EsquinaInfDerecha.configure(valorUNuevoProd.get()) #Valor unitario
        cantidad_bodega_EsquinaInfDerecha.configure(cantBodNewProd.get()) #Cantidad en bodega
        minimo_EsqInfDer.configure(cantMinNewProd.get()) #Cantidad minima
        messagebox.showinfo("Cambios", "Se realizaron los cambios correctamente")
        cambios.destroy()

    button_guardar_cambios=Button(cambios, text="Guardar cambios", font=("Times New Roman", 13), width=25, command=guardar_cambios)
    button_guardar_cambios.place(x=0, y=100)

    cambios.mainloop()



def producto_mas_vendido():
    global prodLapiz
    global prodAspirina
    global prodBorrador
    global prodPan
    textoLapiz = prodLapiz.cget('text')
    textoAspirina=prodAspirina.cget('text')
    textoBorrador=prodBorrador.cget('text')
    textoPan=prodPan.cget('text')

    if ventas1>ventas2 and ventas1>ventas3 and ventas1>ventas4:
        messagebox.showinfo("Resultado", f"El producto más vendido es {textoLapiz}")
    elif ventas2>ventas1 and ventas2>ventas3 and ventas2>ventas4:
        messagebox.showinfo("Resultado",f"El producto más vendido es {textoAspirina}")
    elif ventas3>ventas1 and ventas3>ventas2 and ventas3>ventas4:
        messagebox.showinfo("Resultado", f"El producto más vendido es {textoBorrador}")
    else:
        messagebox.showinfo("Resultado", f"El producto más vendido es {textoPan}")

def producto_con_menos_ventas():
    global prodLapiz
    global prodAspirina
    global prodBorrador
    global prodPan
    textoLapiz = prodLapiz.cget('text')
    textoAspirina=prodAspirina.cget('text')
    textoBorrador=prodBorrador.cget('text')
    textoPan=prodPan.cget('text')
    if ventas1<ventas2 and ventas1<ventas3 and ventas1<ventas4:
        messagebox.showinfo("Resultado", f"El producto menos vendido es {textoLapiz}")
    elif ventas2<ventas1 and ventas2<ventas3 and ventas2<ventas4:
        messagebox.showinfo("Resultado",f"El producto menos vendido es {textoAspirina}")
    elif ventas3<ventas1 and ventas3<ventas2 and ventas3<ventas4:
        messagebox.showinfo("Resultado", f"El producto menos vendido es {textoBorrador}")
    else:
        messagebox.showinfo("Resultado",f"El producto menos vendido es {textoPan}")


def dinero_en_caja():
    global cant_ventas1
    global cant_ventas2
    global cant_ventas3
    global cant_ventas4
    global dinero_total
    dinero_total=0.0
    dinero_total = float(cant_ventas1+cant_ventas2+cant_ventas3+cant_ventas4)
    messagebox.showinfo("Total Dinero de la tienda", f"El dinero total de la tienda es de ${dinero_total}")


#Promedio de las ventas realizadas
def promedio_ventas():
    global cant_ventas1
    global cant_ventas2
    global cant_ventas3
    global cant_ventas4
    global dinero_total
    promedioDeVentasRealizadas=float(cant_ventas1+cant_ventas2+cant_ventas3+cant_ventas4)/4
    messagebox.showinfo("Promedio de ventas", f"El promedio de ventas es de {promedioDeVentasRealizadas}")


#Botones de producto mas vendido, menos vendido, el promedio de ventas y el dinero en caja
button_ProdMasVendido=Button(window, text="Producto más vendido", width=36, command=producto_mas_vendido)
button_ProdMasVendido.place(x=2, y=563)
button_ProdMenosVendido=Button(window, text="Producto menos vendido", width=37, command=producto_con_menos_ventas)
button_ProdMenosVendido.place(x=264, y=563)
button_ProdVentas=Button(window, text="Promedio ventas", width=38, command=promedio_ventas)
button_ProdVentas.place(x=534, y=563)
button_DineroEnCaja=Button(window, text="Dinero en caja", width=45, command=dinero_en_caja)
button_DineroEnCaja.place(x=238, y=590)



#Productos de la tienda

#Datos del Lapiz
prodLapiz=Label(window, text="Lapiz", font=("Times New Roman", 13))
prodLapiz.place(x=0, y=48)

tipo_1_EsquinaIzquierdaSup=Label(window, text="Tipo:", font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
tipo_1_EsquinaIzquierdaSup.place(x=120,y=80)
tipo_EsqIzqSup=Label(window, text=tipo_producto1, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
tipo_EsqIzqSup.place(x=290,y=80)

CantBod_EsquinaSupIzquierda=Label(window, text="Cantidad Bodega:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
CantBod_EsquinaSupIzquierda.place(x=120,y=120)
cantidad_bodega_EsquinaSupIzquierda=Label(window, text=cant_bodega1, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
cantidad_bodega_EsquinaSupIzquierda.place(x=290,y=120)

valor_unitario_EsquinaSupIzquierda=Label(window, text="Valor Unitario:", font=("Times New Roman",12),  borderwidth=2, width=15, relief="groove")
valor_unitario_EsquinaSupIzquierda.place(x=120,y=160)
valor_U_EsquinaSupIzquierda=Label(window, text=valor1, font=("Times New Roman",12),  borderwidth=2, width=10, relief="groove")
valor_U_EsquinaSupIzquierda.place(x=290,y=160)

cant_vendida_EsqSupIzquierda=Label(window, text="Cantidad Vendida:", font=("Times New Roman",12),  borderwidth=2, width=15, relief="groove")
cant_vendida_EsqSupIzquierda.place(x=120,y=200)
vendido_EsqSupIzq=Label(window, text=cant_ventas1, font=("Times New Roman",12),  borderwidth=2, width=10, relief="groove")
vendido_EsqSupIzq.place(x=290,y=200)

cant_min_EsqSuperiorIzq=Label(window, text="Cantidad Minima:", font=("Times New Roman",12),  borderwidth=2, width=15, relief="groove")
cant_min_EsqSuperiorIzq.place(x=120,y=240)
minimo_EsqSupIzq=Label(window, text=cant_minima1, font=("Times New Roman",12),  borderwidth=2, width=10, relief="groove")
minimo_EsqSupIzq.place(x=290,y=240)


#(--------------PRODUCTO 1 AL 2----------------)

#Datos de la Aspirina
prodAspirina=Label(window, text="Aspirina", font=("Times New Roman", 13))
prodAspirina.place(x=400, y=48)

tipo_3_EsquinaDerechaSup=Label(window, text="Tipo:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
tipo_3_EsquinaDerechaSup.place(x=540,y=80)
tipo_EsqDerSup=Label(window, text=tipo_producto2, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
tipo_EsqDerSup.place(x=690,y=80)

CantBod_EsquinaSupDerecha=Label(window, text="Cantidad Bodega:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
CantBod_EsquinaSupDerecha.place(x=540,y=120)
cantidad_bodega_EsquinaSupDerecha=Label(window, text=cant_bodega2, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
cantidad_bodega_EsquinaSupDerecha.place(x=690,y=120)

valor_unitario_EsquinaSupDerecha=Label(window, text="Valor Unitario:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
valor_unitario_EsquinaSupDerecha.place(x=540,y=160)
valor_U_EsquinaSupDerecha=Label(window, text=valor2, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
valor_U_EsquinaSupDerecha.place(x=690,y=160)

cant_vendida_EsqSupDerecha=Label(window, text="Cantidad Vendida:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_vendida_EsqSupDerecha.place(x=540,y=200)
vendido_EsqSupDer=Label(window, text=cant_ventas2, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
vendido_EsqSupDer.place(x=690,y=200)

cant_min_EsqSuperiorDer=Label(window, text="Cantidad Minima:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_min_EsqSuperiorDer.place(x=540,y=240)
minimo_EsqSupDer=Label(window, text=cant_minima2, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
minimo_EsqSupDer.place(x=690,y=240)



# (---------------Producto 2 AL 3 ----------)

#Datos del borrador
prodBorrador=Label(window, text="Borrador", font=("Times New Roman", 13))
prodBorrador.place(x=0, y=310)

tipo_1_EsquinaIzquierdaInf=Label(window, text="Tipo:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
tipo_1_EsquinaIzquierdaInf.place(x=130,y=340)
tipo_EsqInfIzq=Label(window, text=tipo_producto3, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
tipo_EsqInfIzq.place(x=270,y=340)

CantBod_EsquinaInfIzquierda=Label(window, text="Cantidad Bodega:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
CantBod_EsquinaInfIzquierda.place(x=130,y=376)
cantidad_bodega_EsquinaInfIzquierda=Label(window, text=cant_bodega3, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
cantidad_bodega_EsquinaInfIzquierda.place(x=270,y=376)

valor_unitario_EsquinaInfIzquierda=Label(window, text="Valor Unitario:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
valor_unitario_EsquinaInfIzquierda.place(x=130,y=416)
valor_U_EsquinaInfIzquierda=Label(window, text=valor3, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
valor_U_EsquinaInfIzquierda.place(x=270,y=416)

cant_vendida_EsqInfIzquierda=Label(window, text="Cantidad Vendida:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_vendida_EsqInfIzquierda.place(x=130,y=456)
vendido_EsqInfIzq=Label(window, text=cant_ventas3, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
vendido_EsqInfIzq.place(x=270,y=456)

cant_min_EsqInferiorIzq=Label(window, text="Cantidad Minima:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_min_EsqInferiorIzq.place(x=130,y=496)
minimo_EsqInfIzq=Label(window, text=cant_minima3, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
minimo_EsqInfIzq.place(x=270,y=496)

#(----------------Producto del 3 al 4-----------------)

#Datos del Pan
prodPan=Label(window, text="Pan", font=("Times New Roman", 13))
prodPan.place(x=400, y=310)

tipo_1_EsquinaDerechaInf=Label(window, text="Tipo:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
tipo_1_EsquinaDerechaInf.place(x=550,y=342)
tipo_EsqInfDer=Label(window, text=tipo_producto4, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
tipo_EsqInfDer.place(x=690,y=342)

CantBod_EsquinaInfDerecha=Label(window, text="Cantidad Bodega:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
CantBod_EsquinaInfDerecha.place(x=550,y=376)
cantidad_bodega_EsquinaInfDerecha=Label(window, text=cant_bodega4, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
cantidad_bodega_EsquinaInfDerecha.place(x=690,y=376)

valor_unitario_EsquinaInfDerecha=Label(window, text="Valor Unitario:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
valor_unitario_EsquinaInfDerecha.place(x=550,y=416)
valor_U_EsquinaInfDerecha=Label(window, text=valor4, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
valor_U_EsquinaInfDerecha.place(x=690,y=416)

cant_vendida_EsqInfDerecha=Label(window, text="Cantidad Vendida:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_vendida_EsqInfDerecha.place(x=550,y=456)
vendido_EsqInfDer=Label(window, text=cant_ventas4, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
vendido_EsqInfDer.place(x=690,y=456)

cant_min_EsqInferiorDer=Label(window, text="Cantidad Minima:", font=("Times New Roman",12), borderwidth=2, width=15, relief="groove")
cant_min_EsqInferiorDer.place(x=550,y=496)
minimo_EsqInfDer=Label(window, text=cant_minima4, font=("Times New Roman",12), borderwidth=2, width=10, relief="groove")
minimo_EsqInfDer.place(x=690,y=496)


#Botones de Abastececimiento, Venta y cambios
button_abastecer_lapiz=Button(window, text="Abastecer", width=17, command=abastecer_lapiz_IzqSup)
button_abastecer_lapiz.place(x=0, y=282)
button_vender_lapiz=Button(window, text="Vender", width=18, command=vender_lapiz_IzqSup)
button_vender_lapiz.place(x=128, y=282)
button_cambiar_lapiz=Button(window, text="Cambiar", width=18, command=cambiar_Izquierda_Superior)
button_cambiar_lapiz.place(x=263, y=282)

button_abastecer_aspirina=Button(window, text="Abastecer", width=17, command=abastecer_aspirina_DerSup)
button_abastecer_aspirina.place(x=404, y=282)
button_vender_aspirina=Button(window, text="Vender", width=17, command=vender_aspirina_DerSup)
button_vender_aspirina.place(x=532, y=282)
button_cambiar_aspirina=Button(window, text="Cambiar", width=18, command=cambiar_Derecha_Superior)
button_cambiar_aspirina.place(x=662, y=282)

button_abastecer_borrador=Button(window, text="Abastecer", width=17, command=abastecer_borrador_IzqInf)
button_abastecer_borrador.place(x=0, y=535)
button_vender_borrador=Button(window, text="Vender", width=18, command=vender_borrador_IzqInf)
button_vender_borrador.place(x=128, y=535)
button_cambiar_borrador=Button(window, text="Cambiar", width=18, command=cambiar_Izquierda_Inferior)
button_cambiar_borrador.place(x=263, y=535)



button_abastecer_pan=Button(window, text="Abastecer", width=17, command=abastecer_pan_DerInf)
button_abastecer_pan.place(x=404, y=535)
button_vender_pan=Button(window, text="Vender", width=18, command=vender_pan_DerInf)
button_vender_pan.place(x=532, y=535)
button_cambiar_pan=Button(window, text="Cambiar", width=18, command=cambiar_Derecha_Inferior)
button_cambiar_pan.place(x=662, y=535)

titulo=Label(window, text="Sistema de Stock", font=("Arial", 24))
titulo.pack()


window.mainloop()
