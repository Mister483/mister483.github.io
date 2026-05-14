
"""Default template:

{
    "Comida": "",
    "Kilocalorías": "",
    "Proteínas": "",
    "Grasa total": "",
    "Grasa saturada": "",
    "Grasa insaturada": "",
    "Carbohidratos": "",
    "Fibra": "",
    "Calcio": "",
    "Hierro": "",
    "Yodo": "",
    "Magnesio": "",
    "Zinc": "",
    "Sodio": "",
    "Potasio": "",
    "Fósforo": "",
    "Selenio": "",
    "Vitamina B1": "",
    "Vitamina B2": "",
    "Vitamina B3": "",
    "Vitamina B6": "",
    "Vitamina B9": "",
    "Vitamina B12": "",
    "Vitamina C": "",
    "Vitamina A": "",
    "Vitamina D": "",
    "Vitamina E": ""
},

"""


# Los números hacen referencia a la cantidad de cualquier elemento
# presente por cada 100 gramos de alimento comestible salvo que se indique lo contrario.
comida = [
{
    "Comida": "Defecto", # Agua, fideos, huevos (6), leche, queso (80 gramos), aceite de girasol
    "Kilocalorías": "1375",
    "Proteínas": "92",
    "Grasa total": "73",
    "Grasa saturada": "27",
    "Grasa insaturada": "28",
    "Carbohidratos": "92",
    "Fibra": "4",
    "Calcio": "1708",
    "Hierro": "8",
    "Yodo": "179",
    "Magnesio": "130",
    "Zinc": "6",
    "Sodio": "1488",
    "Potasio": "678",
    "Fósforo": "1378",
    "Selenio": "99",
    "Vitamina B1": "0.5",
    "Vitamina B2": "1.6",
    "Vitamina B3": "18",
    "Vitamina B6": "0.5",
    "Vitamina B9": "192",
    "Vitamina B12": "9",
    "Vitamina C": "14",
    "Vitamina A": "930",
    "Vitamina D": "8",
    "Vitamina E": "8"
},
{
    "Comida": "Aceite de girasol", # 10 gramos
    "Kilocalorías": "90",
    "Proteínas": "0",
    "Grasa total": "10",
    "Grasa saturada": "1.23",
    "Grasa insaturada": "8.75",
    "Carbohidratos": "0",
    "Fibra": "0",
    "Calcio": "0", # Desconocido
    "Hierro": "0", # Desconocido
    "Yodo": "0",
    "Magnesio": "0", # Desconocido
    "Zinc": "0", # Desconocido
    "Sodio": "0", # Desconocido
    "Potasio": "0", # Desconocido
    "Fósforo": "0", # Desconocido
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0", # Desconocido
    "Vitamina D": "0",
    "Vitamina E": "4.9"
},
{
    "Comida": "Aceite de maíz", # 10 gramos
    "Kilocalorías": "90",
    "Proteínas": "0", # Desconocido
    "Grasa total": "10",
    "Grasa saturada": "1.31",
    "Grasa insaturada": "8.70",
    "Carbohidratos": "0",
    "Fibra": "0",
    "Calcio": "0", # Desconocido
    "Hierro": "0", # Desconocido
    "Yodo": "0",
    "Magnesio": "0", # Desconocido
    "Zinc": "0", # Desconocido
    "Sodio": "0", # Desconocido
    "Potasio": "0", # Desconocido
    "Fósforo": "0", # Desconocido
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0", # Desconocido
    "Vitamina D": "0",
    "Vitamina E": "1.7"
},
{
    "Comida": "Aceite de oliva", # 10 gramos
    "Kilocalorías": "90",
    "Proteínas": "0", # Desconocido
    "Grasa total": "10",
    "Grasa saturada": "1.66",
    "Grasa insaturada": "8.15",
    "Carbohidratos": "0",
    "Fibra": "0",
    "Calcio": "0", # Desconocido
    "Hierro": "0",
    "Yodo": "0",
    "Magnesio": "0", # Desconocido
    "Zinc": "0", # Desconocido
    "Sodio": "0", # Desconocido
    "Potasio": "0", # Desconocido
    "Fósforo": "0.1",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0", # Desconocido
    "Vitamina D": "0",
    "Vitamina E": "0.5"
},
{
    "Comida": "Aceitunas",
    "Kilocalorías": "196",
    "Proteínas": "0.8",
    "Grasa total": "20",
    "Grasa saturada": "2.81",
    "Grasa insaturada": "16.23",
    "Carbohidratos": "1",
    "Fibra": "4.4",
    "Calcio": "63",
    "Hierro": "1.5",
    "Yodo": "1",
    "Magnesio": "12",
    "Zinc": "0",
    "Sodio": "2250",
    "Potasio": "91",
    "Fósforo": "17",
    "Selenio": "0.9",
    "Vitamina B1": "0.03",
    "Vitamina B2": "0.07",
    "Vitamina B3": "1",
    "Vitamina B6": "0.02",
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "22",
    "Vitamina D": "0",
    "Vitamina E": "1,99"
},
{
    "Comida": "Agua", # 3 litros
    "Kilocalorías": "0",
    "Proteínas": "0",
    "Grasa total": "0",
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "0",
    "Fibra": "0",
    "Calcio": "240",
    "Hierro": "0",
    "Yodo": "0",
    "Magnesio": "36",
    "Zinc": "0",
    "Sodio": "33",
    "Potasio": "9",
    "Fósforo": "0",
    "Selenio": "0",
    "Vitamina B1": "0",
    "Vitamina B2": "0",
    "Vitamina B3": "0",
    "Vitamina B6": "0",
    "Vitamina B9": "0",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Almendras", # En 25 gramos
    "Kilocalorías": "151",
    "Proteínas": "5",
    "Grasa total": "13.4",
    "Grasa saturada": "1.06",
    "Grasa insaturada": "11.68",
    "Carbohidratos": "0.9",
    "Fibra": "3.6",
    "Calcio": "63.5",
    "Hierro": "1.1",
    "Yodo": "0.5",
    "Magnesio": "64.5",
    "Zinc": "0.4",
    "Sodio": "1.5",
    "Potasio": "215",
    "Fósforo": "128",
    "Selenio": "1",
    "Vitamina B1": "0.06",
    "Vitamina B2": "0.17",
    "Vitamina B3": "1.3",
    "Vitamina B6": "0.03",
    "Vitamina B9": "24",
    "Vitamina B12": "0",
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "5"
},
{
    "Comida": "Arroz",
    "Kilocalorías": "381",
    "Proteínas": "7",
    "Grasa total": "0.9",
    "Grasa saturada": "0.21",
    "Grasa insaturada": "0.55",
    "Carbohidratos": "86",
    "Fibra": "0.2",
    "Calcio": "10",
    "Hierro": "0.5",
    "Yodo": "2",
    "Magnesio": "13",
    "Zinc": "0.2",
    "Sodio": "6",
    "Potasio": "110",
    "Fósforo": "100",
    "Selenio": "7",
    "Vitamina B1": "0.05",
    "Vitamina B2": "0.03",
    "Vitamina B3": "3.1",
    "Vitamina B6": "0.30",
    "Vitamina B9": "20",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0.3"
},
{
    "Comida": "Banana", # Por unidad
    "Kilocalorías": "99",
    "Proteínas": "1.3",
    "Grasa total": "0.3",
    "Grasa saturada": "0.12",
    "Grasa insaturada": "0.14",
    "Carbohidratos": "21.1",
    "Fibra": "3.6",
    "Calcio": "9.5",
    "Hierro": "0.6",
    "Yodo": "2.1",
    "Magnesio": "40.1",
    "Zinc": "0.2",
    "Sodio": "1.1",
    "Potasio": "370",
    "Fósforo": "29.6",
    "Selenio": "1.1",
    "Vitamina B1": "0.06",
    "Vitamina B2": "0.07",
    "Vitamina B3": "0.8",
    "Vitamina B6": "0.54",
    "Vitamina B9": "23.2",
    "Vitamina B12": "0",
    "Vitamina C": "10.6",
    "Vitamina A": "19",
    "Vitamina D": "0",
    "Vitamina E": "0.2"
},
{
    "Comida": "Brócoli",
    "Kilocalorías": "38",
    "Proteínas": "4.4",
    "Grasa total": "0.9",
    "Grasa saturada": "0.2",
    "Grasa insaturada": "0.6",
    "Carbohidratos": "1.8",
    "Fibra": "2.6",
    "Calcio": "56",
    "Hierro": "1.7",
    "Yodo": "2",
    "Magnesio": "22",
    "Zinc": "0.6",
    "Sodio": "8",
    "Potasio": "370",
    "Fósforo": "87",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.1",
    "Vitamina B2": "0.06",
    "Vitamina B3": "1.7",
    "Vitamina B6": "0.14",
    "Vitamina B9": "90",
    "Vitamina B12": "0",
    "Vitamina C": "87",
    "Vitamina A": "69",
    "Vitamina D": "0",
    "Vitamina E": "1.3"
},
{
    "Comida": "Café", # En 50 gramos (una ración)
    "Kilocalorías": "4",
    "Proteínas": "0.3",
    "Grasa total": "0",
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "0.8",
    "Fibra": "0",
    "Calcio": "5",
    "Hierro": "0.2",
    "Yodo": "0",
    "Magnesio": "6",
    "Zinc": "0",
    "Sodio": "3.5",
    "Potasio": "66",
    "Fósforo": "5",
    "Selenio": "0",
    "Vitamina B1": "0.01",
    "Vitamina B2": "0.01",
    "Vitamina B3": "0.7",
    "Vitamina B6": "0",
    "Vitamina B9": "0",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Choclo", # Choclo natural (no enlatado) | Por unidad
    "Kilocalorías": "72",
    "Proteínas": "2.3",
    "Grasa total": "0.5",
    "Grasa saturada": "0.08",
    "Grasa insaturada": "0.41",
    "Carbohidratos": "13.4",
    "Fibra": "1.9",
    "Calcio": "2.8",
    "Hierro": "0.5",
    "Yodo": "0",
    "Magnesio": "22",
    "Zinc": "0.5",
    "Sodio": "3.4",
    "Potasio": "202",
    "Fósforo": "59.8",
    "Selenio": "0.6",
    "Vitamina B1": "0.07",
    "Vitamina B2": "0.06",
    "Vitamina B3": "1.2",
    "Vitamina B6": "0.12",
    "Vitamina B9": "27.5",
    "Vitamina B12": "0",
    "Vitamina C": "5",
    "Vitamina A": "8.3",
    "Vitamina D": "0",
    "Vitamina E": "0.2"
},
{
    "Comida": "Choclo enlatado", # Enlatado específicamente
    "Kilocalorías": "73",
    "Proteínas": "2.9",
    "Grasa total": "1.2",
    "Grasa saturada": "0.2",
    "Grasa insaturada": "0.8",
    "Carbohidratos": "10.7",
    "Fibra": "3.9",
    "Calcio": "4",
    "Hierro": "0.5",
    "Yodo": "0",
    "Magnesio": "23",
    "Zinc": "0.5",
    "Sodio": "270",
    "Potasio": "220",
    "Fósforo": "79",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.04",
    "Vitamina B2": "0.06",
    "Vitamina B3": "2",
    "Vitamina B6": "0.13",
    "Vitamina B9": "8",
    "Vitamina B12": "0",
    "Vitamina C": "1",
    "Vitamina A": "18.3",
    "Vitamina D": "0",
    "Vitamina E": "0.46"
},
{
    "Comida": "Durazno", # Por unidad
    "Kilocalorías": "72",
    "Proteínas": "1.1",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "15.8",
    "Fibra": "2.5",
    "Calcio": "14.1",
    "Hierro": "0.7",
    "Yodo": "3.5",
    "Magnesio": "15.8",
    "Zinc": "0.1",
    "Sodio": "5.3",
    "Potasio": "458",
    "Fósforo": "38.7",
    "Selenio": "1.8",
    "Vitamina B1": "0.05",
    "Vitamina B2": "0.09",
    "Vitamina B3": "1.8",
    "Vitamina B6": "0.04",
    "Vitamina B9": "5.3",
    "Vitamina B12": "0",
    "Vitamina C": "14.1",
    "Vitamina A": "147",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Fideos", # Aunque hay varios tipos, esta lista recoge información de FEN
    "Kilocalorías": "375",
    "Proteínas": "12",
    "Grasa total": "1.8",
    "Grasa saturada": "0.3",
    "Grasa insaturada": "0.27",
    "Carbohidratos": "75.8",
    "Fibra": "4",
    "Calcio": "25",
    "Hierro": "1.6",
    "Yodo": "0", # Desconocido
    "Magnesio": "53",
    "Zinc": "1.5",
    "Sodio": "11",
    "Potasio": "230",
    "Fósforo": "180",
    "Selenio": "62.2",
    "Vitamina B1": "0.18",
    "Vitamina B2": "0.05",
    "Vitamina B3": "5.4",
    "Vitamina B6": "0.1",
    "Vitamina B9": "23",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0" # Desconocido
},
{
    "Comida": "Frutillas",
    "Kilocalorías": "40",
    "Proteínas": "0.7",
    "Grasa total": "0.5",
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "7",
    "Fibra": "2.2",
    "Calcio": "25",
    "Hierro": "0.8",
    "Yodo": "8",
    "Magnesio": "12",
    "Zinc": "0.1",
    "Sodio": "2",
    "Potasio": "190",
    "Fósforo": "26",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.02",
    "Vitamina B2": "0.04",
    "Vitamina B3": "0.6",
    "Vitamina B6": "0.06",
    "Vitamina B9": "20",
    "Vitamina B12": "0",
    "Vitamina C": "60",
    "Vitamina A": "1",
    "Vitamina D": "0",
    "Vitamina E": "0.2"
},
{
    "Comida": "Garbanzos",
    "Kilocalorías": "373",
    "Proteínas": "19.4",
    "Grasa total": "5",
    "Grasa saturada": "0", # Desconocido
    "Grasa insaturada": "4.16",
    "Carbohidratos": "55",
    "Fibra": "15",
    "Calcio": "145",
    "Hierro": "6.7",
    "Yodo": "0",
    "Magnesio": "160",
    "Zinc": "0.8",
    "Sodio": "26",
    "Potasio": "797",
    "Fósforo": "375",
    "Selenio": "2",
    "Vitamina B1": "0.4",
    "Vitamina B2": "0.15",
    "Vitamina B3": "4.3",
    "Vitamina B6": "0.53",
    "Vitamina B9": "180",
    "Vitamina B12": "0",
    "Vitamina C": "4",
    "Vitamina A": "32",
    "Vitamina D": "0",
    "Vitamina E": "2.88"
},
{
    "Comida": "Harina", # Información de FEN
    "Kilocalorías": "375",
    "Proteínas": "9.3",
    "Grasa total": "1.2",
    "Grasa saturada": "0.16",
    "Grasa insaturada": "0.64",
    "Carbohidratos": "80",
    "Fibra": "3.4",
    "Calcio": "15",
    "Hierro": "1.1",
    "Yodo": "1",
    "Magnesio": "28",
    "Zinc": "0.8",
    "Sodio": "3",
    "Potasio": "130",
    "Fósforo": "120",
    "Selenio": "4",
    "Vitamina B1": "0.09",
    "Vitamina B2": "0.06",
    "Vitamina B3": "2.3",
    "Vitamina B6": "0.15",
    "Vitamina B9": "22",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0" # Desconocido
},
{
    "Comida": "Huevo", # Una unidad
    "Kilocalorías": "84",
    "Proteínas": "7",
    "Grasa total": "6.3",
    "Grasa saturada": "1.75",
    "Grasa insaturada": "3.22",
    "Carbohidratos": "0", # Desconocido
    "Fibra": "0",
    "Calcio": "32.1",
    "Hierro": "1.1",
    "Yodo": "29.8",
    "Magnesio": "6.8",
    "Zinc": "0.7",
    "Sodio": "78.8",
    "Potasio": "73.2",
    "Fósforo": "113",
    "Selenio": "6.2",
    "Vitamina B1": "0.05",
    "Vitamina B2": "0.26",
    "Vitamina B3": "2.1",
    "Vitamina B6": "0.7",
    "Vitamina B9": "28.2",
    "Vitamina B12": "1.4",
    "Vitamina C": "0",
    "Vitamina A": "107",
    "Vitamina D": "0.99",
    "Vitamina E": "0.6"
},
{
    "Comida": "Huevos", # Dos unidades
    "Kilocalorías": "168",
    "Proteínas": "14",
    "Grasa total": "12.6",
    "Grasa saturada": "3.50",
    "Grasa insaturada": "6.44",
    "Carbohidratos": "0", # Desconocido
    "Fibra": "0",
    "Calcio": "64.2",
    "Hierro": "2.2",
    "Yodo": "59.6",
    "Magnesio": "13.6",
    "Zinc": "1.4",
    "Sodio": "157.6",
    "Potasio": "146.4",
    "Fósforo": "226",
    "Selenio": "12.4",
    "Vitamina B1": "0.1",
    "Vitamina B2": "0.52",
    "Vitamina B3": "4.2",
    "Vitamina B6": "0.14",
    "Vitamina B9": "56.4",
    "Vitamina B12": "2.8",
    "Vitamina C": "0",
    "Vitamina A": "214",
    "Vitamina D": "1.98",
    "Vitamina E": "1.2"
},
{
    "Comida": "Kiwi", # Por unidad
    "Kilocalorías": "47",
    "Proteínas": "0.9",
    "Grasa total": "0.4",
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "9.1",
    "Fibra": "1.6",
    "Calcio": "21.5",
    "Hierro": "0.3",
    "Yodo": "0",
    "Magnesio": "12.9",
    "Zinc": "0.1",
    "Sodio": "3.4",
    "Potasio": "249",
    "Fósforo": "30.1",
    "Selenio": "0.5",
    "Vitamina B1": "0.01",
    "Vitamina B2": "0.03",
    "Vitamina B3": "0.5",
    "Vitamina B6": "0.13",
    "Vitamina B9": "0",
    "Vitamina B12": "0",
    "Vitamina C": "50.7",
    "Vitamina A": "2.6",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Leche", # En 0,2 litros (un vaso) | Con proteína agregada La Serenísima
    "Kilocalorías": "74",
    "Proteínas": "9.2",
    "Grasa total": "0",
    "Grasa saturada": "0",
    "Grasa insaturada": "0", # Desconocido
    "Carbohidratos": "9.2",
    "Fibra": "0", # Desconocido
    "Calcio": "298",
    "Hierro": "0", # Desconocido
    "Yodo": "0", # Desconocido
    "Magnesio": "0", # Desconocido
    "Zinc": "0", # Desconocido
    "Sodio": "107",
    "Potasio": "0", # Desconocido
    "Fósforo": "0", # Desconocido
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0.71",
    "Vitamina C": "14",
    "Vitamina A": "128",
    "Vitamina D": "2",
    "Vitamina E": "0" # Desconocido
},
{
    "Comida": "Lentejas",
    "Kilocalorías": "351",
    "Proteínas": "23.8",
    "Grasa total": "1.8",
    "Grasa saturada": "0.33",
    "Grasa insaturada": "1",
    "Carbohidratos": "54",
    "Fibra": "11.7",
    "Calcio": "56",
    "Hierro": "7.1",
    "Yodo": "2",
    "Magnesio": "78",
    "Zinc": "3.1",
    "Sodio": "12",
    "Potasio": "737",
    "Fósforo": "240",
    "Selenio": "9.9",
    "Vitamina B1": "0.5",
    "Vitamina B2": "0.2",
    "Vitamina B3": "5.6",
    "Vitamina B6": "0.6",
    "Vitamina B9": "35",
    "Vitamina B12": "0",
    "Vitamina C": "3",
    "Vitamina A": "10",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Mandarina", # Por unidad
    "Kilocalorías": "73",
    "Proteínas": "1.4",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "15.3",
    "Fibra": "3.2",
    "Calcio": "61.2",
    "Hierro": "0.5",
    "Yodo": "0", # Desconocido
    "Magnesio": "18.7",
    "Zinc": "0.7",
    "Sodio": "3.4",
    "Potasio": "272",
    "Fósforo": "29.2",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.12",
    "Vitamina B2": "0.03",
    "Vitamina B3": "0.5",
    "Vitamina B6": "0.12",
    "Vitamina B9": "35.7",
    "Vitamina B12": "0",
    "Vitamina C": "59.5",
    "Vitamina A": "95.2",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Maní", # En 10 gramos - Información de Cámara del maní (CAM)
    "Kilocalorías": "57",
    "Proteínas": "2.6",
    "Grasa total": "4.8",
    "Grasa saturada": "0.59",
    "Grasa insaturada": "4.2",
    "Carbohidratos": "1.66",
    "Fibra": "0.79",
    "Calcio": "6.5",
    "Hierro": "0.29",
    "Yodo": "0", # Desconocido
    "Magnesio": "17.5",
    "Zinc": "0.33",
    "Sodio": "1",
    "Potasio": "68.2",
    "Fósforo": "39.5",
    "Selenio": "0.69",
    "Vitamina B1": "0.06",
    "Vitamina B2": "0.01",
    "Vitamina B3": "1.27",
    "Vitamina B6": "0.03",
    "Vitamina B9": "24",
    "Vitamina B12": "0", # Desconocido
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "0", # Desconocido
    "Vitamina D": "0", # Desconocido
    "Vitamina E": "0.81"
},
{
    "Comida": "Manteca", # En 15 gramos
    "Kilocalorías": "112",
    "Proteínas": "0.1",
    "Grasa total": "12.5",
    "Grasa saturada": "6.75",
    "Grasa insaturada": "3.52",
    "Carbohidratos": "0", # Desconocido
    "Fibra": "0",
    "Calcio": "2.3",
    "Hierro": "0",
    "Yodo": "5.7",
    "Magnesio": "0.3",
    "Zinc": "0",
    "Sodio": "0.8",
    "Potasio": "2.4",
    "Fósforo": "2.3",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0", # Desconocido
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "124",
    "Vitamina D": "0.11",
    "Vitamina E": "0.3"
},
{
    "Comida": "Manzana", # Por unidad
    "Kilocalorías": "89",
    "Proteínas": "0.5",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "20.2",
    "Fibra": "3.4",
    "Calcio": "10.1",
    "Hierro": "0.7",
    "Yodo": "3.4",
    "Magnesio": "8.4",
    "Zinc": "0.2",
    "Sodio": "3.4",
    "Potasio": "202",
    "Fósforo": "13.4",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.07",
    "Vitamina B2": "0.03",
    "Vitamina B3": "0.3",
    "Vitamina B6": "0.05",
    "Vitamina B9": "8.4",
    "Vitamina B12": "0",
    "Vitamina C": "16.8",
    "Vitamina A": "6.7",
    "Vitamina D": "0",
    "Vitamina E": "0.3"
},
{
    "Comida": "Miel", # En 30 gramos
    "Kilocalorías": "94",
    "Proteínas": "0.2",
    "Grasa total": "0",
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "23.4",
    "Fibra": "0",
    "Calcio": "1.5",
    "Hierro": "0.1",
    "Yodo": "0", # Desconocido
    "Magnesio": "0.6",
    "Zinc": "0.3",
    "Sodio": "3.3",
    "Potasio": "15.3",
    "Fósforo": "5.1",
    "Selenio": "0.3",
    "Vitamina B1": "0",
    "Vitamina B2": "0.01",
    "Vitamina B3": "0.1",
    "Vitamina B6": "0",
    "Vitamina B9": "0",
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Naranja", # Por unidad
    "Kilocalorías": "69",
    "Proteínas": "1.3",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "14.1",
    "Fibra": "3.3",
    "Calcio": "59.1",
    "Hierro": "0.5",
    "Yodo": "3.3",
    "Magnesio": "19.7",
    "Zinc": "0.3",
    "Sodio": "4.9",
    "Potasio": "329",
    "Fósforo": "46",
    "Selenio": "1.6",
    "Vitamina B1": "0.16",
    "Vitamina B2": "0.05",
    "Vitamina B3": "0.5",
    "Vitamina B6": "0.10",
    "Vitamina B9": "60.8",
    "Vitamina B12": "0",
    "Vitamina C": "82.1",
    "Vitamina A": "65.7",
    "Vitamina D": "0",
    "Vitamina E": "0.3"
},
{
    "Comida": "Nueces", # En 25 gramos
    "Kilocalorías": "153",
    "Proteínas": "3.5",
    "Grasa total": "14.8",
    "Grasa saturada": "1.60",
    "Grasa insaturada": "12.36",
    "Carbohidratos": "0.8",
    "Fibra": "1.3",
    "Calcio": "19.3",
    "Hierro": "0.6",
    "Yodo": "2.3",
    "Magnesio": "35",
    "Zinc": "0.5",
    "Sodio": "0.8",
    "Potasio": "172.5",
    "Fósforo": "76",
    "Selenio": "4.8",
    "Vitamina B1": "0.08",
    "Vitamina B2": "0.03",
    "Vitamina B3": "0.9",
    "Vitamina B6": "0.18",
    "Vitamina B9": "16.5",
    "Vitamina B12": "0",
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0.2"
},
{
    "Comida": "Palta", # Por unidad
    "Kilocalorías": "200",
    "Proteínas": "2.1",
    "Grasa total": "17",
    "Grasa saturada": "2",
    "Grasa insaturada": "14.27",
    "Carbohidratos": "8.4",
    "Fibra": "2.6",
    "Calcio": "22.7",
    "Hierro": "1",
    "Yodo": "2.8",
    "Magnesio": "58.2",
    "Zinc": "0.4",
    "Sodio": "2.8",
    "Potasio": "568",
    "Fósforo": "39.8",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.13",
    "Vitamina B2": "0.17",
    "Vitamina B3": "2.1",
    "Vitamina B6": "0.60",
    "Vitamina B9": "15.6",
    "Vitamina B12": "0",
    "Vitamina C": "24.1",
    "Vitamina A": "35.5",
    "Vitamina D": "0",
    "Vitamina E": "4.5"
},
{
    "Comida": "Papa", # Por unidad
    "Kilocalorías": "135",
    "Proteínas": "3.8",
    "Grasa total": "0.3",
    "Grasa saturada": "0.06",
    "Grasa insaturada": "0.20",
    "Carbohidratos": "27.5",
    "Fibra": "3.1",
    "Calcio": "13.8",
    "Hierro": "0.9",
    "Yodo": "4.6",
    "Magnesio": "38.3",
    "Zinc": "0.5",
    "Sodio": "10.7",
    "Potasio": "872",
    "Fósforo": "76.5",
    "Selenio": "1.5",
    "Vitamina B1": "0.15",
    "Vitamina B2": "0.06",
    "Vitamina B3": "2.3",
    "Vitamina B6": "0.38",
    "Vitamina B9": "18.4",
    "Vitamina B12": "0",
    "Vitamina C": "27.5",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0.2"
},
{
    "Comida": "Pera", # Por unidad
    "Kilocalorías": "82",
    "Proteínas": "0.7",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0",
    "Grasa insaturada": "0",
    "Carbohidratos": "17.7",
    "Fibra": "3.8",
    "Calcio": "20.1",
    "Hierro": "0.3",
    "Yodo": "3.3",
    "Magnesio": "11.7",
    "Zinc": "0.2",
    "Sodio": "3.3",
    "Potasio": "217",
    "Fósforo": "29.3",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.05",
    "Vitamina B2": "0.05",
    "Vitamina B3": "0.3",
    "Vitamina B6": "0.03",
    "Vitamina B9": "18.4",
    "Vitamina B12": "0",
    "Vitamina C": "5",
    "Vitamina A": "16.7",
    "Vitamina D": "0",
    "Vitamina E": "0" # Desconocido
},
{
    "Comida": "Queso", # Referencia de queso rallado Tregar | 40 gramos
    "Kilocalorías": "44",
    "Proteínas": "3.6",
    "Grasa total": "2.9",
    "Grasa saturada": "1.9",
    "Grasa insaturada": "0", # Desconocido
    "Carbohidratos": "0.9",
    "Fibra": "0",
    "Calcio": "119",
    "Hierro": "0", # Desconocido
    "Yodo": "0", # Desconocido
    "Magnesio": "0", # Desconocido
    "Zinc": "0", # Desconocido
    "Sodio": "108",
    "Potasio": "0", # Desconocido
    "Fósforo": "65",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0", # Desconocido
    "Vitamina B3": "0", # Desconocido
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0", # Desconocido
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "20",
    "Vitamina D": "0", # Desconocido
    "Vitamina E": "0", # Desconocido
},
{
    "Comida": "Soja", # En 50 gramos
    "Kilocalorías": "203",
    "Proteínas": "17.4",
    "Grasa total": "9.3",
    "Grasa saturada": "1.1",
    "Grasa insaturada": "6.3",
    "Carbohidratos": "7.9",
    "Fibra": "7.8",
    "Calcio": "120",
    "Hierro": "4.8",
    "Yodo": "3",
    "Magnesio": "125",
    "Zinc": "2.1",
    "Sodio": "2.5",
    "Potasio": "865",
    "Fósforo": "330",
    "Selenio": "7",
    "Vitamina B1": "0.30",
    "Vitamina B2": "0.13",
    "Vitamina B3": "3.8",
    "Vitamina B6": "0.19",
    "Vitamina B9": "185",
    "Vitamina B12": "0",
    "Vitamina C": "0", # Desconocido
    "Vitamina A": "1",
    "Vitamina D": "0",
    "Vitamina E": "1.4"
},
{
    "Comida": "Té",
    "Kilocalorías": "0",
    "Proteínas": "0.1",
    "Grasa total": "0", # Desconocido
    "Grasa saturada": "0", # Desconocido
    "Grasa insaturada": "0", # Desconocido
    "Carbohidratos": "0",
    "Fibra": "0",
    "Calcio": "0", # Desconocido
    "Hierro": "0", # Desconocido
    "Yodo": "0", # Desconocido
    "Magnesio": "1",
    "Zinc": "0", # Desconocido
    "Sodio": "0", # Desconocido
    "Potasio": "17",
    "Fósforo": "1",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0", # Desconocido
    "Vitamina B2": "0.01",
    "Vitamina B3": "0.1",
    "Vitamina B6": "0", # Desconocido
    "Vitamina B9": "0", # Desconocido
    "Vitamina B12": "0",
    "Vitamina C": "0",
    "Vitamina A": "0",
    "Vitamina D": "0",
    "Vitamina E": "0"
},
{
    "Comida": "Tomate", # Por unidad
    "Kilocalorías": "31",
    "Proteínas": "1.4",
    "Grasa total": "0.2",
    "Grasa saturada": "0",
    "Grasa insaturada": "0.16", # Grasas monoinsaturadas desconocidas
    "Carbohidratos": "4.9",
    "Fibra": "2",
    "Calcio": "15.5",
    "Hierro": "0.8",
    "Yodo": "9.9",
    "Magnesio": "14.1",
    "Zinc": "0.3",
    "Sodio": "4.2",
    "Potasio": "409",
    "Fósforo": "38.1",
    "Selenio": "0", # Desconocido
    "Vitamina B1": "0.08",
    "Vitamina B2": "0.06",
    "Vitamina B3": "1.1",
    "Vitamina B6": "0.16",
    "Vitamina B9": "39.5",
    "Vitamina B12": "0",
    "Vitamina C": "36.7",
    "Vitamina A": "116",
    "Vitamina D": "0",
    "Vitamina E": "1.7"
},
{
    "Comida": "Zanahoria", # Por unidad
    "Kilocalorías": "27",
    "Proteínas": "0.6",
    "Grasa total": "0.1",
    "Grasa saturada": "0.02",
    "Grasa insaturada": "0.09",
    "Carbohidratos": "4.8",
    "Fibra": "1.9",
    "Calcio": "27.2",
    "Hierro": "0.5",
    "Yodo": "6",
    "Magnesio": "8.6",
    "Zinc": "0.2",
    "Sodio": "51.1",
    "Potasio": "169",
    "Fósforo": "24.6",
    "Selenio": "0.7",
    "Vitamina B1": "0.03",
    "Vitamina B2": "0.03",
    "Vitamina B3": "0.4",
    "Vitamina B6": "0.10",
    "Vitamina B9": "6.6",
    "Vitamina B12": "0",
    "Vitamina C": "4",
    "Vitamina A": "894",
    "Vitamina D": "0",
    "Vitamina E": "0.3"
},
]


