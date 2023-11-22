import streamlit as st
import pickle
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

    
def count_numbers(s):
    num_count = sum(c.isdigit() for c in s)
    return num_count

def count_alpha(s):
    alpha_count = sum(c.isalpha() for c in s)
    return alpha_count

def check_status(data):
    prediction = classifier.predict([data])
    if prediction == 0:
        return "The Coin is predicted as Bitcoin"
    elif prediction == 1:
        return "The Coin is predicted as Dogecoin"
    elif prediction == 2:
        return "The Coin is predicted as Ethereum" 
    elif prediction == 3:
        return "The Coin is predicted as Litecoin" 


def main():
    html_temp = """
    <div style="background-color:black; padding:10px">
    <h2 style="color:white;text-align:center;">INDIGENOUS CRYPTOCURRENCY INVESTIGATION TOOLKIT</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    private_key = st.text_input("ENTER PRIVATE KEY" , "")
    public_key = st.text_input("ENTER PUBLIC KEY" , "")
    data=list()
    data.append(count_numbers(private_key))
    data.append(count_alpha(private_key))
    data.append(count_numbers(public_key))
    data.append(count_alpha(public_key))
    data.append(len(private_key))
    data.append(len(public_key))
    result=""
    if st.button("Predict"):
        result = check_status(data)
    st.success("Prediction: {}".format(result))

if __name__ == '__main__':
    main()

