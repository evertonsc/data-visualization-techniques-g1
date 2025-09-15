# 🗂️ Transform CSV file into graphics 📊

## Contextualization
The density graphics describe the relative probability and help with the visualization of the informations, which are hard to analyze from datatables.

A restaurant network provides lunch and dinner and works with tips for waiters. There are 245 clients and this company would like to make some analysis about the clients. The .csv file to be used is stored into data/ folder.
<br><br>
The following table represents a client-relation (rows) and theirs attributes: total_conta (total bill), gorjeta (tip), sexo (man or woman), fumante (is smoker or not), dia (day of the meal), tempo (lunch or dinner) e quantidade (people at the table).

<img width="765" height="365" alt="image" src="https://github.com/user-attachments/assets/911c9858-b927-4a74-93ee-e84c0caae56f" />


## Objective
Develop an algorithm using Python libraries as Seaborn, Pandas and Matplotlib to:

a) Create a density graphic of total tips by sex;<br>
b) Create a density graphic of total tips by number of people at the table;<br>
c) Create a density graphic of total tips by weekday;<br>
d) Based on the visualizations created in items a, b and c, what can be assessed in relation to this restaurant company?


## Hands-on

### Requirements
* You must have Python installed;
* You must have Seaborn, Pandas and Matplotlib libraries installed. `pip install seaborn matplotlib pandas`

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
Based on graphics, it is possible to observe some relevant patterns to the restaurant's management:

By sex:
Both men and women presented similar distributions, with the highest peak in tips between 2 and 3 monetary units. This indicates that most tips, regardless of gender, tend to be concentrated in this range. The curve for women (purple) is slightly more accentuated at the peak, which means there is a higher concentration of tips close to the average among them. On the other hand, the curve for men (blue) is slightly more spread out, suggesting greater variability. In other words, there are cases of both smaller and larger tips. 

At higher values (above 6 monetary units), it can be observed that men have a relatively higher density than women. This indicates that, althought less frequent, the higher tips tend to be given by men. 

By number of people:
It is possible to observe some characteristics by separating people into groups. For example:

Small tables (1-2 people):
They give smaller tips on average, concentrated in 1 to 3 monetary units. The curves are very narrow, indicating more predictable values.

Medium tables (3-4 people):
There is a shift towards slightly larger tips, generally between 2 and 5 monetary units. The distribution begins to spread out more, showing greater diversity in value of tips.

Large tables (5-6 people):

The curves become even more open and shift to the right, with peaks between 4 and 6 monetary units. They indicate a higher probability of larger tip, althought there is still considerable variation. 

In general, the more people at the table, the higher the tip tends to be. In addition, larger tables show more dispersion, meaning that both average tips and more extreme values apperar more frequently

By day of the week:

Thursday (green):
It shows the sharpest and most concentrated peak, around 2 monetary units. This indicates that, on this day, most tips tend to be smaller and very consistent, with little dispersion.

Friday (red):
It also has a concentration close to 2–3 units, but with a slightly more spread distribution than on Thursday. This suggests greater variability in tips on Fridays.

Saturday (orange):
It has a more dispersed distribution, with significant values up to 10–12 monetary units. This indicates that on Saturdays there is a greater chance of high tips, even if they are less frequent. The main peak is between 2 and 3 units.

Sunday (blue):
Has a curve with a peak further to the right, between 3 and 4 units, standing out as the day with a tendency for slightly higher tips on average. Still, there is dispersion, with cases of larger tips.
