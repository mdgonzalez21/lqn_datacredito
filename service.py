import json

from lqn_soap_datacredito.utils import lqn_datacredito_client, pretty_dict

def handler(event, context):
    client = lqn_datacredito_client()
    service = event.get("service")
    data = event.get("data", None)
    result = {"error": True, "message": "Ningun servicio utilizado"}
    if service == "consultar_historial":
        result = client.consultar_hc2(data)
        
    return json.dumps(result.dict())
        
CONSULTA = {
    "service": "consultar_historial",
    "data":{
        "clave": "02ZOG",
        "identificacion": "6469739",
        "primerApellido": "ALFONSO",
        "producto": "64",
        "tipoIdentificacion": "1",
        "usuario": "900986913",
    }
}

resultado = handler(CONSULTA, None)

# result = pretty_dict(resultado.dict())

print(resultado)