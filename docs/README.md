# DATASUS — microdados e tabelas de saúde (`datasus`)

O `datasus-fetcher` baixa do FTP público do DATASUS (`ftp.datasus.gov.br`, Ministério da Saúde) os arquivos dos sistemas de informação do SUS — internações, produção ambulatorial, cadastro de estabelecimentos, mortalidade, nascimentos, agravos de notificação e programas — mais as bases auxiliares de população e de território. O conversor declara **113 datasets**, de **16 sistemas**; este diretório tem uma página por dataset (`datasets/<id>.md`), com o esquema de referência do lake (`datasets/<id>.schema.json`).

## Datasets por sistema

### Base populacional (IBGE) (`base-populacional-ibge`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `base-populacional-ibge-pop` | POP - Censo e Estimativas: a população residente de um município, em um ano, por sexo, situação e faixa etária | 1980 a 2012 | `convertido` | [base-populacional-ibge-pop](datasets/base-populacional-ibge-pop.md) |
| `base-populacional-ibge-pops` | POPS - Estimativas por Sexo e Idade: a população estimada de um município, em um ano, por sexo e idade simples | 2000 a 2025 | `convertido` | [base-populacional-ibge-pops](datasets/base-populacional-ibge-pops.md) |
| `base-populacional-ibge-popt` | POPT - Estimativas TCU: a população total estimada de um município em um ano (estimativas para o TCU) | 1992 a 2025 | `convertido` | [base-populacional-ibge-popt](datasets/base-populacional-ibge-popt.md) |

### Base territorial (`base-territorial`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `base-territorial` | Base Territorial: uma entidade territorial (tabelas `tb_*`) ou um vínculo município–recorte (tabelas `rl_*`) | versões publicadas | `parcial` | [base-territorial](datasets/base-territorial.md) |
| `base-territorial-conversao` | Base Territorial - Conversão: um código de uma categoria de conversão do TabWin (arquivo `.cnv`), por UF | versões publicadas | `convertido` | [base-territorial-conversao](datasets/base-territorial-conversao.md) |
| `base-territorial-mapas` | Base Territorial - Mapas: um mapa digital em formato TabWin (`.MAP`), por UF e ano de referência | 1991 a 2025 | `so-bruto` | [base-territorial-mapas](datasets/base-territorial-mapas.md) |

### CIH — Comunicação de Informação Hospitalar (`cih`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `cih-cr` | Comunicação de Internação Hospitalar: uma internação comunicada (CIH) por um estabelecimento, em uma competência | 2008-01 a 2011-04 | `convertido` | [cih-cr](datasets/cih-cr.md) |

### CIHA — Comunicação de Informação Hospitalar e Ambulatorial (`ciha`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `ciha` | Sistema de Comunicação de Informação Hospitalar e Ambulatorial: um atendimento (internação ou ambulatorial) comunicado por um estabelecimento, em uma competência | 2011-01 a 2026-09 | `convertido` | [ciha](datasets/ciha.md) |