total = []

while True:
    try:
        inpt = input("¿Qué vas a comer hoy?\n").capitalize()

        if inpt == "N":
            print()
            break

        for c in comida:
            if inpt == c["Comida"]:
                total.append(c)
                break

        if inpt != c["Comida"]:
            print(f"¿Qué? ¿Qué significa {inpt}? ¿De qué me estás hablando? ¿Es esta línea lo suficientemente larga ya?")

    except EOFError:
        break


totales = {
    "Kilocalorías": 0.0,
    "Proteínas": 0.0,
    "Grasa total": 0.0,
    "Grasa saturada": 0.0,
    "Grasa insaturada": 0.0,
    "Carbohidratos": 0.0,
    "Fibra": 0.0,
    "Calcio": 0.0,
    "Hierro": 0.0,
    "Yodo": 0.0,
    "Magnesio": 0.0,
    "Zinc": 0.0,
    "Sodio": 0.0,
    "Potasio": 0.0,
    "Fósforo": 0.0,
    "Selenio": 0.0,
    "Vitamina B1": 0.0,
    "Vitamina B2": 0.0,
    "Vitamina B3": 0.0,
    "Vitamina B6": 0.0,
    "Vitamina B9": 0.0,
    "Vitamina B12": 0.0,
    "Vitamina C": 0.0,
    "Vitamina A": 0.0,
    "Vitamina D": 0.0,
    "Vitamina E": 0.0
}


