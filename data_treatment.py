import pandas as pd
from sklearn.preprocessing import LabelEncoder

def treat_test_data(df, params):

    df["Title"] = df["Name"].apply(lambda x: x.split(",")[-1].split()[0])

    df["Title"] = params['title_le'].fit_transform(df["Title"])
    df["Sex"] = params['sex_le'].fit_transform(df["Sex"])

    for sex, age in params['age'].iteritems():
        df.loc[(df["Sex"] == sex) & (df["Age"].isnull()), "Age"] = age

    for class_, port in params['port'].iteritems():
        df.loc[(df["Pclass"] == class_) & (df["Embarked"].isnull()), "Embarked"] = port
    df["Embarked"] = params['port_le'].fit_transform(df["Embarked"])

    #Fill NaN with mean or most common value from train set
    for class_, fare in params['fare'].iteritems():
        df.loc[(df["Pclass"] == class_) & (df["Fare"].isnull()), "Fare"] = fare

    #Drop columns that are not needed
    df = df.drop(["PassengerId", "Cabin", "Ticket", "Name"], axis=1)


    return df

def treat_train_data(df):

    df["Title"] = df["Name"].apply(lambda x: x.split(",")[-1].split()[0])

    name_le = LabelEncoder()
    df["Title"] = name_le.fit_transform(df["Title"])

    sex_le = LabelEncoder()
    df["Sex"] = sex_le.fit_transform(df["Sex"])

    df["Age"] = df.groupby("Sex")["Age"].transform(lambda x: x.fillna(int(x.mean())))
    mean_age_by_group = df.groupby('Sex')['Age'].mean().apply(int)

    df["Embarked"] = df.groupby("Pclass")["Embarked"].transform(lambda x: x.fillna(x.value_counts().idxmax()))
    port_by_group = df.groupby('Pclass')['Embarked'].agg(lambda x: x.value_counts().index[0])
    port_le = LabelEncoder()
    df["Embarked"] = port_le.fit_transform(df["Embarked"])

    df = df.drop(["PassengerId", "Cabin", "Ticket", "Name"], axis=1)

    default_fare = df.groupby('Pclass')['Fare'].mean().apply(int)
    default_sib = df['SibSp'].mean()
    default_parch = df['Parch'].mean()
    default_sex = df['Sex'].value_counts().idxmax()

    #For features without treatment, get mean or most common value

    treat_params = {
        'title_le': name_le,
        'sex_le': sex_le,
        'port_le': port_le,
        'age': mean_age_by_group,
        'port': port_by_group,
        'fare': default_fare,
        'sib': default_sib,
        'parch': default_parch,
        'sex': default_sex
    }

    return df, treat_params

if __name__ == "__main__":

    data_path = "./data/train.csv"
    df = pd.read_csv(data_path)
    train_df, params = treat_train_data(df)

    test_data_path = "./data/test.csv"
    df = pd.read_csv(test_data_path)
    test_df = treat_test_data(df, params)

    print(test_df.head())





