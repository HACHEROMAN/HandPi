import time
import sys
import threading
sys.path.append('/home/pi/uHand_Pi/')
from pyngrok import conf, ngrok
from flask import Flask, request, jsonify
import LeArm

app = Flask(__name__)

control_total_mode = False
juego = False
lenguaje_signos = False
agarrar = False
LeArm.initLeArm([0, 0, 0, 0, 0, 0])

@app.route("/", methods=["POST"])
def handle_request():
    global control_total_mode
    global juego
    global lenguaje_signos
    global agarrar
    data = request.get_json()
    request_type = data["request"]["type"]
    should_end_session = False
    
    if request_type == "LaunchRequest":
        mensaje = "Puedes decir modo rock, saludo uno, saludo dos, okei, juego, numeros, agarrar objetos. O puedes decir 'control total' para tener control completo."
        print(">>> Skill iniciada.")

    elif request_type == "IntentRequest":
        intent = data["request"]["intent"]["name"]
        
        if not control_total_mode and not juego and not lenguaje_signos and not agarrar:

            if intent == "ModoDosIntent":
                mensaje = "Activando el modo rock"
                print(">>> Ejecutando acción: archivo 7_2_25")
                LeArm.runActionGroup("7_2_25", 1000)
                should_end_session = False

            elif intent == "ModoCincoIntent":
                mensaje = "Hola, mucho gusto"
                print(">>> Ejecutando acción: archivo saludo_dos")
                LeArm.runActionGroup("saludo_dos", 1000)
                should_end_session = False
            
            elif intent == "ModoCuatroIntent":
                mensaje = "Hola, mucho gusto"
                print(">>> Ejecutando acción: archivo 19_hello")
                LeArm.runActionGroup("19_hello", 1000)
                should_end_session = False

            elif intent == "ModoSeisIntent":
                mensaje = "okei"
                print(">>> Ejecutando acción: archivo 13_3_345")
                LeArm.runActionGroup("13_3_345", 1000)
                should_end_session = False
            
            elif intent == "ModoSacarDedoIntent":
                mensaje = "Hola muy buenas"
                print(">>> Ejecutando acción: archivo saludo_con_dedo")
                LeArm.runActionGroup("saludo_con_dedo", 1000)
                should_end_session = False

            # Activar control total
            elif intent == "ControlTotalIntent":
                control_total_mode = True
                mensaje = "Control total activado. Ahora puedes decir abre o cierra el dedo pulgar, índice, medio, anular, meñique, ademas puedes decir cerrar, abrir, mueve a la izquierda, derecha o centro la mano. Para regresar, di 'salir del control total'."
                print(">>> Activado control total.")
                should_end_session = False

            elif intent == "ModoJuegoIntent":
                juego = True
                mensaje = "Juego piedra papel o tijera activado. Ahora puedes decir piedra papel o tijera. Para regresar, di 'salir del juego'."
                print(">>> Activado juego.")
                should_end_session = False

            elif intent == "ModoSignosIntent":
                lenguaje_signos = True
                mensaje = "Numeros en lenguaje de señas activado. Ahora puedes decir un numero del uno al diez. Para regresar, di 'salir de numeros'."
                print(">>> Activado numeros.")
                should_end_session = False
            
            elif intent == "ModoAgarreIntent":
                agarrar = True
                mensaje = "Agarrar objetos activado. Ahora puedes decir agarra y mueve a la izquierda o a la derecha. Para regresar, di 'salir de agarrar objetos'."
                print(">>> Activado agarrar objetos.")
                should_end_session = False

            elif intent == "AMAZON.HelpIntent":
                mensaje = "Puedes decir modo rock, saludo uno, saludo dos, okei, juego, numeros, agarrar objetos. O puedes decir 'control total' para tener control completo."
                print(">>> Ayuda solicitada.")
                should_end_session = False

            else:
                mensaje = "No entendí eso. Puedes solicitar ayuda, solo di, ayuda."
                print(">>> Intento no reconocido.")
                should_end_session = False

        elif control_total_mode:
            if intent == "ModoSieteIntent":
                mensaje = "Cerrando el dedo pulgar"
                print(">>> Ejecutando acción: archivo cierra_pulgar")
                LeArm.runActionGroup("cierra_pulgar", 1000)
                should_end_session = False

            elif intent == "ModoOchoIntent":
                mensaje = "Cerrando el dedo índice"
                print(">>> Ejecutando acción: archivo cierra_indice")
                LeArm.runActionGroup("cierra_indice", 1000)
                should_end_session = False

            elif intent == "ModoNueveIntent":
                mensaje = "Cerrando el dedo del medio"
                print(">>> Ejecutando acción: archivo cierra_dedo_medio")
                LeArm.runActionGroup("cierra_dedo_medio", 1000)
                should_end_session = False

            elif intent == "ModoDiezIntent":
                mensaje = "Cerrando el dedo anular"
                print(">>> Ejecutando acción: archivo cierra_anular")
                LeArm.runActionGroup("cierra_anular", 1000)
                should_end_session = False

            elif intent == "ModoOnceIntent":
                mensaje = "Cerrando el dedo meñique"
                print(">>> Ejecutando acción: archivo cierra_menique")
                LeArm.runActionGroup("cierra_menique", 1000)
                should_end_session = False
                
            elif intent == "ModoPulgarIntent":
                mensaje = "Abriendo el dedo pulgar"
                print(">>> Ejecutando acción: archivo abre_pulgar")
                LeArm.runActionGroup("abre_pulgar", 1000)
                should_end_session = False
            
            elif intent == "ModoIndiceIntent":
                mensaje = "Abriendo el dedo indice"
                print(">>> Ejecutando acción: archivo abre_indice")
                LeArm.runActionGroup("abre_indice", 1000)
                should_end_session = False
                
            elif intent == "ModoMedioIntent":
                mensaje = "Abriendo el dedo del medio"
                print(">>> Ejecutando acción: archivo abre_medio")
                LeArm.runActionGroup("abre_medio", 1000)
                should_end_session = False
                
            elif intent == "ModoAnularIntent":
                mensaje = "Abriendo el dedo anular"
                print(">>> Ejecutando acción: archivo abre_anular")
                LeArm.runActionGroup("abre_anular", 1000)
                should_end_session = False
                
            elif intent == "ModoMeniqueIntent":
                mensaje = "Abriendo el dedo meñique"
                print(">>> Ejecutando acción: archivo abre_menique")
                LeArm.runActionGroup("abre_menique", 1000)
                should_end_session = False
            
            elif intent == "ModoTresIntent":
                mensaje = "Abriendo la mano"
                print(">>> Ejecutando acción: archivo 15_5_12345")
                LeArm.runActionGroup("15_5_12345", 1000)
                should_end_session = False
                
            elif intent == "ModoUnoIntent":
                mensaje = "Cerrando la mano"
                print(">>> Ejecutando acción: archivo 0_0_0")
                LeArm.runActionGroup("0_0_0", 1000)
                should_end_session = False
            
            elif intent == "ModoIzquierdaIntent":
                mensaje = "Moviendo a la izquierda"
                print(">>> Ejecutando acción: archivo mueve_izquierda")
                LeArm.runActionGroup("mueve_derecha", 1000)
                should_end_session = False
            
            elif intent == "ModoDerechaIntent":
                mensaje = "Moviendo a la derecha"
                print(">>> Ejecutando acción: archivo mueve_derecha")
                LeArm.runActionGroup("mueve_izquierda", 1000)
                should_end_session = False
            
            elif intent == "ModoCentroIntent":
                mensaje = "Moviendo al centro"
                print(">>> Ejecutando acción: archivo mueve_centro")
                LeArm.runActionGroup("mueve_centro", 1000)
                should_end_session = False

            elif intent == "ControlTotalSalirIntent":
                mensaje = "Desactivando control total"
                mensaje = "Control total desactivado. Ahora puedes decir modo rock, saludo uno, saludo dos, okei, juego, agarrar objetos. O puedes decir 'control total' para tener control completo."
                print(">>> Desactivando control total.")
                control_total_mode = False
                should_end_session = False

            elif intent == "AMAZON.HelpIntent":
                mensaje = "Ahora puedes decir abre o cierra el dedo pulgar, índice, medio, anular, meñique, ademas puedes decir cerrar, abrir, mueve a la izquierda, derecha o centro la mano.. Para regresar, di 'salir del control total'."
                print(">>> Ayuda solicitada en control total.")
                should_end_session = False

            else:
                mensaje = "No entendí eso. Puedes solicitar ayuda, solo di ayuda."
                print(">>> Intento no reconocido en control total.")
                should_end_session = False

        elif juego:
            
            if intent == "ModoPiedraIntent":
                print(">>> Ejecutando acción: archivo 15_5_12345")
                LeArm.runActionGroup("15_5_12345", 1000)
                mensaje = "Papel,, gané"
                should_end_session = False

            elif intent == "ModoPapelIntent":
                print(">>> Ejecutando acción: archivo tijera_mano")
                LeArm.runActionGroup("tijera_mano", 1000)
                mensaje = "Tijera,, gané"
                should_end_session = False

            elif intent == "ModoTijeraIntent":
                print(">>> Ejecutando acción: archivo 0_0_0")
                LeArm.runActionGroup("0_0_0", 1000)
                mensaje = "Piedra,, gané"
                should_end_session = False

            elif intent == "ModoJuegoSalirIntent":
                mensaje = "Saliendo del juego piedra, papel o tijera"
                mensaje = "Juego desactivado. Ahora puedes decir modo rock, saludo uno, saludo dos, okei, juego, numeros, agarrar objetos. O puedes decir 'control total' para tener control completo."
                print(">>> Desactivando control total.")
                juego = False
                should_end_session = False

            elif intent == "AMAZON.HelpIntent":
                mensaje = "Para jugar puedes decir piedra, papel o tiejera. Para regresar, di 'salir del juego'."
                print(">>> Ayuda solicitada en juego.")
                should_end_session = False

            else:
                mensaje = "No entendí eso. Puedes solicitar ayuda, solo di, ayuda."
                print(">>> Intento no reconocido en juego.")
                should_end_session = False
        
        elif lenguaje_signos:

            if intent == "ModoNumeroUnoIntent":
                print(">>> Ejecutando acción: archivo uno_mano")
                LeArm.runActionGroup("uno_mano", 1000)
                mensaje = "mostrando numero uno"
                should_end_session = False

            elif intent == "ModoNumeroDosIntent":
                print(">>> Ejecutando acción: archivo dos_mano")
                LeArm.runActionGroup("dos_mano", 1000)
                mensaje = "mostrando numero dos"
                should_end_session = False

            elif intent == "ModoNumeroTresIntent":
                print(">>> Ejecutando acción: archivo tres_mano")
                LeArm.runActionGroup("tres_mano", 1000)
                mensaje = "mostrando numero tres"
                should_end_session = False
            
            elif intent == "ModoNumeroCuatroIntent":
                print(">>> Ejecutando acción: archivo cuatro_mano")
                LeArm.runActionGroup("cuatro_mano", 1000)
                mensaje = "mostrando numero cuatro"
                should_end_session = False
            
            elif intent == "ModoNumeroCincoIntent":
                print(">>> Ejecutando acción: archivo cinco_mano")
                LeArm.runActionGroup("cinco_mano", 1000)
                mensaje = "mostrando numero cinco"
                should_end_session = False
            
            elif intent == "ModoNumeroSeisIntent":
                print(">>> Ejecutando acción: archivo seis_mano")
                LeArm.runActionGroup("seis_mano", 1000)
                mensaje = "mostrando numero seis"
                should_end_session = False
            
            elif intent == "ModoNumeroSieteIntent":
                print(">>> Ejecutando acción: archivo siete_mano")
                LeArm.runActionGroup("siete_mano", 1000)
                mensaje = "mostrando numero siete"
                should_end_session = False
            
            elif intent == "ModoNumeroOchoIntent":
                print(">>> Ejecutando acción: archivo ocho_mano")
                LeArm.runActionGroup("ocho_mano", 1000)
                mensaje = "mostrando numero ocho"
                should_end_session = False

            elif intent == "ModoNumeroNueveIntent":
                print(">>> Ejecutando acción: archivo nueve_mano")
                LeArm.runActionGroup("nueve_mano", 1000)
                mensaje = "mostrando numero nueve"
                should_end_session = False
            
            elif intent == "ModoNumeroDiezIntent":
                print(">>> Ejecutando acción: archivo diez_mano")
                LeArm.runActionGroup("diez_mano", 1000)
                mensaje = "mostrando numero diez"
                should_end_session = False

            elif intent == "ModoSignosSalirIntent":
                mensaje = "Saliendo de numeros en lenguaje de señas"
                mensaje = "Numeros desactivados. Ahora puedes decir modo rock, saludo uno, saludo dos, okei, juego, numeros, agarrar objetos. O puedes decir 'control total' para tener control completo."
                print(">>> Desactivando control total.")
                lenguaje_signos = False
                should_end_session = False

            elif intent == "AMAZON.HelpIntent":
                mensaje = "Puedes decir un numero del uno al diez. Para regresar, di 'salir de numeros'."
                print(">>> Ayuda solicitada en numeros.")
                should_end_session = False

            else:
                mensaje = "No entendí eso. Puedes solicitar ayuda, solo di, ayuda."
                print(">>> Intento no reconocido en numeros.")
                should_end_session = False
                
        elif agarrar:
            
            if intent == "ModoAgarrarIzquierdaIntent":
                print(">>> Ejecutando acción: archivo 17_left_move")
                mensaje = "Agarrando y moviendo a la izquierda"
                LeArm.runActionGroup("17_left_move", 1000)
                should_end_session = False

            elif intent == "ModoAgarrarDerechaIntent":
                print(">>> Ejecutando acción: archivo 18_right_move")
                mensaje = "Agarrando y moviendo a la derecha"
                LeArm.runActionGroup("18_right_move", 1000)
                should_end_session = False

            elif intent == "ModoAgarrarSalirIntent":
                mensaje = "Saliendo de agarrar objetos"
                mensaje = "Agarrar objetos desactivado. Ahora puedes decir modo rock, saludo uno, saludo dos, okei, juego, numeros, agarrar objetos. O puedes decir 'control total' para tener control completo."
                print(">>> Desactivando agarrar objetos.")
                agarrar = False
                should_end_session = False

            elif intent == "AMAZON.HelpIntent":
                mensaje = "Ahora puedes decir agarra y mueve a la izquierda o a la derecha. Para regresar, di 'salir de agarrar objetos'."
                print(">>> Ayuda solicitada en agarrar objeto.")
                should_end_session = False

            else:
                mensaje = "No entendí eso. Puedes solicitar ayuda, solo di, ayuda."
                print(">>> Intento no reconocido en agarrar objetos.")
                should_end_session = False

    elif request_type == "AMAZON.CancelIntent" or "AMAZON.StopIntent" or "AMAZON.NoIntent" or "AMAZON.NavigateHomeIntent":
        mensaje = "Hasta luego."
        control_total_mode = False
        juego = False
        lenguaje_signos = False
        print(">>> Sesión finalizada.")
        should_end_session = True

    else:
        mensaje = "No entendí eso. Puedes solicitar ayuda, solo di, ayuda."
        print(">>> Solicitud desconocida.")
        should_end_session = False

    return jsonify({
        "version": "1.0",
        "response": {
            "shouldEndSession": should_end_session,  
            "outputSpeech": {
                "type": "PlainText",
                "text": mensaje
            }
        }
    })

#public_url = ngrok.connect(5000)
#print("Tu endpoint público es:", public_url)

app.run(port=5000)