### CNES — Cadastro Nacional de Estabelecimentos de Saúde (`cnes`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `cnes-dc` | Dados Complementares: um estabelecimento de saúde (dados complementares), em uma competência | 2005-08 a 2026-09 | `convertido` | [cnes-dc](datasets/cnes-dc.md) |
| `cnes-ee` | Estabelecimento de Ensino: um registro de ensino/pesquisa de um estabelecimento, em uma competência | 2007-03 a 2021-07 | `convertido` | [cnes-ee](datasets/cnes-ee.md) |
| `cnes-ef` | Estabelecimento Filantrópico: um registro de filantropia de um estabelecimento, em uma competência | 2007-03 a 2026-09 | `convertido` | [cnes-ef](datasets/cnes-ef.md) |
| `cnes-ep` | Equipes: uma equipe de saúde vinculada a um estabelecimento, em uma competência | 2007-04 a 2026-09 | `convertido` | [cnes-ep](datasets/cnes-ep.md) |
| `cnes-eq` | Equipamentos: um tipo de equipamento de um estabelecimento, em uma competência | 2005-08 a 2026-09 | `convertido` | [cnes-eq](datasets/cnes-eq.md) |
| `cnes-gm` | Gestão e Metas: um grupo de gestão e metas de um estabelecimento, em uma competência | 2007-03 a 2026-09 | `convertido` | [cnes-gm](datasets/cnes-gm.md) |
| `cnes-hb` | Habilitação: uma habilitação concedida a um estabelecimento, em uma competência | 2007-03 a 2026-09 | `convertido` | [cnes-hb](datasets/cnes-hb.md) |
| `cnes-in` | Incentivos: um incentivo vinculado a um estabelecimento, em uma competência | 2007-10 a 2026-09 | `convertido` | [cnes-in](datasets/cnes-in.md) |
| `cnes-lt` | Leitos: um conjunto de leitos de um tipo e especialidade em um estabelecimento, em uma competência | 2005-10 a 2026-09 | `convertido` | [cnes-lt](datasets/cnes-lt.md) |
| `cnes-pf` | Profissional: um vínculo profissional–estabelecimento–ocupação (CBO), em uma competência | 2005-08 a 2026-09 | `convertido` | [cnes-pf](datasets/cnes-pf.md) |
| `cnes-rc` | Regra Contratual: uma regra contratual de um estabelecimento, em uma competência | 2007-03 a 2026-09 | `convertido` | [cnes-rc](datasets/cnes-rc.md) |
| `cnes-sr` | Serviço Especializado: um serviço especializado e sua classificação em um estabelecimento, em uma competência | 2005-08 a 2026-09 | `convertido` | [cnes-sr](datasets/cnes-sr.md) |
| `cnes-st` | Estabelecimentos: um estabelecimento de saúde, em uma competência | 2005-08 a 2026-09 | `convertido` | [cnes-st](datasets/cnes-st.md) |

### PCE — Programa de Controle da Esquistossomose (`pce`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `pce` | Programa de Controle da Esquistossomose: a produção de uma localidade em uma competência (contagens de exames e atividades do programa) | 1995 a 2026 | `convertido` | [pce](datasets/pce.md) |

### Painel de Oncologia (`po`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `po` | Painel de Oncologia: um caso com procedimento diagnóstico ou terapêutico de câncer registrado | 2013 a 2026 | `convertido` | [po](datasets/po.md) |

### RESP — Registro de Eventos em Saúde Pública (Zika) (`resp`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `resp` | Notificações de casos suspeitos de SCZ: uma notificação individual de caso suspeito de Síndrome Congênita associada ao vírus Zika | 2015 a 2024 | `convertido` | [resp](datasets/resp.md) |

