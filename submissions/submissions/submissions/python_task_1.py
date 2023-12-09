import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)
    for i in range(min(car_matrix.shape)):
        car_matrix.iloc[i, i] = 0

    return car_matrix

df = pd.read_csv("dataset-1 assessment.csv")
generate_car_matrix(df)



