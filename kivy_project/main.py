from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
import numpy as np
import pickle
from datetime import timedelta
from kivy_garden.graph import Graph, MeshLinePlot
from kivy.uix.floatlayout import FloatLayout

class FirstWindow(Screen):
    def next(self):
        show_popup().open()

class SecondWindow(Screen):
    wti = ObjectProperty(None)
    brent = ObjectProperty(None)
    lr = ObjectProperty(None)
    svm = ObjectProperty(None)
    displ = ObjectProperty(None)
    output = ObjectProperty(None)
    gtitle = ObjectProperty(None)
    #df_prediction = 0

    def toggle1(self):
        if self.wti.state == 'down':
            self.brent.size = 60,37.5
            self.wti.size = 120,37.5

            # self.wti.size_hint = None, None
            # self.brent.size_hint = None, None
        elif self.brent.state == "down":
            self.brent.size = 120, 37.5
            self.wti.size = 60,37.5
            # self.wti.size_hint = None, None
            # self.brent.size_hint = None, None
        if self.wti.state == 'normal' and self.brent.state == 'normal':
            self.wti.size = 90,37.5
            self.brent.size = 90, 37.5

    def toggle2(self):
        if self.lr.state == 'down':
            self.svm.size = 60,37.5
            self.lr.size = 120,37.5
            # self.wti.size_hint = None, None
            # self.brent.size_hint = None, None
        elif self.svm.state == "down":
            self.svm.size = 120, 37.5
            self.lr.size = 60,37.5
            # self.wti.size_hint = None, None
            # self.brent.size_hint = None, None
        if self.lr.state == 'normal' and self.svm.state == 'normal':
            self.lr.size = 90,37.5
            self.svm.size = 90, 37.5

    def oil_get(self):
        try:
            for plot in self.displ.plots:
                self.displ.remove_plot(plot)
        except:
            pass
        df_prediction = 0
        self.plot = 0
        if (self.wti.state == 'normal' and self.brent.state == 'normal') or (self.lr.state == 'normal' and self.svm.state == 'normal'):
            return None
        else:
            header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
            df = 0
            real_date = []
            real_price = []
            if self.wti.state == 'down':
                url = "https://www.investing.com/commodities/crude-oil-historical-data"
                req = urllib.request.Request(url, headers=header)
                html = urlopen(req).read()
                soup_html = soup(html, 'html.parser')
                data = soup_html.find(id="curr_table").find_all("tr")
                for i in data[1:]:
                    j = i.find_all("td")
                    real_price.append(j[1].text)
                    real_date.append(j[0].text)
                self.displ.ylabel = 'Price ($)'
                self.gtitle.text = 'WTI Price Forecast Using'

            elif self.brent.state == 'down':
                url = "https://www.investing.com/commodities/brent-oil-historical-data"
                req = urllib.request.Request(url, headers=header)
                html = urlopen(req).read()
                soup_html = soup(html, 'html.parser')
                data = soup_html.find(id="curr_table").find_all("tr")
                for i in data[1:]:
                    j = i.find_all("td")
                    real_price.append(j[1].text)
                    real_date.append(j[0].text)
                self.displ.ylabel = 'Brent Crude Oil Price'
                self.gtitle.text = 'Brent Price Forecast Using'

            df = pd.DataFrame({'Date': real_date, 'Price':real_price})
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_index(ascending=False).reset_index(drop=True)
            df['Price'] = df['Price'].astype(float)
            new_row = []

            if df.shape[0] == 23:
                for i in range(1,3):
                    new_row.append(df.iloc[-1][0]+timedelta(days=i))
                new_row = pd.DataFrame({'Date': new_row, 'Price':[np.nan,np.nan]})

            elif df.shape[0] == 24:
                new_row = pd.DataFrame({'Date': df.iloc[-1][0] + timedelta(days=1), 'Price':[np.nan]})

            df = df.append(new_row, ignore_index=True)
            df.fillna(df.mean(),inplace=True)
            array_df = np.array(df['Price']).reshape(-1,1)
            scaler = MinMaxScaler(feature_range=(0,1))
            scaled_df = scaler.fit_transform(array_df)
            x_forecast = np.array([[i[0]] for i in scaled_df][-25:])

            prediction = 0
            if self.lr.state == 'down' and self.wti.state == 'down':
                lr_model = pickle.load(open('lr.pkl', 'rb'))
                lr_prediction = lr_model.predict(x_forecast)
                prediction = scaler.inverse_transform(lr_prediction.reshape(-1,1))
                self.gtitle.text = self.gtitle.text + ' LR'

            elif self.svm.state == 'down' and self.wti.state == 'down':
                svm_model = pickle.load(open('svr.pkl', 'rb'))
                svm_prediction = svm_model.predict(x_forecast)
                prediction = scaler.inverse_transform(svm_prediction.reshape(-1,1))
                self.gtitle.text = self.gtitle.text + ' SVM'

            elif self.svm.state == 'down' and self.brent.state == 'down':
                svm_model = pickle.load(open('svrbrent.pkl', 'rb'))
                svm_prediction = svm_model.predict(x_forecast)
                prediction = scaler.inverse_transform(svm_prediction.reshape(-1,1))
                self.gtitle.text = self.gtitle.text + ' SVM'

            elif self.lr.state == 'down' and self.brent.state == 'down':
                svm_model = pickle.load(open('lrbrent.pkl', 'rb'))
                svm_prediction = svm_model.predict(x_forecast)
                prediction = scaler.inverse_transform(svm_prediction.reshape(-1,1))
                self.gtitle.text = self.gtitle.text + ' LR'

            date = []
            for i in range(1,26):
                date.append(df.loc[24,'Date']+timedelta(days=i))
            df_prediction = pd.DataFrame({'Date':date, 'Price':[i[0] for i in prediction]})
            df_prediction = df.append(df_prediction, ignore_index=True)
            self.displ.ymin = int(df_prediction['Price'].min() - 2)
            self.displ.ymax = int(df_prediction['Price'].max() + 2)
            self.displ.y_ticks_major = (int(df_prediction['Price'].max() + 2) - int(df_prediction['Price'].min() - 2))/2
            self.displ.y_grid_label = True

            plot = MeshLinePlot(color=[1,0,0,1])
            plot.points = [(i,df_prediction.iloc[i][1]) for i in range(50)]
            self.displ.add_plot(plot)

        # plot = MeshLinePlot(color=[1, 0, 0, 1])
        # plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        # self.displ.add_plot(plot)
        return df_prediction

class P(FloatLayout):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv

def show_popup():
    show = P()
    popupWindow = Popup(title='Welcome!', content=show,size_hint=(None,None), size=(420,400))
    return popupWindow

if __name__ == "__main__":
    MyMainApp().run()