### SIA — Sistema de Informações Ambulatoriais (`sia`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sia-ab` | APAC de Acompanhamento a Cirurgia Bariátrica: uma APAC de acompanhamento a cirurgia bariátrica, por competência | 2008-01 a 2025-07 | `convertido` | [sia-ab](datasets/sia-ab.md) |
| `sia-abo` | APAC Acompanhamento Pós Cirurgia Bariátrica: uma APAC de acompanhamento pós-cirurgia bariátrica, por competência | 2014-01 a 2026-08 | `convertido` | [sia-abo](datasets/sia-abo.md) |
| `sia-acf` | APAC Confeção de Fístula Arteriovenosa: uma APAC de confecção de fístula arteriovenosa | 2014-08 a 2026-08 | `convertido` | [sia-acf](datasets/sia-acf.md) |
| `sia-ad` | APAC de Laudos Diversos: uma APAC de laudos diversos, por competência | 2008-01 a 2026-08 | `convertido` | [sia-ad](datasets/sia-ad.md) |
| `sia-am` | APAC de Medicamentos: uma APAC de medicamentos (dispensação de um medicamento), por competência | 2008-01 a 2026-08 | `convertido` | [sia-am](datasets/sia-am.md) |
| `sia-an` | APAC de Nefrologia: uma APAC de nefrologia (terapia renal substitutiva), por competência | 2008-01 a 2014-10 | `convertido` | [sia-an](datasets/sia-an.md) |
| `sia-aq` | APAC de Quimioterapia: uma APAC de quimioterapia, por competência | 2008-01 a 2026-08 | `convertido` | [sia-aq](datasets/sia-aq.md) |
| `sia-ar` | APAC de Radioterapia: uma APAC de radioterapia, por competência | 2008-01 a 2026-08 | `convertido` | [sia-ar](datasets/sia-ar.md) |
| `sia-atd` | APAC de Tratamento Dialítico: uma APAC de tratamento dialítico, por competência | 2014-08 a 2026-08 | `convertido` | [sia-atd](datasets/sia-atd.md) |
| `sia-pa` | Produção Ambulatorial: a produção ambulatorial aprovada de um procedimento em um estabelecimento, agregada por competência, ocupação, faixa etária, sexo e município | 1994-07 a 2026-08 | `convertido` | [sia-pa](datasets/sia-pa.md) |
| `sia-ps` | Psicossocial: um registro da RAAS psicossocial (ação de atenção psicossocial a um paciente) | 2012-11 a 2026-08 | `convertido` | [sia-ps](datasets/sia-ps.md) |
| `sia-sad` | Atenção Domiciliar: um registro da RAAS de atenção domiciliar | 2012-04 a 2018-10 | `convertido` | [sia-sad](datasets/sia-sad.md) |

### SIH — Sistema de Informações Hospitalares (`sih`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sih-er` | ER - AIH Rejeitadas com código de erro: um erro de processamento associado a uma AIH rejeitada | 2011-01 a 2026-09 | `convertido` | [sih-er](datasets/sih-er.md) |
| `sih-rd` | RD - AIH Reduzida: uma AIH (Autorização de Internação Hospitalar) aprovada, em uma competência de processamento | 1992-01 a 2026-09 | `convertido` | [sih-rd](datasets/sih-rd.md) |
| `sih-rj` | RJ - AIH Rejeitadas: uma AIH rejeitada no processamento, em uma competência | 2008-01 a 2026-09 | `convertido` | [sih-rj](datasets/sih-rj.md) |
| `sih-sp` | SP - Serviços Profissionais: um serviço profissional (ato) lançado em uma AIH aprovada | 1997-06 a 2026-09 | `convertido` | [sih-sp](datasets/sih-sp.md) |

### SIM — Sistema de Informação sobre Mortalidade (`sim`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sim-do-cid09` | Declarações de Óbito CID-9: uma Declaração de Óbito (um óbito) de 1979 a 1995, codificada pela CID-9 | 1979 a 1995 | `convertido` | [sim-do-cid09](datasets/sim-do-cid09.md) |
| `sim-do-cid10` | Declarações de Óbito CID-10: uma Declaração de Óbito (um óbito, fetal ou não) a partir de 1996, codificada pela CID-10 | 1996 a 2026 | `convertido` | [sim-do-cid10](datasets/sim-do-cid10.md) |
| `sim-doext-cid09` | Declarações de Óbito Externas CID-9: um óbito por causa externa, de 1979 a 1995 (CID-9) | 1979 a 1995 | `convertido` | [sim-doext-cid09](datasets/sim-doext-cid09.md) |
| `sim-doext-cid10` | Declarações de Óbito Externas CID-10: um óbito por causa externa, a partir de 1996 (CID-10) | 1996 a 2025 | `convertido` | [sim-doext-cid10](datasets/sim-doext-cid10.md) |
| `sim-dofet-cid09` | Declarações de Óbito Fetais CID-9: um óbito fetal, de 1979 a 1995 (CID-9) | 1979 a 1995 | `convertido` | [sim-dofet-cid09](datasets/sim-dofet-cid09.md) |
| `sim-dofet-cid10` | Declarações de Óbito Fetais CID-10: um óbito fetal, a partir de 1996 (CID-10) | 1996 a 2025 | `convertido` | [sim-dofet-cid10](datasets/sim-dofet-cid10.md) |
| `sim-doinf-cid09` | Declarações de Óbito Infantis CID-9: um óbito de menor de 1 ano, de 1979 a 1995 (CID-9) | 1979 a 1995 | `convertido` | [sim-doinf-cid09](datasets/sim-doinf-cid09.md) |
| `sim-doinf-cid10` | Declarações de Óbito Infantis CID-10: um óbito de menor de 1 ano, a partir de 1996 (CID-10) | 1996 a 2025 | `convertido` | [sim-doinf-cid10](datasets/sim-doinf-cid10.md) |
| `sim-domat-cid10` | Declarações de Óbitos Maternos CID-10: um óbito materno, a partir de 1996 (CID-10) | 1996 a 2025 | `convertido` | [sim-domat-cid10](datasets/sim-domat-cid10.md) |
| `sim-dorext-cid10` | Mortalidade de Residentes no Exterior CID-10: um óbito de residente no exterior ocorrido no Brasil, a partir de 2013 (CID-10) | 2013 a 2025 | `convertido` | [sim-dorext-cid10](datasets/sim-dorext-cid10.md) |

