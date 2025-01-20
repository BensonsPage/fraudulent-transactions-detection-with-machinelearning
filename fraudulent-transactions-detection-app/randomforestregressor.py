import pickle
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from dataprocessor import DataProcessor
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score
from imblearn.pipeline import Pipeline

class RandomForestBasedModel:
    rf_model = None
    val_x = None
    val_y = None

    def __init__(self):
        data_processor_obj = DataProcessor()
        data_processor_obj.clean_data()
        data_processor_obj.explore_data()
        self.ml_features_selected = data_processor_obj.select_ml_data()

    def train_model(self):
        # Balancing The Dataset
        # The data is highly imbalanced, meaning if use it for training the way it is, the model will have poor performance on detecting fraud transactions.

        # Under-sampling and Over-sampling
        over = SMOTE(sampling_strategy = 0.8)
        under = RandomUnderSampler(sampling_strategy = 0.1)
        x = self.ml_features_selected.iloc[:,:7].values
        y = self.ml_features_selected.iloc[:,7].values

        steps = [('under', under),('over', over)]
        pipeline = Pipeline(steps=steps)
        x, y = pipeline.fit_resample(x, y)
        print (Counter(y))
        # Split into validation and training data
        train_x, self.val_x, train_y, self.val_y = train_test_split(x, y, test_size=0.2)

        # Define the model. Set random_state to 1
        self.rf_model = RandomForestRegressor(random_state=42)

        # fit your model
        self.rf_model.fit(train_x, train_y)

    def evaluate_model(self):
        # Save Model State
        filename = 'rf_model.sav'
        pickle.dump(self.rf_model, open(filename, 'wb'))

        rf_val_predictions = self.rf_model.predict(self.val_x)

        # Takes prediction and round them off to the nearest number.
        rf_ytest_pred = [round(a) for a in rf_val_predictions]
        rf_y_true_test = [round(a) for a in self.val_y]



        #Calculate the mean absolute error of your Random Forest model on the validation data
        rf_val_mae = mean_absolute_error(rf_val_predictions, rf_y_true_test)

        print("Validation MAE for Random Forest Based Model: {}".format(rf_val_mae))


        conf_matrix = confusion_matrix(rf_y_true_test, rf_ytest_pred)

        print("Confusion Matrix for Random Forest Based Model")
        print("-----------")
        print(conf_matrix)
        print("Precision :\t"+str(precision_score(rf_y_true_test,rf_ytest_pred)))
        print("Recall:\t"+str(recall_score(rf_y_true_test,rf_ytest_pred)))
        print("F1 Score of the Model :\t"+str(f1_score(rf_y_true_test,rf_ytest_pred)))

        # Confusion Matrix Visualization
        sns.heatmap(conf_matrix,
                    annot=True,
                    fmt='g',
                    xticklabels=['1','0'],
                    yticklabels=['1','0'])
        plt.ylabel('Actual', fontsize=13)
        plt.title('Confusion Matrix', fontsize=17, pad=20)
        plt.gca().xaxis.set_label_position('top')
        plt.xlabel('Prediction', fontsize=13)
        plt.gca().xaxis.tick_top()

        plt.gca().figure.subplots_adjust(bottom=0.2)
        plt.gca().figure.text(0.5, 0.05, 'Prediction', ha='center', fontsize=13)
        plt.show()

RandomForestBasedModelObj = RandomForestBasedModel()
RandomForestBasedModelObj.train_model()
RandomForestBasedModelObj.evaluate_model()