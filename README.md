# Building frontend
```bash
docker-compose run --rm node bash -c "npm install && npm run build"
```

# Valores iniciales para existencias
```js
[    
    {
        "nombre" : "Bomba de infusion",
        "marca" : "Hospira",
        "referencia" : "Plum A+",
        "cantidad" : "5"
    },
    {
        "nombre" : "Regulador vacío adulto",
        "marca" : "FLOW METER",
        "referencia" : "VR-C2UD-CMA",
        "cantidad" : "3"
    },
    {
        "nombre" : "Flujometro",
        "marca" : "AMVEX",
        "referencia" : "15 LITROS",
        "cantidad" : "10"
    },
    {
        "nombre" : "Tensiometro",
        "marca" : "ALPK2",
        "referencia" : "NT",
        "cantidad" : "1"
    },
    {
        "nombre" : "Ventilador",
        "marca" : "Newport",
        "referencia" : "E360T",
        "cantidad" : "9"
    }
]
```


# Valores iniciales para proveedores
```js
[
    {
        "Nombre" : "FLOW METER",
        "Telefono" : 3322114,
        "Ciudad" : "Medellin",
        "Direccion" : "Calle 54 # 2-32",
        "Email" : "contacto@flowmeter.com"
    },
    {
        "Nombre" : "AT. MEDICAS",
        "Telefono" : 3654214,
        "Ciudad" : "Medellin",
        "Direccion" : "Calle 14 # 21-2",
        "Email" : "contacto@atmedicas.com"
    },
    {
        "Nombre" : "LINDE COLOMBIA S.A.",
        "Telefono" : 202154,
        "Ciudad" : "Medellin",
        "Direccion" : "Calle 101 # 54-3",
        "Email" : "contacto@lindesa.com"
    }
]
```