for t in total:
    totales["Kilocalorías"] += float(t["Kilocalorías"])
    totales["Proteínas"] += float(t["Proteínas"])
    totales["Grasa total"] += float(t["Grasa total"])
    totales["Grasa saturada"] += float(t["Grasa saturada"])
    totales["Grasa insaturada"] += float(t["Grasa insaturada"])
    totales["Carbohidratos"] += float(t["Carbohidratos"])
    totales["Fibra"] += float(t["Fibra"])
    totales["Calcio"] += float(t["Calcio"])
    totales["Hierro"] += float(t["Hierro"])
    totales["Yodo"] += float(t["Yodo"])
    totales["Magnesio"] += float(t["Magnesio"])
    totales["Zinc"] += float(t["Zinc"])
    totales["Sodio"] += float(t["Sodio"])
    totales["Potasio"] += float(t["Potasio"])
    totales["Fósforo"] += float(t["Fósforo"])
    totales["Selenio"] += float(t["Selenio"])
    totales["Vitamina B1"] += float(t["Vitamina B1"])
    totales["Vitamina B2"] += float(t["Vitamina B2"])
    totales["Vitamina B3"] += float(t["Vitamina B3"])
    totales["Vitamina B6"] += float(t["Vitamina B6"])
    totales["Vitamina B9"] += float(t["Vitamina B9"])
    totales["Vitamina B12"] += float(t["Vitamina B12"])
    totales["Vitamina C"] += float(t["Vitamina C"])
    totales["Vitamina A"] += float(t["Vitamina A"])
    totales["Vitamina D"] += float(t["Vitamina D"])
    totales["Vitamina E"] += float(t["Vitamina E"])


