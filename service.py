# Module: default
# Author: Joseska y Jon
# Muchas gracias a Oscar Alonso
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import xbmc, time
import xbmcaddon
import xbmcgui

ADDON_SETTINGS = xbmcaddon.Addon()
ID = ADDON_SETTINGS.getAddonInfo('id') 

def log(msg, level=xbmc.LOGDEBUG):
        xbmc.log(msg='[{addon}]: {msg}'.format(addon=ID, msg=msg), level=level)


get_condvisibility = xbmc.getCondVisibility

class Carga():  
    def carga_Palantir():
        # Variables condicionales sujetas a ajustes en la skin para indicar cantidad de tiempo.
        rapido = get_condvisibility("Skin.HasSetting(Behaviour.waitFast)")
        medio = get_condvisibility("Skin.HasSetting(Behaviour.waitMedium)")
        lento = get_condvisibility("Skin.HasSetting(Behaviour.waitSlow)")
        # Inicialización de variables de tiempo según el ajuste activo.
        if rapido:
            tiempoSistema=3
            tiempoAddon=2
            tiempoPalantir=5
        elif medio:
            tiempoSistema=8
            tiempoAddon=2
            tiempoPalantir=15
        else:
            tiempoSistema=14
            tiempoAddon=2
            tiempoPalantir=23
        xbmcgui.Dialog().notification("Arctic Horizon 2 Recauchutado", "Iniciando Palantir de forma segura, tardará unos " 
               + str(tiempoSistema + tiempoAddon + tiempoPalantir) +  " segundos")
        #desactivar addon Palantir3
        xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "plugin.video.palantir3", "enabled": false }, "id":1}')

        # Tiempo suficiente para que el sistema se ponga en marcha
        time.sleep(tiempoSistema)
                
        # Activar addon Palantir3
        xbmc.executeJSONRPC('{"jsonrpc":"2.0", "method":"Addons.SetAddonEnabled", "params":{ "addonid": "plugin.video.palantir3", "enabled": true }, "id":1}')

        # Tiempo suficiente para que el addon se active 
        time.sleep(tiempoAddon)

        #ejecutar addon Palantir3
        xbmc.executebuiltin('RunAddon("plugin.video.palantir3")')

        #volver a la pantalla de inicio
        xbmc.executebuiltin('ActivateWindow(home)')

        xbmcgui.Dialog().notification("Arctic Horizon 2 Recauchutado", "Faltan unos " 
               + str(tiempoPalantir) +  " segundos para terminar de cargar Palantir")

        # Tiempo suficiente para que el addon de Palantir3 se ejecute
        time.sleep(tiempoPalantir)

        #Recargar skin
        xbmc.executebuiltin('ReloadSkin()')


# Inicio del script
if get_condvisibility("[Skin.HasSetting(Behaviour.waitFast) | Skin.HasSetting(Behaviour.waitMedium) | Skin.HasSetting(Behaviour.waitSlow) ]"):
    Carga.carga_Palantir()


