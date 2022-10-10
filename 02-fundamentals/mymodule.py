SPEED_OF_LIGHT = 300000000 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

def hydrTlak(hloubka, hustota_kapaliny, gravitacni_konstanta):
    '''
        Funkce pro vypocet hydrostatickeho tlaku
    '''
    return hloubka * hustota_kapaliny * gravitacni_konstanta

def time_by_light_speed(lenght):
    '''
    Vrací čas, za který rychlost světla urazí tuto vzdálenost v metrech.

    '''
    return lenght / SPEED_OF_LIGHT


def time_by_sound_speed(length):
    '''
    Vrací čas, za který zvuk urazí určitou vzdálenost.
    Vzdálenost je nutno zadat v kilometrech.
    '''
    return (length * 1000) / SPEED_OF_SOUND


def hmotnostNaMesici(hmotnost, gravKonstPuvod, gravKonstNew):
    '''
    Vypočte naši hmotnost na měsíci.
    '''
    return hmotnost * (gravKonstNew / gravKonstPuvod)