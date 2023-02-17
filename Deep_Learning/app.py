import tkinter as tk
import customtkinter as ctk 
from customtkinter import CTkImage
import numpy as np
from keras.models import load_model
import keras

from PIL import Image
import tkinter as tk
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

app = ctk.CTk()
app.resizable(False, False)
app.geometry("600x700")
app.title("Diabets Predictor")
ctk.set_appearance_mode("dark")

counter = 0
df_diabetes = pd.read_csv('data-diabetes.csv')


# Drop the columns 2 and 3
df_diabetes = df_diabetes.drop(columns=[df_diabetes.columns[2], df_diabetes.columns[3]])

# Select columns from 0 to 8 (inclusive)
dataset_X = df_diabetes.iloc[:, :6].values

sc = MinMaxScaler(feature_range = (0,1))
dataset_scaled = sc.fit_transform(dataset_X)


class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="", color="grey", height=30, width=200, font=("Verdana", 10), fg_color="black", corner_radius=5):
        super().__init__(master, width=50, font=font, fg=fg_color,  highlightthickness=5, highlightcolor="#b7e3fd", borderwidth=0)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self["fg"]

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color
        

    def foc_in(self, *args):
        if self["fg"] == self.placeholder_color:
            self.delete("0", "end")
            self["fg"] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class PredictionForm(tk.Tk):
    def __init__(self):

        frame = ctk.CTkFrame(app, fg_color="transparent")
        
        imgGif = ctk.CTkLabel(frame, text="")
        imgGif.pack(pady=(0, 10))
        # Chargement de l'image à l'aide de PIL
        pil_image = Image.open("./image_diabets.webp")
        imgtk = CTkImage(pil_image, size=(600,300)) 
        imgGif.imgtk = imgtk
        imgGif.configure(image=imgtk)

        # Créez les widgets d'entrée 
        frame1 = ctk.CTkFrame(frame, fg_color="transparent")
        frame1.pack()
        self.Pregnancies_entry = PlaceholderEntry(frame1, placeholder="Pregnancies", color="grey")
        self.Pregnancies_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.Glucose_entry = PlaceholderEntry(frame1, placeholder="Glucose", color="grey")
        self.Glucose_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        '''
        self.BloodPressure_entry = PlaceholderEntry(frame1, placeholder="BloodPressure", color="grey")
        self.BloodPressure_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.SkinThickness_entry = PlaceholderEntry(frame1, placeholder="SkinThickness", color="grey")
        self.SkinThickness_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        '''

        self.Insulin_entry = PlaceholderEntry(frame1, placeholder="Insulin", color="grey")
        self.Insulin_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.BMI_entry = PlaceholderEntry(frame1, placeholder="BMI", color="grey")
        self.BMI_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.DiabetesPedigreeFunction_entry = PlaceholderEntry(frame1, placeholder="DiabetesPedigreeFunction", color="grey")
        self.DiabetesPedigreeFunction_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.Age_entry = PlaceholderEntry(frame1, placeholder="Age", color="grey")
        self.Age_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.login_button = ctk.CTkButton(frame, text="Predict", command=self.login, text_color="white", height=50, font=("Verdana", 25, "bold"), width=300, fg_color="#3AA48F")
        self.error_label = ctk.CTkLabel(frame, text="", text_color="orange")

        # Placez les widgets dans la fenêtre
        self.Pregnancies_entry.pack(pady=5)
        
        self.Glucose_entry.pack(pady=5)

        '''
        self.BloodPressure_entry.pack(pady=5)

        self.SkinThickness_entry.pack(pady=5)
        '''
        
        self.Insulin_entry.pack(pady=5)

        self.BMI_entry.pack(pady=5)

        self.DiabetesPedigreeFunction_entry.pack(pady=5)

        self.Age_entry.pack(pady=5)
        
        self.login_button.pack(pady=15)
        self.error_label.pack(pady=5)
        
        frame.pack(fill=tk.BOTH, expand=True)

    def login(self):
        # Chargement du modèle sauvegardé
        model = keras.models.load_model('model.h5')

        # Création d'un exemple à prédire (assurez-vous que les dimensions sont les mêmes que celles des données d'entraînement)
        final_features = [np.array([self.Pregnancies_entry.get(), self.Glucose_entry.get(), self.Insulin_entry.get() ,self.DiabetesPedigreeFunction_entry.get(), self.BMI_entry.get(), self.Age_entry.get()])]

        # Prédiction de la sortie pour l'exemple créé
        prediction = model.predict(sc.transform(final_features))
        print("prediction ", prediction)

        for widget in app.winfo_children():
                widget.destroy()

        if prediction > 0.5:
            BadResult(prediction * 100)
        else:
            GoodResult(prediction * 100)



class GoodResult(tk.Tk):
    def __init__(self, precision):

        frame = ctk.CTkFrame(app, fg_color="transparent")
        
        imgGif = ctk.CTkLabel(frame, text="")
        imgGif.pack()
        # Chargement de l'image à l'aide de PIL
        pil_image = Image.open("./dontHave.png")
        imgtk = CTkImage(pil_image, size=(600,550)) 
        imgGif.imgtk = imgtk
        imgGif.configure(image=imgtk)

        frame.pack(fill=tk.BOTH, expand=True)
                
        label = "With precision equal to : " + str(round(precision[0][0], 2)) + "%"

        self.precision_label = ctk.CTkLabel(frame, text= label, text_color="black", font=("Verdana", 25, "bold"), width=600, fg_color="#ededed", height=50)
        
        self.test_button = ctk.CTkButton(frame, text="Test again",text_color="white", command=self.test_again, height=50, font=("Verdana", 25, "bold"), width=300, fg_color="#3AA48F")

        self.precision_label.pack(pady=0)

        self.test_button.pack(pady=15)

        frame.pack(fill=tk.BOTH, expand=True)

    def test_again(self):
        for widget in app.winfo_children():
                widget.destroy()
        PredictionForm()

class BadResult(tk.Tk):
    def __init__(self, precision):

        frame = ctk.CTkFrame(app, fg_color="transparent")
        
        imgGif = ctk.CTkLabel(frame, text="")
        imgGif.pack()
        # Chargement de l'image à l'aide de PIL
        pil_image = Image.open("./youHave.png")
        imgtk = CTkImage(pil_image, size=(600,550)) 
        imgGif.imgtk = imgtk
        imgGif.configure(image=imgtk)
        
        label = "With precision equal to : " + str(round(precision[0][0], 2)) + "%"

        self.precision_label = ctk.CTkLabel(frame, text= label, text_color="black", font=("Verdana", 25, "bold"), width=600, fg_color="#ededed", height=50)
        
        self.test_button = ctk.CTkButton(frame, text="Test again",text_color="white", command=self.test_again, height=50, font=("Verdana", 25, "bold"), width=300, fg_color="#3AA48F")

        self.precision_label.pack(pady=0)

        self.test_button.pack(pady=15)

        frame.pack(fill=tk.BOTH, expand=True)

    def test_again(self):
        for widget in app.winfo_children():
                widget.destroy()
        PredictionForm()


# Fenetre de prediction
PredictionForm()

app.mainloop()