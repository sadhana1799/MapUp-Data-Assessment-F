import pandas as pd   
import numpy as np
def calculate_distance_matrix(df)->pd.DataFrame():
    unique_ids = np.unique(df[['id_start', 'id_end']].values)
    distance_matrix = pd.DataFrame(0, index=unique_ids, columns=unique_ids)
    for index, row in df.iterrows():
        start_id, end_id, distance = row['id_start'], row['id_end'], row['distance']
        distance_matrix.loc[start_id, end_id] = distance

    for i in range(0,len(distance_matrix.columns)):
        for j in range(i+2,len(distance_matrix)):
          k= j-1
          distance_matrix.iloc[i, j] = distance_matrix.iloc[i, k] + distance_matrix.iloc[k, j]

    df = distance_matrix + distance_matrix.T

    return df
df = pd.read_csv("dataset-3 assessment.csv")
calculate_distance_matrix(df)





def unroll_distance_matrix(distance_matrix_df):
    unrolled_data = []
    for i in distance_matrix_df.index:
        for j in distance_matrix_df.columns:
            if i != j:
                unrolled_data.append({
                    'id_start': i,
                    'id_end': j,
                    'distance': distance_matrix_df.loc[i, j]
                })

    unrolled_df = pd.DataFrame(unrolled_data)

    return unrolled_df
distance_matrix_df = calculate_distance_matrix(df)
unroll_distance_matrix(distance_matrix_df)





def calculate_toll_rate(unrolled_df):
    result_df = unrolled_df.copy()
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        result_df[vehicle_type] = result_df['distance'] * rate_coefficient

    result_df = result_df.drop(columns=['distance'])

    return result_df

distance_matrix_df = calculate_distance_matrix(df)
unrolled_df = unroll_distance_matrix(distance_matrix_df)
calculate_toll_rate(unrolled_df)
