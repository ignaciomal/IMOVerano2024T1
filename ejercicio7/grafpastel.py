import matplotlib.pyplot as plt
def obt_graf_pastel(datos, marcas_texto):
    separaciones = [0] * len(datos)  # Lista de ceros del mismo tamaño que datos
    plt.figure(figsize=(8, 8))
    plt.pie(datos, 
            explode=separaciones,  
            counterclock=False, 
            startangle=90, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            colors=["#B63014", "#E811D1" , "#51B614", "#E8E811", "#EFB4C7", "#1111E8"], 
            labels=marcas_texto)
    plt.title("Grafico de pastel", fontsize=20)
    plt.show()
