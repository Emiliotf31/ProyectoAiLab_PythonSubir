from menu_modos import *
import random
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox as mss
from leer_escribir import *
   
def menu(comb):
    direc="./Registros_usuarios/Usuario_Actual.csv"
    id_inic=leer_csv(path=direc)[2][0]
    modo_juego(comb,id_inic)

def again(entrena):
    print("AGAIN")
    entrena.destroy()
    #import modo_entrena
    subprocess.call(["python", "modo_entrena.py"])

def ganador(comb):
        global hp_pers,hp_cpu,hp_pers,hp_cpu,t

        direc="./Registros_usuarios/Usuario_Actual.csv"
        id_inic=leer_csv(path=direc)[2][0]

        if hp_pers==0:
            time.sleep(2)
            valor=mss.askyesno(message="Has sido derrotado, mejor suerte para la próxima. ¿Quieres intentarlo de nuevo?",title="Derrota")
            if valor == True:
                t=3
                comb.quit()
                #import escenario_pelea
            else:
                #entrena.destroy()
                t=0
                comb.quit()
                #import escenario_pelea
        if hp_cpu==0:
            mss.showinfo(message="¡Felicidades! Has ganado la batalla. Ahora regresarás al menú principal.",title="Ganador")
            #comb.destroy()
            #modo_juego(comb,id_inic)
##            import escenario_pelea
            t=0
            comb.quit()
            print("Sale de la función Ganador IF")
        print("Sale de la función Ganador")
        #import escenario_pelea
    

