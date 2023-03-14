import functions as fun

fun.crear_csv_comics(letra='M', nombre_archivo='comics_m_2.csv', offset=100)

total_characters = fun.hacer_peticion(letra='M')

print(total_characters['data']['total'])