from decimal import Decimal

def GetValorDeCuotaFija(self, monto, tasa, cuotas, periodo=MENSUAL, limit_dec=None):
    """
    Retorna el valor actual de la cuota, según el método francés,
    en donde las cuotas son fijas. -> float(x)
 
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)].
    Donde:
    R = renta (cuota)
    P = principal (préstamo adquirido)
    i = tasa de interés
    n = número de periodos
    -> (Moneda valor, Moneda interes, Moneda monto)
    """
    tasa = tasa / Decimal(100)
    if periodo == DIARIO:
        tasa /= Decimal(30.4167)
    elif periodo == SEMANAL:
        tasa /= Decimal(4.34524)
    if periodo == QUINCENAL:
        tasa /= Decimal(2.0)
    elif periodo == ANUAL:
        tasa *= 12

    # Si no se especifica una tasa, se pone un número casi imperceptible para
    # evitar que la formula lanze una excepción de división por cero.
    if not tasa:
        tasa = Decimal(0.00000000001)
    # Furmula para el cálculo según el sistema francés.
    valor = monto * ( (tasa * ((1 + tasa)**cuotas)) / (((1 + tasa)**cuotas) - 1) )
    interes = valor - monto
    if limit_dec:
        return (round(valor, limit_dec), round(interes, limit_dec), round(monto, limit_dec))
    return (valor, interes, monto)
