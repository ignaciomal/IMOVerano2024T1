def imprimir_tabla(clases_orden, fa_sorted, frecuencia_rel, frecuencia_rel_acum):
    # Imprimir encabezados
    print('Clases'.ljust(10), 'Fa'.ljust(8), 'Fr'.ljust(8), 'F acumulada'.ljust(12))
    print('------'.ljust(10), '---'.ljust(8), '---'.ljust(8), '-----------'.ljust(12))

    # Iterar sobre las clases y sus correspondientes datos
    for i in range(len(clases_orden)):
        print(f' {clases_orden[i]}'.ljust(10),
              str(fa_sorted[i]).ljust(8),
              f'{frecuencia_rel[i]:.2f}'.ljust(8),
              str(frecuencia_rel_acum[i]).ljust(12))