# fraudulent-transactions-detection-with-machinelearning
- sample project for implementing detection of fraudulent transactions using random forest algorithm.

## Clone
- git clone https://github.com/BensonsPage/fraudulent-transactions-detection-with-machinelearning

## Make App Changes.
- possible change include replacing your transactions_data.csv with your actual data.
- making changes to dataprocessor.py to reflect the new dataset.
- making changes to randomforestregressor.py to reflect the new dataset.
- making changes to app.py and forms.py as per new dataset.

## Checkout changes to a branch in your repository.
- git checkout -b branch-name
- git add * # To include changes in the commit.
- git commit -m "Update App" # To Commit your changes.
- git push origin branch-name # push the branch to the remote repository.
- Merge your changes to your main branch.

## build and run your docker container.
- navigate into the "fraudulent-transactions-detection-with-machinelearning" and run below command. <br />
docker compose up 
- If you encounter error, make the changes and run below command to rebuild the image. <br />
docker compose up -d --no-deps --build fraudulent-transactions-detection-service
- If you navigate to on your browser, you should see your app running on. <br />
http://localhost:8000
- You can as well see your container "fraudulent-transactions-detection-app" running.
- Open the container terminal and run below command. <br />
pip install imblearn
- Ensure imblearn has installed successfully then run below command to train the "Random Forest" Algorith. <br />
python3 randomforestregressor.py
- If you made some changes to the dataset, ensure you address the errors related to the dataset.
- You should be able to push a payload to the saved model state and get your transaction classified through http://localhost:8000.