print(f"{totales['Kilocalorías']:.0f} kilocalorías                    -- Objetivo diario de 3000")
print(f"{totales['Proteínas']:.0f} gramos de proteínas              -- Objetivo diario de ~130 gramos")
print(f"{totales['Grasa total']:.0f} gramos de grasa total            -- Objetivo diario de 100-117 gramos")
print(f"{totales['Grasa saturada']:.0f} gramos de grasa saturada          -- Objetivo diario de 23-27 gramos")
print(f"{totales['Grasa insaturada']:.0f} gramos de grasa insaturada        -- Objetivo diario de 84 gramos")
print(f"{totales['Carbohidratos']:.0f} gramos de carbohidratos          -- Objetivo diario de ~455 gramos")
print(f"{totales['Fibra']:.0f} gramos de fibra                   -- Objetivo diario de ~35 gramos")
print(f"{totales['Calcio']:.0f} miligramos de calcio            -- Objetivo diario de 1000 miligramos")
print(f"{totales['Hierro']:.0f} miligramos de hierro              -- Objetivo diario de 10 miligramos")
print(f"{totales['Yodo']:.0f} microgramos de yodo              -- Objetivo diario de 140 microgramos")
print(f"{totales['Magnesio']:.0f} miligramos de magnesio           -- Objetivo diario de 350 miligramos")
print(f"{totales['Zinc']:.0f} miligramos de zinc                -- Objetivo diario de 15 miligramos")
print(f"{totales['Sodio']:.0f} miligramos de sodio             -- Objetivo diario de <2000 miligramos")
print(f"{totales['Potasio']:.0f} miligramos de potasio           -- Objetivo diario de 3500 miligramos")
print(f"{totales['Fósforo']:.0f} miligramos de fósforo           -- Objetivo diario de 700 miligramos")
print(f"{totales['Selenio']:.0f} microgramos de selenio           -- Objetivo diario de 70 microgramos")
print(f"{totales['Vitamina B1']:.1f} miligramos de vitamina B1        -- Objetivo diario de 1,2 miligramos")
print(f"{totales['Vitamina B2']:.1f} miligramos de vitamina B2        -- Objetivo diario de 1,8 miligramos")
print(f"{totales['Vitamina B3']:.0f} miligramos de vitamina B3         -- Objetivo diario de 20 miligramos")
print(f"{totales['Vitamina B6']:.1f} miligramos de vitamina B6        -- Objetivo diario de 1,8 miligramos")
print(f"{totales['Vitamina B9']:.0f} microgramos de vitamina B9       -- Objetivo diario de 400 microgramos")
print(f"{totales['Vitamina B12']:.0f} microgramos de vitamina B12        -- Objetivo diario de 2 microgramos")
print(f"{totales['Vitamina C']:.0f} miligramos de vitamina C         -- Objetivo diario de 60 miligramos")
print(f"{totales['Vitamina A']:.0f} microgramos de vitamina A       -- Objetivo diario de 1000 microgramos")
print(f"{totales['Vitamina D']:.0f} microgramos de vitamina D          -- Objetivo diario de 15 microgramos")
print(f"{totales['Vitamina E']:.0f} miligramos de vitamina E           -- Objetivo diario de 12 miligramos")
