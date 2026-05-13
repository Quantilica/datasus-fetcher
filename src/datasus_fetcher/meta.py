"""Metadata of DATASUS' datasets."""

# Brazil UFs
states = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    "BR",
]

uf_pattern = "{}".format("|".join(states).lower())
month_pattern = "|".join(f"{i:02}" for i in range(1, 12 + 1))
year_4digit_pattern = r"\d{4}"  # 1997
year_2digit_pattern = r"\d{2}"  # 97

# 9701, 9702, ... 9712, 9801, ...
year_pattern = rf"({year_4digit_pattern})"
year2_pattern = rf"({year_2digit_pattern})"
uf_year_pattern = rf"({uf_pattern})({year_4digit_pattern})"
uf_year2_pattern = rf"({uf_pattern})({year_2digit_pattern})"
uf_year2_month_pattern = (
    rf"({uf_pattern})({year_2digit_pattern})({month_pattern})"
)
uf_year2_month_pattern_sia_pa = uf_year2_month_pattern + r"(|[a-z])"
uf_mapas_year_pattern = rf"({uf_pattern})_mapas_({year_4digit_pattern})"
uf_cnv_pattern = rf"({uf_pattern})_cnv"

BASE_PATH = "/dissemin/publicos"

datasets = {
    "sih-rd": {
        "name": "RD - AIH Reduzida",
        "group": "sih",
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/199201_200712/Dados",
                "filename_prefix": "RD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "RD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sih-rj": {
        "name": "RJ - AIH Rejeitadas",
        "group": "sih",
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "RJ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sih-sp": {
        "name": "SP - Serviços Profissionais",
        "group": "sih",
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/199201_200712/Dados",
                "filename_prefix": "SP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "SP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sih-er": {
        "name": "ER - AIH Rejeitadas com código de erro",
        "group": "sih",
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "ER",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sinasc-dn": {
        "name": "Declarações de nascidos vivos",
        "group": "sinasc",
        "periods": [
            {
                "dir": BASE_PATH + "/SINASC/1994_1995/Dados/DNRES",
                "filename_prefix": "DNR",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINASC/1996_/Dados/DNRES",
                "filename_prefix": "DN",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINASC/PRELIM/DNRES",
                "filename_prefix": "DN",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinasc-dnex": {
        "name": "Declarações de nascidos vivos no exterior",
        "group": "sinasc",
        "periods": [
            {
                "dir": BASE_PATH + "/SINASC/1996_/Dados/DNRES",
                "filename_prefix": "DNEX",
                "filename_pattern": year_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-do-cid09": {
        "name": "Declarações de Óbito CID-9",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DORES",
                "filename_prefix": "DOR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "year"],
    },
    "sim-do-cid10": {
        "name": "Declarações de Óbito CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DORES",
                "filename_prefix": "DO",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DORES",
                "filename_prefix": "DO",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sim-doext-cid09": {
        "name": "Declarações de Óbito Externas CID-9",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOEXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-doext-cid10": {
        "name": "Declarações de Óbito Externas CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOEXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-dofet-cid09": {
        "name": "Declarações de Óbito Fetais CID-9",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOFET",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-dofet-cid10": {
        "name": "Declarações de Óbito Fetais CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOFET",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-doinf-cid09": {
        "name": "Declarações de Óbito Infantis CID-9",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOINF",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-doinf-cid10": {
        "name": "Declarações de Óbito Infantis CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOINF",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-domat-cid10": {
        "name": "Declarações de Óbitos Maternos CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOMAT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "sim-dorext-cid10": {
        "name": "Mortalidade de Residentes no Exterior CID-10",
        "group": "sim",
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOREXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["year"],
    },
    "cnes-dc": {
        "name": "Dados Complementares",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/DC",
                "filename_prefix": "DC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-ee": {
        "name": "Estabelecimento de Ensino",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EE",
                "filename_prefix": "EE",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-ef": {
        "name": "Estabelecimento Filantrópico",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EF",
                "filename_prefix": "EF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-ep": {
        "name": "Equipes",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EP",
                "filename_prefix": "EP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-eq": {
        "name": "Equipamentos",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EQ",
                "filename_prefix": "EQ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-gm": {
        "name": "Gestão e Metas",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/GM",
                "filename_prefix": "GM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-hb": {
        "name": "Habilitação",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/HB",
                "filename_prefix": "HB",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-in": {
        "name": "Incentivos",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/IN",
                "filename_prefix": "IN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-lt": {
        "name": "Leitos",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/LT",
                "filename_prefix": "LT",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-pf": {
        "name": "Profissional",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/PF",
                "filename_prefix": "PF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-rc": {
        "name": "Regra Contratual",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/RC",
                "filename_prefix": "RC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-sr": {
        "name": "Serviço Especializado",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/SR",
                "filename_prefix": "SR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cnes-st": {
        "name": "Estabelecimentos",
        "group": "cnes",
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/ST",
                "filename_prefix": "ST",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-ab": {
        "name": "APAC de Acompanhamento a Cirurgia Bariátrica",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AB",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-abo": {
        "name": "APAC Acompanhamento Pós Cirurgia Bariátrica",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ABO",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-acf": {
        "name": "APAC Confeção de Fístula Arteriovenosa",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ACF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-ad": {
        "name": "APAC de Laudos Diversos",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-am": {
        "name": "APAC de Medicamentos",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-an": {
        "name": "APAC de Nefrologia",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-aq": {
        "name": "APAC de Quimioterapia",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AQ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-ar": {
        "name": "APAC de Radioterapia",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-atd": {
        "name": "APAC de Tratamento Dialítico",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ATD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-pa": {
        "name": "Produção Ambulatorial",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/199407_200712/Dados",
                "filename_prefix": "PA",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "PA",
                "filename_pattern": uf_year2_month_pattern_sia_pa,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-ps": {
        "name": "Psicossocial",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "PS",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sia-sad": {
        "name": "Atenção Domiciliar",
        "group": "sia",
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "SAD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "cih-cr": {
        "name": "Comunicação de Internação Hospitalar",
        "group": "cih",
        "periods": [
            {
                "dir": BASE_PATH + "/CIH/200801_201012/Dados",
                "filename_prefix": "CR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "ciha": {
        "name": "Sistema de Comunicação de Informação Hospitalar e Ambulatorial",
        "group": "ciha",
        "periods": [
            {
                "dir": BASE_PATH + "/CIHA/201101_/Dados",
                "filename_prefix": "CIHA",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "resp": {
        "name": "Notificações de casos suspeitos de SCZ",
        "group": "resp",
        "periods": [
            {
                "dir": BASE_PATH + "/RESP/DADOS",
                "filename_prefix": "RESP",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "year"],
    },
    "sisprenatal-pn": {
        "name": "Pré-Natal",
        "group": "sisprenatal",
        "periods": [
            {
                "dir": BASE_PATH + "/SISPRENATAL/201201_/Dados",
                "filename_prefix": "PN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sinan-acbi": {
        "name": "Acidente de trabalho com material biológico",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ACBI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ACBI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-acgr": {
        "name": "Acidente de trabalho",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ACGR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ACGR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-anim": {
        "name": "Acidente por Animais Peçonhentos",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ANIM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ANIM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-antr": {
        "name": "Atendimento Antirrábico",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ANTR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ANTR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-botu": {
        "name": "Botulismo",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "BOTU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "BOTU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-canc": {
        "name": "Câncer relacionado ao trabalho",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CANC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CANC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-chag": {
        "name": "Doença de Chagas Aguda",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CHAG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CHAG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-chik": {
        "name": "Febre de Chikungunya",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CHIK",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CHIK",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-cole": {
        "name": "Cólera",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "COLE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "COLE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-coqu": {
        "name": "Coqueluche",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "COQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "COQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-deng": {
        "name": "Dengue",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DENG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DENG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-derm": {
        "name": "Dermatoses ocupacionais",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DERM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DERM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-dift": {
        "name": "Difteria",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DIFT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DIFT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-esqu": {
        "name": "Esquistossomose",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ESQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ESQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-fmac": {
        "name": "Febre Maculosa",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "FMAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "FMAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-ftif": {
        "name": "Febre Tifoide",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "FTIF",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "FTIF",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hans": {
        "name": "Hanseníase",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HANS",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HANS",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hant": {
        "name": "Hantavirose",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HANT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HANT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hepa": {
        "name": "Hepatites Virais",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HEPA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HEPA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-iexo": {
        "name": "Intoxicação Exógena",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-leiv": {
        "name": "Leishmaniose Visceral",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LEIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LEIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-lept": {
        "name": "Leptospirose",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LEPT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LEPT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-lerd": {
        "name": "LER/Dort",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LERD",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LERD",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-ltan": {
        "name": "Leishmaniose Tegumentar Americana",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LTAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LTAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-mala": {
        "name": "Malária",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MALA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MALA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-meni": {
        "name": "Meningite",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MENI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MENI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-ment": {
        "name": "Transtornos mentais relacionados ao trabalho",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MENT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MENT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-pair": {
        "name": "Perda auditiva por ruído relacionado ao trabalho",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PAIR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PAIR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-pest": {
        "name": "Peste",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PEST",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PEST",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-pfan": {
        "name": "Paralisia Flácida Aguda",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PFAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PFAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-pneu": {
        "name": "Pneumoconioses relacionadas ao trabalho",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PNEU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PNEU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-raiv": {
        "name": "Raiva",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "RAIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "RAIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-sifa": {
        "name": "Sífilis Adquirida",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-sifc": {
        "name": "Sífilis Congênita",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-sifg": {
        "name": "Sífilis em Gestante",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-teta": {
        "name": "Tétano Acidental",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TETA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TETA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-tetn": {
        "name": "Tétano Neonatal",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TETN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TETN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-tube": {
        "name": "Tuberculose",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TUBE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TUBE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-viol": {
        "name": "Violência doméstica, sexual e/ou outras violências",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "VIOL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "VIOL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-zika": {
        "name": "Zika Vírus",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ZIKA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ZIKA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "base-populacional-ibge-pop": {
        "name": "POP - Censo e Estimativas",
        "group": "base-populacional-ibge",
        "periods": [
            {
                "dir": BASE_PATH + "/IBGE/POP",
                "filename_prefix": "POP",
                "filename_pattern": uf_year2_pattern,
                "extension": "zip",
            },
        ],
        "partition": ["uf", "year"],
    },
    "base-populacional-ibge-pops": {
        "name": "POPS - Estimativas por Sexo e Idade",
        "group": "base-populacional-ibge",
        "periods": [
            {
                "dir": BASE_PATH + "/IBGE/POPSVS",
                "filename_prefix": "POPS",
                "filename_pattern": uf_year2_pattern,
                "extension": "zip",
            },
        ],
        "partition": ["uf", "year"],
    },
    "base-populacional-ibge-popt": {
        "name": "POPT - Estimativas TCU",
        "group": "base-populacional-ibge",
        "periods": [
            {
                "dir": BASE_PATH + "/IBGE/POPTCU",
                "filename_prefix": "POPT",
                "filename_pattern": uf_year2_pattern,
                "extension": "zip",
            },
        ],
        "partition": ["uf", "year"],
    },
    "base-territorial-mapas": {
        "name": "Base Territorial - Mapas",
        "group": "base-territorial",
        "periods": [
            {
                "dir": "/territorio/mapas",
                "filename_prefix": "",
                "filename_pattern": uf_mapas_year_pattern,
                "extension": "zip",
            },
        ],
        "partition": ["uf", "year"],
    },
    "base-territorial": {
        "name": "Base Territorial",
        "group": "base-territorial",
        "periods": [
            {
                "dir": "/territorio/tabelas",
                "filename_prefix": "",
                "filename_pattern": "",
                "extension": "zip",
            },
        ],
        "partition": [],
    },
    "base-territorial-conversao": {
        "name": "Base Territorial - Conversão",
        "group": "base-territorial",
        "periods": [
            {
                "dir": "/territorio/conversoes",
                "filename_prefix": "",
                "filename_pattern": uf_cnv_pattern,
                "extension": "zip",
            },
        ],
        "partition": ["uf"],
    },
    "pce": {
        "name": "Programa de Controle da Esquistossomose",
        "group": "pce",
        "periods": [
            {
                "dir": BASE_PATH + "/PCE/DADOS",
                "filename_prefix": "PCE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            }
        ],
        "partition": ["uf", "year"],
    },
    "po": {
        "name": "Painel de Oncologia",
        "group": "po",
        "periods": [
            {
                "dir": BASE_PATH + "/PAINEL_ONCOLOGIA/DADOS",
                "filename_prefix": "PO",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            }
        ],
        "partition": ["uf", "year"],
    },
    "siscolo-cc": {
        "name": "Citopatológico de Colo de Útero",
        "group": "siscolo",
        "periods": [
            {
                "dir": BASE_PATH + "/SISCAN/SISCOLO4/Dados",
                "filename_prefix": "CC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            }
        ],
        "partition": ["uf", "yearmonth"],
    },
    "siscolo-hc": {
        "name": "Histopatológico de Colo de Útero",
        "group": "siscolo",
        "periods": [
            {
                "dir": BASE_PATH + "/SISCAN/SISCOLO4/Dados",
                "filename_prefix": "HC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sismama-cm": {
        "name": "Citopatológico de Mama",
        "group": "sismama",
        "periods": [
            {
                "dir": BASE_PATH + "/SISCAN/SISMAMA/Dados",
                "filename_prefix": "CM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sismama-hm": {
        "name": "Histopatológico de Mama",
        "group": "sismama",
        "periods": [
            {
                "dir": BASE_PATH + "/SISCAN/SISMAMA/Dados",
                "filename_prefix": "HM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": ["uf", "yearmonth"],
    },
    "sinan-exan": {
        "name": "Doenças exantemáticas",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "EXAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "EXAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-ntra": {
        "name": "Notificação de Tracoma",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "NTRA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "NTRA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-sdta": {
        "name": "Surto Doenças Transmitidas por Alimentos",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SDTA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SDTA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-src": {
        "name": "Síndrome da Rubéola Congênita",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SRC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SRC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-toxc": {
        "name": "Toxoplasmose Congênita",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TOXC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TOXC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-toxg": {
        "name": "Toxoplasmose Gestacional",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TOXG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TOXG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-trac": {
        "name": "Inquérito de Tracoma",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TRAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TRAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-varc": {
        "name": "Varicela",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "VARC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "VARC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-aida": {
        "name": "AIDS em adultos",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "AIDA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "AIDA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-aidc": {
        "name": "AIDS em crianças",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "AIDC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "AIDC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-espo": {
        "name": "Esporotricose (Epizootia)",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ESPO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ESPO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hiva": {
        "name": "HIV em adultos",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HIVA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HIVA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hivc": {
        "name": "HIV em crianças",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HIVC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HIVC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hive": {
        "name": "HIV em crianças expostas",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HIVE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HIVE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-hivg": {
        "name": "HIV em gestante",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HIVG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HIVG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
    "sinan-rota": {
        "name": "Rotavírus",
        "group": "sinan",
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ROTA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ROTA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
                "preliminary": True,
            },
        ],
        "partition": ["uf", "year"],
    },
}


docs = {
    "base-populacional-ibge": {
        "dir": [BASE_PATH + "/IBGE/DOC"],
    },
    "base-territorial": {
        "dir": ["/territorio/doc"],
    },
    "cmd": {
        "dir": [BASE_PATH + "/CMD/201701_/doc"],
    },
    "ciha": {
        "dir": [BASE_PATH + "/CIHA/201101_/Doc"],
    },
    "cnes": {
        "dir": [BASE_PATH + "/CNES/200508_/doc"],
    },
    "pce": {
        "dir": [BASE_PATH + "/PCE/DOCS/"],
    },
    "po": {
        "dir": [BASE_PATH + "/PAINEL_ONCOLOGIA/DOC"],
    },
    "resp": {
        "dir": [BASE_PATH + "/RESP/DOCS"],
    },
    "sia": {
        "dir": [BASE_PATH + "/SIASUS/200801_/Doc"],
    },
    "sih": {
        "dir": [BASE_PATH + "/SIHSUS/200801_/Doc"],
    },
    "sim": {
        "dir": [
            BASE_PATH + "/SIM/CID9/DOCS",
            BASE_PATH + "/SIM/CID10/DOCS",
        ],
    },
    "sinan": {
        "dir": [BASE_PATH + "/SINAN/DOCS"],
    },
    "sinasc": {
        "dir": [
            BASE_PATH + "/SINASC/ANT/DOCS",
            BASE_PATH + "/SINASC/NOV/DOCS",
        ],
    },
}


auxiliary_tables = {
    "base-populacional-ibge": {
        "dir": [BASE_PATH + "/IBGE/Auxiliar"],
    },
    "cih": {
        "dir": [BASE_PATH + "/CIH/200801_201012/Auxiliar"],
    },
    "ciha": {
        "dir": [BASE_PATH + "/CIHA/201101_/Auxiliar"],
    },
    "cmd": {
        "dir": [BASE_PATH + "/CMD/201701_/Auxiliar"],
    },
    "cnes": {
        "dir": [BASE_PATH + "/CNES/200508_/Auxiliar"],
    },
    "pce": {
        "dir": [BASE_PATH + "/PCE/AUXILIAR"],
    },
    "po": {
        "dir": [BASE_PATH + "/PAINEL_ONCOLOGIA/AUXILIAR"],
    },
    "resp": {
        "dir": [BASE_PATH + "/RESP/AUXILIAR"],
    },
    "sia": {
        "dir": [BASE_PATH + "/SIASUS/200801_/Auxiliar"],
    },
    "sih": {
        "dir": [BASE_PATH + "/SIHSUS/200801_/Auxiliar"],
    },
    "sim": {
        "dir": [
            BASE_PATH + "/SIM/CID9/TAB",
            BASE_PATH + "/SIM/CID10/TAB",
        ],
    },
    "sinan": {
        "dir": [BASE_PATH + "/SINAN/AUXILIAR"],
    },
    "sinasc": {
        "dir": [
            BASE_PATH + "/SINASC/1994_1995/Auxiliar",
            BASE_PATH + "/SINASC/1996_/Auxiliar",
        ],
    },
    "siscolo": {
        "dir": [BASE_PATH + "/SISCAN/SISCOLO4/Auxiliar"],
    },
    "sismama": {
        "dir": [BASE_PATH + "/SISCAN/SISMAMA/Auxiliar"],
    },
    "sisprenatal": {
        "dir": [BASE_PATH + "/SISPRENATAL/201201_/Auxiliar"],
    },
}


datasets_groups = {
    "base-populacional-ibge": {
        "name": "Base Populacional - IBGE",
    },
    "base-territorial": {
        "name": "Base Territorial",
    },
    "cih": {
        "name": "CIH: Sistema de Comunicação de Informação Hospitalar",
    },
    "ciha": {
        "name": "CIHA: Sistema de Comunicação de Informação Hospitalar e Ambulatorial",
    },
    "cnes": {
        "name": "CNES: Cadastro Nacional de Estabelecimentos de Saúde",
    },
    "pce": {
        "name": "PCE: Programa de Controle da Esquistossomose",
    },
    "po": {
        "name": "PO: Painel de Oncologia",
    },
    "resp": {
        "name": "RESP: Notificações de casos suspeitos de SCZ",
    },
    "sia": {
        "name": "SIA: Sistema de Informações Ambulatoriais",
    },
    "sih": {
        "name": "SIH: Sistema de Informação Hospitalar",
    },
    "sim": {
        "name": "SIM: Sistema de Informação de Mortalidade",
    },
    "sinan": {
        "name": "SINAN: Sistema de Informação de Agravos de Notificação",
    },
    "sinasc": {
        "name": "SINASC: Sistema de Informação de Nascidos Vivos",
    },
    "siscolo": {
        "name": "SISCOLO: Sistema de Informações de Cânceres de Colo de Útero",
    },
    "sismama": {
        "name": "SISMAMA: Sistema de Informações de Cânceres de Mama",
    },
    "sisprenatal": {
        "name": "SISPRENATAL: Sistema de Monitoramento e Avaliação do Pré-Natal, Parto, Puepério e Criança",
    },
}