### SINAN — Sistema de Informação de Agravos de Notificação (`sinan`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sinan-acbi` | Acidente de trabalho com material biológico: uma ficha de notificação/investigação de acidente de trabalho com material biológico | 2006 a 2026 | `convertido` | [sinan-acbi](datasets/sinan-acbi.md) |
| `sinan-acgr` | Acidente de trabalho: uma ficha de notificação/investigação de acidente de trabalho | 2006 a 2026 | `convertido` | [sinan-acgr](datasets/sinan-acgr.md) |
| `sinan-aida` | AIDS em adultos: uma ficha de notificação/investigação de aIDS em adultos | 2007 a 2024 | `convertido` | [sinan-aida](datasets/sinan-aida.md) |
| `sinan-aidc` | AIDS em crianças: uma ficha de notificação/investigação de aIDS em crianças | 2007 a 2024 | `convertido` | [sinan-aidc](datasets/sinan-aidc.md) |
| `sinan-anim` | Acidente por Animais Peçonhentos: uma ficha de notificação/investigação de acidente por Animais Peçonhentos | 2007 a 2026 | `convertido` | [sinan-anim](datasets/sinan-anim.md) |
| `sinan-antr` | Atendimento Antirrábico: uma ficha de notificação/investigação de atendimento Antirrábico | 2006 a 2026 | `convertido` | [sinan-antr](datasets/sinan-antr.md) |
| `sinan-botu` | Botulismo: uma ficha de notificação/investigação de botulismo | 2007 a 2026 | `convertido` | [sinan-botu](datasets/sinan-botu.md) |
| `sinan-canc` | Câncer relacionado ao trabalho: uma ficha de notificação/investigação de câncer relacionado ao trabalho | 2007 a 2026 | `convertido` | [sinan-canc](datasets/sinan-canc.md) |
| `sinan-chag` | Doença de Chagas Aguda: uma ficha de notificação/investigação de doença de Chagas Aguda | 2000 a 2025 | `convertido` | [sinan-chag](datasets/sinan-chag.md) |
| `sinan-chik` | Febre de Chikungunya: uma ficha de notificação/investigação de febre de Chikungunya | 2014 a 2026 | `convertido` | [sinan-chik](datasets/sinan-chik.md) |
| `sinan-cole` | Cólera: uma ficha de notificação/investigação de cólera | 2007 a 2025 | `convertido` | [sinan-cole](datasets/sinan-cole.md) |
| `sinan-coqu` | Coqueluche: uma ficha de notificação/investigação de coqueluche | 2007 a 2026 | `convertido` | [sinan-coqu](datasets/sinan-coqu.md) |
| `sinan-deng` | Dengue: uma ficha de notificação/investigação de dengue | 2000 a 2026 | `convertido` | [sinan-deng](datasets/sinan-deng.md) |
| `sinan-derm` | Dermatoses ocupacionais: uma ficha de notificação/investigação de dermatoses ocupacionais | 2006 a 2026 | `convertido` | [sinan-derm](datasets/sinan-derm.md) |
| `sinan-dift` | Difteria: uma ficha de notificação/investigação de difteria | 2007 a 2026 | `convertido` | [sinan-dift](datasets/sinan-dift.md) |
| `sinan-espo` | Esporotricose (Epizootia): uma ficha de notificação/investigação de esporotricose (Epizootia) | 2013 a 2022 | `convertido` | [sinan-espo](datasets/sinan-espo.md) |
| `sinan-esqu` | Esquistossomose: uma ficha de notificação/investigação de esquistossomose | 2007 a 2026 | `convertido` | [sinan-esqu](datasets/sinan-esqu.md) |
| `sinan-exan` | Doenças exantemáticas: uma ficha de notificação/investigação de doenças exantemáticas | 2007 a 2026 | `convertido` | [sinan-exan](datasets/sinan-exan.md) |
| `sinan-fmac` | Febre Maculosa: uma ficha de notificação/investigação de febre Maculosa | 2007 a 2026 | `convertido` | [sinan-fmac](datasets/sinan-fmac.md) |
| `sinan-ftif` | Febre Tifoide: uma ficha de notificação/investigação de febre Tifoide | 2007 a 2026 | `convertido` | [sinan-ftif](datasets/sinan-ftif.md) |
| `sinan-hans` | Hanseníase: uma ficha de notificação/investigação de hanseníase | 2001 a 2026 | `convertido` | [sinan-hans](datasets/sinan-hans.md) |
| `sinan-hant` | Hantavirose: uma ficha de notificação/investigação de hantavirose | 1999 a 2026 | `convertido` | [sinan-hant](datasets/sinan-hant.md) |
| `sinan-hepa` | Hepatites Virais: uma ficha de notificação/investigação de hepatites Virais | 2007 a 2023 | `convertido` | [sinan-hepa](datasets/sinan-hepa.md) |
| `sinan-hiva` | HIV em adultos: uma ficha de notificação/investigação de hIV em adultos | 2007 a 2024 | `convertido` | [sinan-hiva](datasets/sinan-hiva.md) |
| `sinan-hivc` | HIV em crianças: uma ficha de notificação/investigação de hIV em crianças | 2007 a 2024 | `convertido` | [sinan-hivc](datasets/sinan-hivc.md) |
| `sinan-hive` | HIV em crianças expostas: uma ficha de notificação/investigação de hIV em crianças expostas | 2015 a 2024 | `convertido` | [sinan-hive](datasets/sinan-hive.md) |
| `sinan-hivg` | HIV em gestante: uma ficha de notificação/investigação de hIV em gestante | 2007 a 2024 | `convertido` | [sinan-hivg](datasets/sinan-hivg.md) |
| `sinan-iexo` | Intoxicação Exógena: uma ficha de notificação/investigação de intoxicação Exógena | 2006 a 2026 | `convertido` | [sinan-iexo](datasets/sinan-iexo.md) |
| `sinan-leiv` | Leishmaniose Visceral: uma ficha de notificação/investigação de leishmaniose Visceral | 2000 a 2025 | `convertido` | [sinan-leiv](datasets/sinan-leiv.md) |
| `sinan-lept` | Leptospirose: uma ficha de notificação/investigação de leptospirose | 2000 a 2026 | `convertido` | [sinan-lept](datasets/sinan-lept.md) |
| `sinan-lerd` | LER/Dort: uma ficha de notificação/investigação de lER/Dort | 2006 a 2026 | `convertido` | [sinan-lerd](datasets/sinan-lerd.md) |
| `sinan-ltan` | Leishmaniose Tegumentar Americana: uma ficha de notificação/investigação de leishmaniose Tegumentar Americana | 2000 a 2025 | `convertido` | [sinan-ltan](datasets/sinan-ltan.md) |
| `sinan-mala` | Malária: uma ficha de notificação/investigação de malária | 2004 a 2026 | `convertido` | [sinan-mala](datasets/sinan-mala.md) |
| `sinan-meni` | Meningite: uma ficha de notificação/investigação de meningite | 2007 a 2026 | `convertido` | [sinan-meni](datasets/sinan-meni.md) |
| `sinan-ment` | Transtornos mentais relacionados ao trabalho: uma ficha de notificação/investigação de transtornos mentais relacionados ao trabalho | 2006 a 2026 | `convertido` | [sinan-ment](datasets/sinan-ment.md) |
| `sinan-ntra` | Notificação de Tracoma: uma ficha de notificação/investigação de notificação de Tracoma | 2010 a 2026 | `convertido` | [sinan-ntra](datasets/sinan-ntra.md) |
| `sinan-pair` | Perda auditiva por ruído relacionado ao trabalho: uma ficha de notificação/investigação de perda auditiva por ruído relacionado ao trabalho | 2006 a 2026 | `convertido` | [sinan-pair](datasets/sinan-pair.md) |
| `sinan-pest` | Peste: uma ficha de notificação/investigação de peste | 2007 a 2025 | `convertido` | [sinan-pest](datasets/sinan-pest.md) |
| `sinan-pfan` | Paralisia Flácida Aguda: uma ficha de notificação/investigação de paralisia Flácida Aguda | 2007 a 2026 | `convertido` | [sinan-pfan](datasets/sinan-pfan.md) |
| `sinan-pneu` | Pneumoconioses relacionadas ao trabalho: uma ficha de notificação/investigação de pneumoconioses relacionadas ao trabalho | 2006 a 2026 | `convertido` | [sinan-pneu](datasets/sinan-pneu.md) |
| `sinan-raiv` | Raiva: uma ficha de notificação/investigação de raiva | 2007 a 2026 | `convertido` | [sinan-raiv](datasets/sinan-raiv.md) |
| `sinan-rota` | Rotavírus: uma ficha de notificação/investigação de rotavírus | 2009 a 2026 | `convertido` | [sinan-rota](datasets/sinan-rota.md) |
| `sinan-sdta` | Surto Doenças Transmitidas por Alimentos: uma ficha de notificação/investigação de surto Doenças Transmitidas por Alimentos | 2007 a 2026 | `convertido` | [sinan-sdta](datasets/sinan-sdta.md) |
| `sinan-sifa` | Sífilis Adquirida: uma ficha de notificação/investigação de sífilis Adquirida | 2010 a 2025 | `convertido` | [sinan-sifa](datasets/sinan-sifa.md) |
| `sinan-sifc` | Sífilis Congênita: uma ficha de notificação/investigação de sífilis Congênita | 2007 a 2025 | `convertido` | [sinan-sifc](datasets/sinan-sifc.md) |
| `sinan-sifg` | Sífilis em Gestante: uma ficha de notificação/investigação de sífilis em Gestante | 2007 a 2025 | `convertido` | [sinan-sifg](datasets/sinan-sifg.md) |
| `sinan-src` | Síndrome da Rubéola Congênita: uma ficha de notificação/investigação de síndrome da Rubéola Congênita | 2007 a 2026 | `convertido` | [sinan-src](datasets/sinan-src.md) |
| `sinan-teta` | Tétano Acidental: uma ficha de notificação/investigação de tétano Acidental | 2007 a 2026 | `convertido` | [sinan-teta](datasets/sinan-teta.md) |
| `sinan-tetn` | Tétano Neonatal: uma ficha de notificação/investigação de tétano Neonatal | 2007 a 2026 | `convertido` | [sinan-tetn](datasets/sinan-tetn.md) |
| `sinan-toxc` | Toxoplasmose Congênita: uma ficha de notificação/investigação de toxoplasmose Congênita | 2019 a 2026 | `convertido` | [sinan-toxc](datasets/sinan-toxc.md) |
| `sinan-toxg` | Toxoplasmose Gestacional: uma ficha de notificação/investigação de toxoplasmose Gestacional | 2019 a 2026 | `convertido` | [sinan-toxg](datasets/sinan-toxg.md) |
| `sinan-trac` | Inquérito de Tracoma: uma ficha de notificação/investigação de inquérito de Tracoma | 2009 a 2026 | `convertido` | [sinan-trac](datasets/sinan-trac.md) |
| `sinan-tube` | Tuberculose: uma ficha de notificação/investigação de tuberculose | 2001 a 2025 | `convertido` | [sinan-tube](datasets/sinan-tube.md) |
| `sinan-varc` | Varicela: uma ficha de notificação/investigação de varicela | 2007 a 2026 | `convertido` | [sinan-varc](datasets/sinan-varc.md) |
| `sinan-viol` | Violência doméstica, sexual e/ou outras violências: uma ficha de notificação/investigação de violência doméstica, sexual e/ou outras violências | 2009 a 2025 | `convertido` | [sinan-viol](datasets/sinan-viol.md) |
| `sinan-zika` | Zika Vírus: uma ficha de notificação/investigação de zika Vírus | 2015 a 2026 | `convertido` | [sinan-zika](datasets/sinan-zika.md) |

### SINASC — Sistema de Informações sobre Nascidos Vivos (`sinasc`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sinasc-dn` | Declarações de nascidos vivos: uma Declaração de Nascido Vivo (um nascimento) | 1994 a 2026 | `convertido` | [sinasc-dn](datasets/sinasc-dn.md) |
| `sinasc-dnex` | Declarações de nascidos vivos no exterior: uma Declaração de Nascido Vivo de nascimento ocorrido no exterior | 2014 a 2024 | `convertido` | [sinasc-dnex](datasets/sinasc-dnex.md) |

### SISCOLO — Sistema de Informações do Câncer do Colo do Útero (`siscolo`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `siscolo-cc` | Citopatológico de Colo de Útero: um exame citopatológico do colo do útero | 2006-01 a 2015-10 | `convertido` | [siscolo-cc](datasets/siscolo-cc.md) |
| `siscolo-hc` | Histopatológico de Colo de Útero: um laudo histopatológico do colo do útero | 2006-01 a 2015-10 | `convertido` | [siscolo-hc](datasets/siscolo-hc.md) |

### SISMAMA — Sistema de Informação do Câncer de Mama (`sismama`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sismama-cm` | Citopatológico de Mama: um exame citopatológico de mama | 2009-01 a 2015-07 | `convertido` | [sismama-cm](datasets/sismama-cm.md) |
| `sismama-hm` | Histopatológico de Mama: um laudo histopatológico de mama | 2009-01 a 2015-07 | `convertido` | [sismama-hm](datasets/sismama-hm.md) |

### SISPRENATAL — Sistema de Monitoramento do Pré-Natal (`sisprenatal`)

| Dataset | O que é | Cobertura no FTP | Estado no lake | Página |
|---|---|---|---|---|
| `sisprenatal-pn` | Pré-Natal: um registro de acompanhamento de gestante | 2012-01 a 2014-12 | `convertido` | [sisprenatal-pn](datasets/sisprenatal-pn.md) |

## Como o DATASUS publica

- Os arquivos ficam sob `/dissemin/publicos/` do FTP, um diretório por sistema (`SIHSUS`, `SIASUS`, `CNES`, `SIM`, `SINASC`, `SINAN`...) e, dentro dele, subpastas por série (`199201_200712` e `200801_` no SIH, `CID9` e `CID10` no SIM), por dado final ou preliminar (`FINAIS` e `PRELIM` no SINAN) e por tipo (`Dados`, `Doc`, `Auxiliar`). As bases de território ficam em `/territorio/`.
- Os microdados são DBF compactados no formato DBC (compressão PKWARE DCL, que o fetcher descomprime em código nativo); há um arquivo por UF e competência (SIH, SIA, CNES), por UF e ano (SIM, SINASC) ou nacional por ano (SINAN e os recortes nacionais do SIM). As bases auxiliares vêm em ZIP.
- O nome do arquivo traz o prefixo do arquivo, a UF e o período (`RDSP2401.dbc`: AIH reduzida de São Paulo, janeiro de 2024). No lake, a UF vai para a coluna `uf` e o período vira as partições `ano` e `mes`.
- A documentação oficial (informes técnicos e dicionários de dados) fica em `Doc` ou `DOCS` e cobre só parte dos sistemas: não há dicionário para o SISCOLO, o SISMAMA, o SISPRENATAL e o CIH, e o SINASC publica só os nomes e tamanhos dos campos. Onde faltou, as páginas dizem que a descrição é inferida do nome do campo ou deixam a descrição em aberto.

## Relação entre as fontes

- `sih-rd` (AIH aprovadas) e `sih-rj`/`sih-er` (AIH rejeitadas e seus erros) são complementares; `sih-sp` detalha os serviços profissionais das AIH.
- `cih-cr` (2008 a 2011) é o antecessor de `ciha`, que passou a incluir o atendimento ambulatorial; nenhum dos dois é faturamento, e eles não se somam ao SIH nem ao SIA.
- `sia-an` (nefrologia, até 2014-10) foi substituído por `sia-atd` (tratamento dialítico) e `sia-acf` (fístula), com sobreposição em 2014.
- O SIM tem o dataset geral por UF de residência (`sim-do-*`) e recortes nacionais (fetal, infantil, materno, causas externas, residentes no exterior), que repetem registros do geral.
- Os denominadores populacionais (`base-populacional-ibge-*`) e a base territorial dão apoio às taxas calculadas com os demais datasets.

## Licença e uso

O fetcher declara a fonte como "sem licença declarada; dados públicos pela Lei 12.527/2011 (LAI) e Decreto 8.777/2016". Alguns arquivos trazem dados pessoais de pacientes ou profissionais (datas de nascimento, CEP, CNS, CPF, nome de profissional no CNES); cada página lista as colunas no campo `dados_pessoais`, como inventário por nome de coluna.

## Esquemas de referência

Os esquemas (`datasets/*.schema.json`) foram gerados em 2026-11-16 por conversão local, com o conversor atual (`datasus-fetcher` 0.19.0), de **amostras pequenas** do FTP: de 3 a 5 arquivos por dataset, escolhidos entre os mais antigos e os mais recentes e, dentro de cada ano, o menor arquivo (que costuma ser o de uma UF pequena) para pegar as eras de leiaute. Períodos e UFs fora das amostras podem ter colunas que não aparecem nos esquemas, e a coluna `Período` do dicionário refere-se ao intervalo **amostrado**. Arquivos sem nenhuma linha foram deixados de fora dos esquemas, porque o conversor os grava com nomes de coluna em maiúsculas e com `_deleted` (ver Cuidados de uso nas páginas).

As descrições vêm, nesta ordem, do informe técnico ou dicionário do DATASUS (SIH, SIA, CNES, CIHA, SIM, SINAN, RESP, PCE e Painel de Oncologia), de texto escrito à mão quando o campo não consta do documento (marcado "inferido do nome do campo" quando não há definição oficial) e, no SINAN, de descrições do nível do grupo de campos (ex.: manifestações clínicas) quando o dicionário do agravo não define o campo isoladamente.

## Fora do lake ou parcial

- `base-territorial-mapas`: mapas `.MAP` do TabWin (`so-bruto`); o conversor os ignora.
- `base-territorial`: o lake guarda cada tabela do ZIP mais recente como `datasus/base-territorial-<tabela>`; o id `base-territorial` não existe como dataset do lake (`parcial`).

## Página anterior

Esta pasta substitui o índice geral (`datasets/README.md`) da documentação anterior, cujas fichas por dataset foram migradas para o formato da norma de documentação dos dados.
