import matplotlib.pyplot as plt
def crear_diagrama_barras(marcas_clase, frecuencias, marcas_texto):
    plt.figure(figsize=(12, 6))
    
    plt.barh(marcas_clase, frecuencias,
             height=0.75, edgecolor="k",
             color=["#E81162", "#E89D11", "#38E811", "#11E8D8", "#A711E8", "#EFE4B4"])
    
    plt.yticks(marcas_clase, marcas_texto, fontsize=15)
    plt.xlabel("Frecuencias", fontsize=20)
    plt.ylabel("Marcas de clase", fontsize=20)
    plt.title("Diagrama de barras", fontsize=25)
    plt.grid()
    plt.show()