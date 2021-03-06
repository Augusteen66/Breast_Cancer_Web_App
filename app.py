import pickle
import streamlit as st

rf_model = pickle.load(open('cancer_random_forest_model.pkl', 'rb'))

def prediction(inputs):
    prediction = rf_model.predict([inputs])

    if prediction == 0:
        pred = "Benign"
    else:
        pred = "Malignant"

    return pred

def main():
    html_temp = """
    <div style = "background color: red; padding:10px">
    <h1 style = "color =#E69A8DFF; text-align:center; font : Oswald">Breast Cancer Predictor</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    activities = ['About', 'Predict']

    option = st.sidebar.selectbox('Menu', activities)

    if option == 'About':
        html_temp_about = """
        <h3 style = "color =#E69A8DFF; text-align:center; font : Oswald", padding = 30px>Welcome to Breast Cancer Predictor</h3>
        <p style = "color : navy;text-allign: center; padding : 30px">* Breast cancer (BC) is one of the most common cancers among women worldwide, representing the majority of new cancer cases and cancer-related deaths according to global statistics, making it a significant public health problem in today’s society.
        <br>* The early diagnosis of BC can improve the prognosis and chance of survival significantly, as it can promote timely clinical treatment to patients. ML techniques are being broadly used in the breast cancer classification problem. 
        <br>* They provide high classification accuracy and effective diagnostic capabilities.<br>* Navigate to predict section.
        </p>
        <h5 style = "color =#E69A8DFF; text-align:center; font : Oswald", padding = 30px>Made by Aagaaz Ali Sayed</h5>
        """
        st.markdown(html_temp_about, unsafe_allow_html=True)

    elif option == 'Predict':
        html_temp_enter = """
                    <div style = "padding:10px">
                    <h3 style = "color =#E69A8DFF; text-align:center; font: Oswald">Enter the details about the tumor for prediction.</h3>
                    </div>
                    """
        st.markdown(html_temp_enter, unsafe_allow_html=True)

        radius_worst = st.text_input("Worst Raduis")
        fractal_dimension_mean = st.text_input("Mean Fractional Dimension")
        perimeter_mean = st.text_input("Mean Perimeter")
        concave_points_mean = st.text_input("Mean Concave Points")
        compactness_se = st.text_input("SE Compactness")
        concavity_mean = st.text_input("Mean Concavity")
        concave_points_worst = st.text_input("Worst Concave Points")
        fractal_dimension_worst = st.text_input("Worst Fractional Dimension")
        area_se = st.text_input("SE Area")
        concavity_worst = st.text_input("Worst Concavity")
        concavity_se = st.text_input("SE Concavity")
        symmetry_mean = st.text_input("Mean Symmetry")

        inputs = [radius_worst, fractal_dimension_mean, perimeter_mean, concave_points_mean, compactness_se,
                  concavity_mean, concave_points_worst, fractal_dimension_worst, area_se, concavity_worst, concavity_se,
                  symmetry_mean]
        result = ""

        if st.button('CALCULATE'):
            st.write(("**Cancer Prediction**"))
            result = prediction(inputs)
            st.success('Your tumor is {}'.format(result))
        else:
            pass

if __name__ == '__main__':
    main()