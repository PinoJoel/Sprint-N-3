

import os
class Inicializar():
    # Directorio Base
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    """es para que suba al nivel de src / os.path nos busca la ubicación absoluta de nuestro directorio base"""
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"
    
    # JsonData
    Json = basedir + "/pages"
    Environment = 'Dev'
    
    # BROWSER DE PRUEBAS
    NAVEGADOR = 'CHROME'
    
    # DIRECTORIO DE LA EVIDENCIA
    Path_Evidencias = basedir + u'/data/evidencia'
    # HOJA DE DATOS EXCEL
    Excel = basedir + '/data/DataTest.xlsx'
    if Environment == 'Dev':
        URL = 'https://www.grimoldi.com/'
        User = ''
        Password = ''
        