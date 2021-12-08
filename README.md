# DMProject
This project focuses on finding if a property listed over renting applications will attract customers or not. Any property listed over applications has many basic information associated with it, such as number of bedrooms, number of bathrooms, price, location etc. Other than this they also have associated facilities included with the property. These are the factors that usually affect whether a property seems interesting to a customer or not. 

This app will be very useful to both the platform and property holder. 1) The property holder can identify if the listing that he is providing will attract enough attention or not, and he can modify his entries based on the outcomes from the algorithm. 2) The platform can identify which properties are more in demand and it can help understand what the customers are looking for, thus helping in supply chain.

This project will use the “Two Sigma Connect: Rental Listing Inquiries” dataset located on the Kaggle webpage here. This dataset includes 49352 training data points each with 15 features, and 74659 test data points with 14 features as the classification for these data points is not provided. The 15 features include: 

Out of the given features, we will extrapolate more features which are sort of hidden inside the ‘features’ feature of the dataset. We will also create new features that serve as obvious factors when looking for rooms, like price per room. 
The initial part would be exploring the data, and then we will use multiple classification algorithms, and measure their accuracy over the dataset, to see how well it performs. We will be experimenting with the hyperparameters for the classification algorithms, to fine tune our performance.
Some similar apps that do this are: AirBnB, RentHop, Zillow.


-----
HOW TO RUN THE APP
----
The following dependencies must be fulfilled

numpy

pickle

streamlit

Make sure that the files are present in the same directory.

We need the following command to run the app:

"streamlit run app.py"

Note that the model for random forst is not present, since the model is around 4GB size, it couldnt be uploaded to the github. Hence the Random Forest classification wouldn't work. You can use the ipnyb file to generate your own model and download the model file and run it. You can find the model for random forest [here](https://drive.google.com/file/d/1inofNpgwkwqSQqS_9aAeiOPberlobWJF/view?usp=sharing)

# Sample Run

Please find sample run of the application at the link above.

https://www.youtube.com/watch?v=pOptfqwF-ms