def ataq_hp(comb,pos_per,pos_cpu,hp_cpu_sh,hp_pers_sh,selec_ataq,entrena):
    
    #descripcion_jugador=[Especial, Ataque1, Ataque2, Potenciador, Tipo]
    todos=["Aquader","Electder","Firesor","Mousebug","Rockdog","Splant"]
    descr_aq=["Aqua-jet","Cola férrea","Cabezazo","Lluvia","Agua"]
    descr_el=["Trueno","Arañazo","Mordisco","Campo Magnético","Eléctrico"]
    descr_fi=["Llamarada","Embestida","Mordisco","Día Soleado","Fuego"]
    descr_mo=["Picotazo","Embestida","Cabezazo","Esporas","Escarabajo"]
    descr_ro=["Roca afilado","Velocidad","Cola férrea","Campo Rocoso","Roca"]
    descr_sp=["Hoja Navaja","Mordisco","Cabezazo","Rayo Solar","Planta"]
    descr_jugs=[descr_aq,descr_el,descr_fi,descr_mo,descr_ro,descr_sp]
    damage_ataq_pers=[3,2,2]
    damage_ataq_cpu=[3,2,2]

    tipos=["Agua","Eléctrico","Fuego","Escarabajo","Roca","Planta"]
    vent_desv={"Agua": [["Roca","Fuego"],["Eléctrico","Planta"]],
               "Eléctrico": [["Agua","Escarabajo"],["Roca","Planta"]],
               "Fuego": [["Planta","Escarabajo"],["Agua","Roca"]],
               "Escarabajo": [["Roca","Planta"],["Eléctrico","Fuego"]],
               "Roca": [["Eléctrico","Fuego"],["Agua","Planta"]],
               "Planta": [["Roca","Agua","Eléctrico"],["Fuego","Escarabajo"]]}

    print("Establece los valores")
    global t
    t=random.randint(1,2)

    global hp_pers,hp_cpu
    hp_pers,hp_cpu=20,20

    global cont_1,cont
    cont_1,cont=0,0


    if hp_pers==20 or hp_cpu==20:
        global flag
        flag=True
    
    if t==1:
        primer_mov="¡Tu inicias este combate!\nPiensa bien tu movimiento"
        font_1="Ubuntu 22 bold"
        pos_primer_mov=142
        tp=1
    else:
        primer_mov="Tu oponente inicia este\ncombate. ¡Cuidado!"
        font_1="Ubuntu 22 bold"
        pos_primer_mov=168
        tp=2

    global narr
    narr = Label(comb,text=primer_mov,font=font_1,
                 bg="#46b0f5",fg='#000d74',justify=CENTER)
    narr.place(x=pos_primer_mov,y=505)
    comb.update()
    time.sleep(tp)
    
    for i in range(len(descr_jugs)):
        if pos_per == i:
            pers_s=todos[i]
            pers=descr_jugs[i]
            ataq_esp_pers=pers[0]
            ataq1_pers=pers[1]
            ataq2_pers=pers[2]
            pot_pers=pers[3]
            tipo_pers=pers[4]
        if pos_cpu == i:
            cpu_s=todos[i]
            cpu=descr_jugs[i]
            ataq_esp_cpu=cpu[0]
            ataq1_cpu=cpu[1]
            ataq2_cpu=cpu[2]
            pot_cpu=cpu[3]
            tipo_cpu=cpu[4]

    for k in range(len(tipos)):
        if tipo_pers==tipos[k]:
            comp_vent=list(filter(lambda a:a==tipo_cpu,vent_desv.get(tipos[k])[0]))
            if comp_vent!=[]:
                damage_ataq_pers[0]=damage_ataq_pers[0]+2
            comp_desv=list(filter(lambda a:a==tipo_cpu,vent_desv.get(tipos[k])[1]))
            if comp_desv!=[]:
                damage_ataq_pers[0]=damage_ataq_pers[0]-1

    for k in range(len(tipos)):
        if tipo_cpu==tipos[k]:
            comp_vent=list(filter(lambda a:a==tipo_pers,vent_desv.get(tipos[k])[0]))
            if comp_vent!=[]:
                damage_ataq_cpu[0]=damage_ataq_cpu[0]+2
            comp_desv=list(filter(lambda a:a==tipo_pers,vent_desv.get(tipos[k])[1]))
            if comp_desv!=[]:
                damage_ataq_cpu[0]=damage_ataq_cpu[0]-1
        
        
    def selec_attack(attack,hp_cpu_sh,hp_pers_sh):
        all_attack=["esp","atk1","atk2","pot"]
        if attack == "esp":
            ataq_pers=0
        elif attack == "atk1":
            ataq_pers=1
        elif attack == "atk2":
            ataq_pers=2
        elif attack == "pot":
            ataq_pers=3
            
        global hp_pers,hp_cpu,t,narr,flag,cont,cont_1,selec_ataq4
        if t==1:
            if ataq_pers < 3:
                if ataq_pers==0 and cont_1>1:
                    damage_pers=damage_ataq_pers[ataq_pers]+2
                else:
                    damage_pers=damage_ataq_pers[ataq_pers]
                cont_1=cont_1-1
            else:
                cont_1=3
                selec_ataq4.config(state="disable")
                damage_pers=0
            
            if cont_1==0:
                selec_ataq4.config(state="normal")
            comb.update()

            narr.destroy()
            
            if pers_s == "Mousebug":
                x_1=170
            elif pers_s == "Rockdog":
                x_1=180
            elif pers_s == "Splant":
                x_1=195
            else:
                x_1=190

            narr_at=pers_s+" ha usado:\n"+pers[ataq_pers]
            narr = Label(comb,text=narr_at,font="Ubuntu 25 bold",
                         bg="#46b0f5",fg='#000d74',justify=CENTER)
            narr.place(x=x_1,y=505)
            comb.update()
            print(pers_s, "ha usado", pers[ataq_pers])
            hp_cpu=hp_cpu-damage_pers
            if hp_cpu < 0:
                hp_cpu=0
                
            ##hp_cpu_sh.destroy()
            hp_cpu_text=str(hp_cpu)+" HP"
            hp_cpu_sh.config(text=hp_cpu_text)
            hp_cpu_sh.update()
            print("Puntos de vida (Oponente):",hp_cpu)

            time.sleep(1)
            if hp_pers==0 or hp_cpu==0:
                flag=False
                #ganador(entrena)
                print("Sale del COMBATE")
            else:
                t=2
                
        if t==2:
            if cont==0:
                ataq_cpu=random.randint(0,3)
            else:
                ataq_cpu=random.randint(0,2)
                
            if ataq_cpu < 3:
                if ataq_cpu==0 and cont>1:
                    damage_cpu=damage_ataq_cpu[ataq_cpu]+2
                else:
                    damage_cpu=damage_ataq_cpu[ataq_cpu]
                
            else:
                cont=4
                damage_cpu=0

            cont=cont-1
            if cont<0:
                cont=0

            if cpu_s == "Mousebug":
                x_1=170
            elif cpu_s == "Rockdog":
                x_1=180
            elif cpu_s == "Splant":
                x_1=195
            else:
                x_1=190
            
            narr.destroy()
            narr_at=cpu_s+" ha usado:\n"+cpu[ataq_cpu]
            narr = Label(comb,text=narr_at,font="Ubuntu 25 bold",
                         bg="#46b0f5",fg='#850000',justify=CENTER)
            narr.place(x=x_1,y=505)
            comb.update()
            print(cpu_s, "ha usado", cpu[ataq_cpu])

            hp_pers=hp_pers-damage_cpu
            if hp_pers < 0:
                hp_pers=0

            ##hp_pers_sh.destroy()
            hp_pers_text=str(hp_pers)+" HP"
            hp_pers_sh.config(text=hp_pers_text)
            hp_pers_sh.update()
            print("Puntos de vida (Personaje):",hp_pers)

            
            if hp_pers==0 or hp_cpu==0:
                flag=False
