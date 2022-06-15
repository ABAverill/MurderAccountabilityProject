import pandas as pd
# Import module for linear algebra
from numpy import where
import plotly.express as px

# Import module for k-protoype cluster
from kmodes.kprototypes import KPrototypes

# Import module for data visualization

#from plotnine import *
#import plotnine

# Ignore warnings
import warnings
warnings.filterwarnings('ignore', category = FutureWarning)

Regions = ['Midwest', 'Northeast', 'South', 'West']
Divisions = ['East North Central', 'West North Central', 'Middle Atlantic', 'New England', 'East South Central', 'South Atlantic', 'West South Central', 
             'Mountain', 'Pacific']

Years = ['1990', '1991', '1992', '1993', '1994','1995', '1996', '1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']

#Summary Dataframe
smry = pd.DataFrame(columns=['Divisions','Total_Murders', '1990', '1991', '1992', '1993', '1994','1995', '1996', '1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'])
smry.Divisions = Divisions

for i in range(0,9):
    Filename = Divisions[i] + ".csv"
    df = pd.read_csv(Filename,low_memory=False)
    myVars = locals()
    myVars[Divisions[i]] = df
    smry.Total_Murders[i] = len(df.ID)
    for q in range(0,31):
            Murdyear = df[(df.Year == int(Years[q]))]
            smry.iloc[i, q+2] = len(Murdyear.ID)

smry_new = smry.transpose()
smry_new1 = smry_new.drop('Total_Murders')

smry_new1.columns = smry_new1.iloc[0] 

smry_new1 = smry_new1[1:]
smry_new1 = smry_new1.reset_index()

fig = px.line(smry_new1, x = 'index', y = Divisions, title = 'Murders by Year', labels={'x': 'Year', 'y':'Murders'})
fig.update_layout(
    xaxis_title="Year", yaxis_title="Murders"
)
fig.show()
