import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
    car_matrix = car_matrix.fillna(0)
    for i in range(min(car_matrix.shape)):
        car_matrix.iloc[i, i] = 0

    return car_matrix

df = pd.read_csv("dataset-1 assessment.csv")
generate_car_matrix(df)





def get_type_count(df)->dict:
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    type_count = df['car_type'].value_counts().to_dict()
    type_count = dict(sorted(type_count.items()))
    return type_count

df = pd.read_csv('dataset-1 assessment.csv')
get_type_count(df)





def get_bus_indexes(df)->list:
    mean_bus_value = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()
    bus_indexes.sort()

    return bus_indexes

df = pd.read_csv('dataset-1 assessment.csv')
get_bus_indexes(df)





def filter_routes(df)->list:
    avg_route = df.groupby("route")['truck'].mean()
    filtered_routes = avg_route[avg_route > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes

df = pd.read_csv('dataset-1 assessment.csv')
filter_routes(df)
