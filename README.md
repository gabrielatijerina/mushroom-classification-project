# Mushroom Classification Project
by: Gabriela Tijerina 
****

“I see the mycelium as the Earth's natural Internet, a consciousness with which we might be able to communicate. Through cross-species interfacing, we may one day exchange information with these sentient cellular networks. Because these externalized neurological nets sense any impression upon them, from footsteps to falling tree branches, they could relay enormous amounts of data regarding the movements of all organisms through the landscape.” 
― Paul Stamets, ***Mycelium Running: How Mushrooms Can Help Save the World***
***

### Project Summary:

This dataset is from The Audobon Society Field Guide and consists of 8124 hypothetical samples corresponding to 23 species of gilled mushroom in the Agaricus and Lepiota family. Each entry has 22 features relating to the physical characteristics of each mushroom. Each species is identified as "definitely edible", "definitely poisonous", or of unknown edibility. The latter class has been merged with "definitely poisonous".


The purpose of this notebook is to explore any relationships that exist between the physical characteristics of mushrooms and to accurately predict if a mushroom is safe to eat from these characteristics using ML classification models. 


**Data Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/mushroom)
****

### Goals:
* Explore relationships that exist between the physical characteristics of mushrooms to accurately predict if a mushroom is safe to eat from these characteristics
* Build a model to predict whether or not a mushroom is edible or poisonous 
**** 

### Deliverables:
* README.md file explaining what the project is, how to reproduce our work, and our notes from project planning
* A final Jupyter Notebook [(Mushroom_Classification_Report.ipynb)](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/Mushroom_Classification_Report.ipynb) that includes discoveries I made and work I have done related to uncovering whether or not a mushroom is poisonous or edible
* Python files that automate the data acquisition (`acquire.py`) and data preparation (`prepare.py`) process. 
**** 

### Data Dictionary

| Features | Description | Data Type |
|---------|-------------|-----------|
| class* | poisonous=p, edible=e | object |
| cap-shape | bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s | object |
| cap-surface | fibrous=f,grooves=g,scaly=y,smooth=s | object |
| cap-color | brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y | object |
| bruises | bruises=t,no=f | object |
| odor | almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s | object |
| gill-attachment | attached=a,descending=d,free=f,notched=n |
| gill-spacing | close=c,crowded=w,distant=d | object |
| gill-size | broad=b,narrow=n | object |
| gill-color | black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,
pink=p,purple=u,red=e, white=w,yellow=y | object |
| stalk-shape | enlarging=e,tapering=t | object |
stalk-root | bulbous=b,club=c,cup=u,equal=e, rhizomorphs=z,rooted=r,missing=? | object |
| stalk-surface-above-ring | fibrous=f,scaly=y,silky=k,smooth=s | object |
| stalk-surface-below-ring | fibrous=f,scaly=y,silky=k,smooth=s | object |
| stalk-color-above-ring | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | object |
| stalk-color-below-ring | brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y | object |
| veil-type | partial=p,universal=u | object |
| veil-color | brown=n,orange=o,white=w,yellow=y | object |
| ring-number | none=n,one=o,two=t | object |
| ring-type | cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z | object |
| spore-print-color | black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y | object |
| population | abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y | object |
| habitat | grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d | object |

\* - Indicates the target feature in this data
***


### Data Science Pipeline:

#### 1. Acquire
- Summarize initial data to determine how data needs to be prepared and cleaned 
- Define functions to:
    - Acquire mushroom dataset and return as a dataframe
- All functions to acquire data are included in [acquire.py](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/acquire.py)

#### 2. Prepare
- Review data and address any missing or erroneous values 
- Define functions to:
    - Clean mushroom data and return as a clean dataframe 
    - Remove columns 
    - Encode data
- All functions to prepare the data are included in [prepare.py](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/prepare.py)

#### 3. Explore
- Create visualizations of variables 
- Run statistical tests 
- Summarize key findings and takeaways


#### 4. Model/Evaluate
- Goal: develop a model that performs better than the baseline
- Develop a baseline model and classification models 
- Summarize performance, interpret, and document results


#### 5. Deliver
- A final Jupyter Notebook [(Mushroom_Classification_Report.ipynb)](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/Mushroom_Classification_Report.ipynb) 

### Conclusion:
-  Random Forest, KNN, and Decision Tree models all performed well. I used Random Forest to test, and my model performed better than baseline with 100% accuracy. 

### Next Steps: 
- In the future, I would like to investigate the effectiveness of this model on new, unseen data.

****

### Instructions for Reproducing Project:  
All files are reproducible and available for download and use. 

1.  Read and follow this README.md. 

2.  Download the following files to your working directory:  
 - Download mushroom data set here: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/mushroom)
 - [Mushroom_Classification_Report.ipynb](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/Mushroom_Classification_Report.ipynb)
 - [acquire.py](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/acquire.py)
 - [prepare.py](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/prepare.py)
 
3. Run my final Jupyter Notebook [(Mushroom_Classification_Report.ipynb)](https://github.com/gabrielatijerina/mushroom-classification-project/blob/main/Mushroom_Classification_Report.ipynb) to reproduce my findings and analysis. 