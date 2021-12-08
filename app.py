import streamlit as st
import pickle
import numpy as np
from collections import OrderedDict
from datetime import datetime

my_dict = {
	'RandomForest[Best]': './rf_saved_model.pkl',
	'KNN': './knn_saved_model.pkl',
	'NBClassifier': './nb_saved_model.pkl',
	'SVM[2nd Best]': './svc_saved_model.pkl'
}

model = ''
def show_predict_page():
	data = OrderedDict()	
	st.title('Flat Propertsy Interest Predictor')
	st.write("""### Please provide the information""")

	
	data['bathrooms'] = st.slider("bathrooms", max_value=10, min_value=1)
	data['bedrooms'] = st.slider("bedrooms", max_value=10, min_value=1, step=1)
	lat_long = st.text_input("latitude,longitude", key='lat_long')
	if(lat_long and lat_long.split(',')):
		data['latitude'] = float(lat_long.split(',')[0].strip())
		data['longitude'] = float(lat_long.split(',')[1].strip())
	else:
		data['latitude'] = 0
		data['langitude'] = 0
	data['price'] = st.slider("Price", max_value=50000, step=100)
	data['nPhotos'] = st.slider("number of photos")
	desc = st.text_input("Description", key='desc')
	data['hasDesc'] = 1 if len(desc.strip())!=0 else 0
	# data['description'] = 
	data['nFeatures'] = st.slider("number of features")
	data['nDescWords'] = len(desc.split(" "))
	
	
	date = st.date_input("Date of enrolling the property", key='date')
	# dat = datetime.strptime(date, '%y/%m/%d')
	# print(date.month)
	data['month'] = date.month
	data['weekday'] = date.weekday()
	data['rooms'] = (data['bathrooms'] + data['bedrooms'])
	# print(date.weekday())
	data['price_per_room'] = data['price']/(data['bathrooms'] + data['bedrooms'])
	data['price_per_bedroom'] = data['price']/(data['bedrooms'])

	Parking = ('No', 'Yes') 
	Gym = ('No', 'Yes') 
	Pool = ('No', 'Yes') 
	Fee = ('No', 'Yes')
	Elevator = ('No', 'Yes')
	Garden = ('No', 'Yes')
	Furnished = ('No', 'Yes')
	reducedFee = ('No', 'Yes')
	AC =  ('No', 'Yes')
	Roof = ('No', 'Yes')
	petFriendly = ('No', 'Yes')
	shareable = ('No', 'Yes')
	freeMonth = ('No', 'Yes')
	utilIncluded = ('No', 'Yes')
	laundryIncluded = ('No', 'Yes')
	internetIncluded = ('No', 'Yes')
	Models = ('RandomForest[Best]', 'KNN', 'NBClassifier', 'SVM[2nd Best]')

	data['hasParking'] = 1 if(st.selectbox("Parking", Parking)=='Yes') else 0
	data['hasGym'] = 1 if st.selectbox("Gym", Gym)=='Yes' else 0
	data['noFee'] = 1 if st.selectbox("Extra Fees", Fee)=='Yes' else 0
	data['hasElevator'] = 1 if st.selectbox("Elevator", Elevator)=='Yes' else 0
	data['hasGarden'] = 1 if st.selectbox("Garden", Garden)=='Yes'else 0
	data['isFurnished'] = 1 if st.selectbox("Furnished", Furnished)=='Yes'else 0
	data['reducedFee'] = 1 if st.selectbox("reducedFee", reducedFee)=='Yes'else 0
	data['hasAC'] = 1 if st.selectbox("AC", AC)=='Yes'else 0
	data['hasRoof'] = 1 if st.selectbox("Roof", Roof)=='Yes'else 0
	data['petFriendly'] = 1 if st.selectbox("petFriendly", petFriendly)=='Yes'else 0
	data['shareable'] = 1 if st.selectbox("Shareable", shareable)=='Yes'else 0
	data['freeMonth'] = 1 if st.selectbox("freeMonth", freeMonth)=='Yes'else 0
	data['utilIncluded'] = 1 if st.selectbox("utilIncluded", utilIncluded)=='Yes'else 0
	data['laundryIncluded'] = 1 if st.selectbox("laundryIncluded", laundryIncluded)=='Yes'else 0
	data['internetIncluded'] = 1 if st.selectbox("internetIncluded", internetIncluded)=='Yes'else 0
	model = st.selectbox("Which Model", Models)
	ok = st.button("Find Interest Group")
	X = []
	if ok:
		f = open(my_dict[model],'rb')
		pickle_data = pickle.load(f)
		classfr = pickle_data["model"]
		temp = []
		for key in data:
			temp.append(data[key])
		X.append(temp)
		print(X)
		data = OrderedDict()
		intrst = classfr.predict(X)

		st.subheader(f"The estimated group interest level will be "+ intrst)


data = []
data = OrderedDict()
model = ''
# define_data()
show_predict_page()