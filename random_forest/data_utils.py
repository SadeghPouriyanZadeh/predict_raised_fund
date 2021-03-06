import numpy as np
import pandas as pd
from sklearn.preprocessing import Normalizer, OneHotEncoder, OrdinalEncoder


def get_processed_data(ico_csv_path, target_feature, normalize=True, one_hot_encoder=True):
    df = pd.read_csv(ico_csv_path)
    df_x = df.drop(columns=[target_feature])
    df_y = df[target_feature]
    cat_cols = []
    con_cols = []
    for col in df_x.columns:
        if df_x[col].dtype == np.object_:
            cat_cols.append(col)
        else:
            con_cols.append(col)
    if one_hot_encoder:
        cats = OneHotEncoder(sparse=False).fit_transform(df_x[cat_cols])
    else:
        cats = OrdinalEncoder().fit_transform(df_x[cat_cols])
    if normalize:
        cons = Normalizer().fit_transform(df_x[con_cols])
    else:
        cons = df_x[con_cols].to_numpy()
    x = np.concatenate((cats, cons), axis=1)
    y = df_y.to_numpy()
    return x, y
