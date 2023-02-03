import pandas as pd


def main():
    df = pd.read_csv('recipes.csv')
    print(df.columns)
    print(df['directions'])

if __name__ == "__main__":
    main()
