import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self):
        # Path of the file to read
        transactions_data_path = 'transactions-data/transactions_data.csv'
        self.transactions_data = pd.read_csv(transactions_data_path)

    def explore_data(self):
        # Describe data
        self.transactions_data.info()
        # Get data shape
        self.transactions_data.shape
    def clean_data(self):
        # Remove uNamed columns
        if 'Unnamed: 0' in self.transactions_data.columns:
            self.transactions_data.drop(['Unnamed: 0'], axis=1, inplace=True)
        # Check if there are missing values.
        missing_values_count = self.transactions_data.isnull().sum()
        print (missing_values_count) # This Data has no missing values
        # replace infinite values
        self.transactions_data.replace([np.inf, -np.inf], np.nan)
        # create a new column, TX_DATETIME_parsed, with the parsed dates %Y-%m-%d %H:%M:%S
        if 'TX_DATETIME' in self.transactions_data.columns:
            self.transactions_data['TX_DATETIME_parsed'] = pd.to_datetime(self.transactions_data['TX_DATETIME'], format='%Y-%m-%d %H:%M:%S')
            self.transactions_data.drop(['TX_DATETIME'], axis=1, inplace=True)

    def data_plotting(self):
        # define Seaborn color palette to use
        palette_color = sns.color_palette('bright')
        # declaring data
        data = [self.transactions_data['TX_FRAUD'].loc[self.transactions_data.TX_FRAUD == 1].count(), self.transactions_data['TX_FRAUD'].loc[self.transactions_data.TX_FRAUD == 0].count()]
        keys = ['Fraud', 'Not Fraud']
        # plotting data on chart
        plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
        # Pearson Correlation Heatmap (Shows strength of relationship between variable)
        ml_features_data = self.transactions_data.get(['CUSTOMER_ID', 'TX_FRAUD', 'TX_AMOUNT', 'TX_TIME_SECONDS', 'TX_TIME_DAYS', 'TX_FRAUD_SCENARIO', 'TX_DURING_WEEKEND', 'TX_DURING_NIGHT', 'CUSTOMER_ID_NB_TX_1DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW', 'CUSTOMER_ID_NB_TX_7DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW', 'CUSTOMER_ID_NB_TX_30DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW', 'TERMINAL_ID_NB_TX_1DAY_WINDOW', 'TERMINAL_ID_RISK_1DAY_WINDOW', 'TERMINAL_ID_NB_TX_7DAY_WINDOW', 'TERMINAL_ID_RISK_7DAY_WINDOW', 'TERMINAL_ID_NB_TX_30DAY_WINDOW', 'TERMINAL_ID_RISK_30DAY_WINDOW'])

        ml_features_data.shape
        plt.figure(figsize=(14, 6))
        sns.set(font_scale=0.5)
        sns.heatmap(ml_features_data.corr(), annot=True, cmap="YlGnBu")


        # # Box plot for identifying outliers, showing distribution between numeric data
        boxplot_data = ml_features_data.corr()
        ax = sns.boxplot(boxplot_data)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        plt.show()

    def select_ml_data(self):
        # Features Selection
        # According to the 'correlation heatmap', the features that most determines whether a transaction is fraud are  ['TX_TIME_DAYS', 'CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW', 'TERMINAL_ID_RISK_1DAY_WINDOW', 'TERMINAL_ID_RISK_7DAY_WINDOW', 'TERMINAL_ID_RISK_30DAY_WINDOW'], we will you them to train and validate a random forest algorithm.

        ml_features_selected = self.transactions_data.get(['TX_TIME_DAYS', 'CUSTOMER_ID_AVG_AMOUNT_1DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_7DAY_WINDOW', 'CUSTOMER_ID_AVG_AMOUNT_30DAY_WINDOW', 'TERMINAL_ID_RISK_1DAY_WINDOW', 'TERMINAL_ID_RISK_7DAY_WINDOW', 'TERMINAL_ID_RISK_30DAY_WINDOW', 'TX_FRAUD'])
        return ml_features_selected