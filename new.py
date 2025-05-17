## Importing the libraries
import streamlit as st
import pickle
import numpy as np

## Loading the model
loaded_model = pickle.load(open('churn_model.sav', 'rb'))

def churn_prediction(input_data):
    input_data_as_numpy = np.asarray(input_data)
    input_data_reshape = input_data_as_numpy.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshape)

    if prediction[0] == 1:
        return 'The customer is likely to churn'
    else:
        return 'The customer is not likely to churn'

# Dashboard Page
def main():
    st.title('Churn Modelling Prediction')
    
    ## User input columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        CreditScore = st.number_input('Credit Score', value=0.0)
        Gender = st.number_input('Gender (1 & 0)', value=0.0)
        Age = st.number_input('Age', value=0.0)

    with col2:
        Tenure = st.number_input('Tenure (in years)', value=0.0)
        Balance = st.number_input('Balance', value=0.0)
        NumOfProducts = st.number_input('Number of Products', value=0.0)

    with col3:
        HasCrCard = st.number_input('Has Credit Card (1 & 0)', value=0.0)
        IsActiveMember = st.number_input('Is Active Member (1 & 0)', value=0.0)
        EstimatedSalary = st.number_input('Estimated Salary', value=0.0)

    with col4:
        Geography_France = st.number_input('Geography France (1 & 0)', value=0.0)
        Geography_Germany = st.number_input('Geography Germany (1 & 0)', value=0.0)
        Geography_Spain = st.number_input('Geography Spain (1 & 0)', value=0.0)

    ## Making the prediction
    if st.button('Predict Churn'):
        try:
            input_data = [
                float(CreditScore), 
                float(Gender), 
                float(Age),
                float(Tenure), 
                float(Balance),
                float(NumOfProducts),
                float(HasCrCard), 
                float(IsActiveMember), 
                float(EstimatedSalary),
                float(Geography_France), 
                float(Geography_Germany),
                float(Geography_Spain),
            ]
            result = churn_prediction(input_data)  # Corrected function name
            st.success(result)
        except ValueError:
            st.error('Please enter a numeric value.')
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()