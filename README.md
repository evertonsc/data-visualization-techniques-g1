# 🗂️ Transform CSV file into graphics 📊

## Contextualization
The density graphics describe the relative probability and help with the visualization of the informations, which are hard to analyze from datatables.

A restaurant network provides lunch and dinner and works with tips for waiters. There are 245 clients and this company would like to make some analysis about the clients. The .csv file to be used is stored into data/ folder.
<br><br>
The following table represents a client-relation (rows) and theirs attributes: total_conta (total bill), gorjeta (tip), sexo (man or woman), fumante (is smoker or not), dia (day of the meal), tempo (lunch or dinner) e quantidade (people at the table).

<img width="765" height="365" alt="image" src="https://github.com/user-attachments/assets/911c9858-b927-4a74-93ee-e84c0caae56f" />


## Objective
Develop an algorithm using Python libraries as Seaborn, Pandas and Matplotlib to:

a) Create a density graphic of total tips by sex.<br>
b) Create a density graphic of total tips by quantity of people at the table.<br>
c) Create a density graphic of total tips by weekday;<br>
d) Based on the visualizations created in items a, b and c, what can be assessed in relation to this restaurant company?


## Hands-on

### Requirements
* You must have Python installed;
* You must have Seaborn, Panda and Matplotlib libraries installed. `pip install seaborn matplotlib pandas`

### Execution
* Run `python main.py` to make the out/ dir with the generated graphics.

### Expected
* Three images with their respective density graphic.

#### a) Density by sex:
<img width="1513" height="907" alt="image" src="https://github.com/user-attachments/assets/12c1d38a-b181-4f1e-9c5d-07e6df19fa4e" />


#### b) Density by people at the table:
<img width="1526" height="916" alt="image" src="https://github.com/user-attachments/assets/635cc10c-e64b-4f10-abea-9206598e09bc" />


#### c) Density by weekdays:
<img width="1524" height="915" alt="image" src="https://github.com/user-attachments/assets/03641fdc-7f74-4137-99ff-ab9794cb5b1c" />


#### d) Assessment based on the graphics:

