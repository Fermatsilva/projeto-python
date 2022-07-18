"""
Escreva um programa em Python que resolve a versão geral do problema acima. Peça ao usuário que entre com a hora atual (em horas) e que entre com o número de horas que deverá esperar antes do alarme tocar. Seu programa deve imprimir a hora que o alarme irá tocar.
"""

from turtle import end_fill


hora_atual = input("Qual é a hora atual? Escreva em 'horas'")
hora_atual = int(hora_atual)
hora_atual = hora_atual * 60 * 60

hora_espera = input("Quantas horas você deseja esperar? Escreva em 'horas'")
hora_espera = int(hora_espera)
hora_espera =  hora_espera * 60 * 60

hora_alarme = hora_atual + hora_espera

hora_alarme_dias = hora_alarme / 86400  #tempo em dias
hora_alarme_dias_resto = hora_alarme // 86400 #resto

hora_alarme_horas = (hora_alarme_dias//86400)/3600  #tempo em horas
hora_alarme_horas_resto = hora_alarme_horas // 3600 #resto

hora_alarme_minuto = (hora_alarme_horas // 3600)/60 #tempo em minutos
hora_alarme_minuto_resto = hora_alarme_minuto // 60 #resto

hora_alarme_segundo = hora_alarme_minuto // 60  #tempo em segundos

if hora_alarme_dias_resto == 0:
  print("O seu alarme dispertará em", hora_alarme_dias, "dias" )
else:
  if hora_alarme_horas_resto == 0:
    print("O seu alarme dispertará em", hora_alarme_dias, "dias e", hora_alarme_horas, "horas")
  else:
    if hora_alarme_minuto_resto == 0:
      print("O seu alarme dispertará em", hora_alarme_dias, "dias", hora_alarme_horas, "horas e", hora_alarme_segundo "segundos".)