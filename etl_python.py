from csv import reader
from collections import defaultdict
import time

from pathlib import Path

PATH_DO_TXT = "data\measurements.txt"

def processar_temperaturas(path_do_txt: Path) -> dict:
    print("Iniciando o processamento do arquivo.")

    start_time = time.time()

    temperatura_por_station = defaultdict(list)

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)

    print("Dados carregados. Calculando estatísticas...")

    # Dicionário para armazenar os dados calculados
    results = {}

    # calculando temperatura minima, maxima e media e armazenando em results
    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)

        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatística calculada. Ordenando...")

    #Ordenando os resultados pelo nome da estacao
    sorted_results = dict(sorted(results.items()))

    ##### formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results}
    
    #Formata o dicionario conforme "regra de negocio"
    formatted_results = {}
    for station, (minimo, media, maximo) in sorted_results.items():
        formatted_results[station] = f"{minimo:.1f}/{media:.1f}/{maximo:.1f}"

    end_time = time.time() # tempo de termino
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    return formatted_results

if __name__ == "__main__":
    path_do_txt: Path = Path("data\measurements.txt")
    resultados = processar_temperaturas(path_do_txt)
    
    #print(resultados)