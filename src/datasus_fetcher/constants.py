"""Constants and schema definitions for DATASUS microdata processing."""

from __future__ import annotations

# Sentinel values representing missing or null entries in DATASUS DBF files
SENTINEL_NULLS = {
    "",
    " ",
    "  ",
    "   ",
    "NA",
    "null",
    "NULL",
    "None",
    "none",
    "999999",
    "99999999",
    "00000000",
}

# Administrative and classification codes that MUST be preserved as clean
# strings with leading zeros
CODE_COLUMNS = {
    # Municipalities (IBGE 6-digit or 7-digit)
    "MUNIC_RES",
    "MUNIC_MOV",
    "MUNIC_ATEN",
    "MUNIC_NOT",
    "MUNIC_INTER",
    "COD_MUN",
    "CO_MUN_RES",
    "CO_MUN_NOT",
    "CO_MUN_ATEN",
    "CO_MUN_IN",
    "CO_MUN_DEF",
    "CO_MUNIC_R",
    "CO_MUNIC_N",
    "CO_MUNIC_O",
    "CO_MUNIC_S",
    # States and Zip
    "UF",
    "SG_UF",
    "CEP",
    "CEP_RES",
    # Diagnoses and Causes of Death (ICD-10 / CID-10, ICD-9)
    "CID10",
    "DIAG_PRINC",
    "DIAG_SECUN",
    "DIAGSEC1",
    "DIAGSEC2",
    "DIAGSEC3",
    "DIAGSEC4",
    "DIAGSEC5",
    "DIAGSEC6",
    "DIAGSEC7",
    "DIAGSEC8",
    "DIAGSEC9",
    "CID_MORTE",
    "CID_NOTIF",
    "CAUSABAS",
    "CAUSABAS_O",
    "CAUSAEXT",
    "CID",
    # Occupations and Professions (CBO 6-digit)
    "CBO",
    "CBO_MED",
    "CBO_SOLIC",
    "CBO_EXEC",
    "CO_OCUPA",
    "CO_CBO",
    # Facilities and Providers (CNES 7-digit)
    "CNES",
    "CNES_EXEC",
    "COD_ESTAB",
    "CO_UNIDADE",
    # Health Procedures (SUS SIA/SIH 10-digit codes)
    "PROC_REA",
    "PROC_SOLIC",
    "PROCED_REA",
    "PROCED_SOL",
    "PA_PROC_ID",
    "CO_PROCED",
    # Identification numbers
    "N_AIH",
    "NUM_AIH",
    "NUM_NOTIF",
    "NUM_DOC",
    "NUM_SUS",
    "CNS",
    "CNS_PAC",
    # Categorical codes: kept as text, not integers. As integers "01" became 1
    # and, with the lenient cast, letter codes (SEXO "M"/"F" in SINAN) became
    # null without warning. IDADE is left in its source type on purpose: in
    # the SIM it is a text code ("487" = 87 years, the first digit is the
    # unit); in the SIH it is a numeric field with the age.
    "SEXO",
    "RACA_COR",
    "RACACOR",
    "MORTE",
    "OBITO",
    "PARTO",
    "GRAVIDEZ",
    "GESTACAO",
    "ESTCIV",
    "ESC",
    "ESCOL",
}

# Columns containing dates formatted as YYYYMMDD
DATE_COLUMNS = {
    "DT_INTER",
    "DT_SAIDA",
    "DT_NASC",
    "DT_OBITO",
    "DT_NOTIF",
    "DT_SIN_PRI",
    "DT_DIGITA",
    "DT_INVEST",
    "DT_INTERNA",
    "DT_DESL",
    "DT_ENVIO",
    "DT_PROCESS",
    "DT_CAD",
    "DT_ATEND",
    "DT_OCOR",
    "DATA",
    "DT_REG",
}

# The SIM date fields (DTOBITO, DTNASC, DTATESTADO...) are DDMMYYYY text and
# are deliberately left as text: from 1996 to 2005 hundreds of values per year
# are partial (year only, "1996", or month and year, "011996"), and a few are
# not dates ("00101976", "09202003"). Parsing them would turn those into null.

# Columns containing monetary values (SUS reimbursements, hospital expenses)
FLOAT_COLUMNS = {
    "VAL_TOT",
    "VAL_UTI",
    "VAL_SH",
    "VAL_SP",
    "VAL_SADT",
    "VAL_RN",
    "VAL_ACOMP",
    "VAL_ORTP",
    "VAL_SANGUE",
    "VAL_SADT_E",
    "VAL_SH_FED",
    "VAL_SP_FED",
    "VAL_SH_GES",
    "VAL_SP_GES",
    "VAL_UCI",
    "VAL_TOT_U",
    "VAL_LIQ",
    "VAL_BRUT",
    "VAL_BASE",
    "VAL_PROC",
    "VAL_COBR",
    "VAL_APROV",
    "VAL_REAJ",
}

# Columns containing integer counts. QTDFILVIVO and QTDFILMORT (SIM, SINASC)
# are left as text on purpose: "99" means "unknown", not 99 children, and the
# files carry a few non-numeric values ("XX" in SIM 1996 GO, "9." in 2002 SP).
INTEGER_COLUMNS = {
    "DIAS_PERM",
    "QT_DIARIAS",
    "QTDE_PROC",
    "QTD_FILHOS",
    "CONSULTAS",
    "ANO",
    "MES",
}