##                ganador(entrena)
            else:
                t=1
        #llamar()
        #print("SALE DE LLAMAR")
        print(t)
        ganador(entrena)
        #print("SALE DE GANADOR y COMBATIR")
        
    print("SALE DE SELEC_ATTACK")
    all_attack=["esp","atk1","atk2","pot"]

    def llamar():
        print("ENTRA EN LLAMAR")
        print(flag)
        global cont_1
        while flag==True:
            if t==1:
                selec_ataq1 = Button(comb, text=pers[0], width=20, height=1,
                                    font="Ubuntu 15 normal",activebackground="#ca9e20"
                                    ,relief=RAISED,bg="#c7ca20",justify=CENTER,
                                    command=lambda:selec_attack("esp",
                                                                hp_cpu_sh,hp_pers_sh))
                selec_ataq1.place(x=400,y=90)
                selec_ataq2 = Button(comb, text=pers[1], width=20, height=1,
                                    font="Ubuntu 15 normal",activebackground="#ca9e20"
                                    ,relief=RAISED,bg="#c7ca20",justify=CENTER,
                                    command=lambda:selec_attack("atk1",
                                                                hp_cpu_sh,hp_pers_sh))
                selec_ataq2.place(x=400,y=131)
                selec_ataq3 = Button(comb, text=pers[2], width=20, height=1,
                                    font="Ubuntu 15 normal",activebackground="#ca9e20"
                                    ,relief=RAISED,bg="#c7ca20",justify=CENTER,
                                    command=lambda:selec_attack("atk2",
                                                                hp_cpu_sh,hp_pers_sh))
                selec_ataq3.place(x=400,y=172)
                global selec_ataq4
                selec_ataq4 = Button(comb,text=pers[3], width=20, height=1,
                                    font="Ubuntu 15 normal",activebackground="#ca9e20"
                                    ,relief=RAISED,bg="#c7ca20",justify=CENTER,
                                    command=lambda:selec_attack("pot",
                                                                hp_cpu_sh,hp_pers_sh))
                selec_ataq4.place(x=400,y=213)
                
                print("Después del clic",t)
                comb.mainloop()
                print("SALE DEL LOOP")

                
            if t==2:
                selec_attack(all_attack[0],hp_cpu_sh,hp_pers_sh)
            print("Dentro del while",t)
        
            
    print("ANTES DE ENTRAR EN LLAMAR")
    print(flag) 
    llamar()
    print("SALE DE EN LLAMAR")
    print(t)
    if t==0:
        menu(entrena)
    elif t==3:
        again(entrena)
    
    print("Se acabó el juego")





