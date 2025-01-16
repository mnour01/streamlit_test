import streamlit as st

st.title("Bonjour Streamlit!")
st.header("Première application Mehdi Nour")
st.text("Ceci est une application simple utilisant Streamlit.")


name = st.text_input("Quel est votre nom?")
st.write(f"Bonjour, {name}!")


# if st.button("Cliquez ici"):
#     st.write("Bouton cliqué!")


# number = st.slider("Choisissez un nombre", 0, 100, 50)
# st.write(f"Le nombre choisi est {number}")


# option = st.selectbox("Choisissez une option", ["Option 1", "Option 2", "Option 3"])
# st.write(f"Vous avez sélectionné {option}")


# import pandas as pd

# data = pd.DataFrame({
#     'Colonne 1': [1, 2, 3, 4],
#     'Colonne 2': [10, 20, 30, 40]
# })
# st.write("Voici un DataFrame :", data)


# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# st.pyplot(fig)




# import numpy as np
# import pandas as pd

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(chart_data)



# if st.checkbox("Afficher un message secret"):
#     st.write("🎉 Vous avez trouvé le secret!")
