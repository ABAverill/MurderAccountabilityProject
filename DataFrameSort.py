import pandas as pd
# Import module for linear algebra
from numpy import where

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





# Format scientific notation from Pandas
pd.set_option('display.float_format', lambda x: '%.3f' % x)


df = pd.read_csv(r"C:\Users\AA-Computer\Documents\Andrew's Files\MAP Data Files\Python Code\1990-2020FullFile.csv",low_memory=False)


for i in range(0, len(Divisions)):
      newdf = df[(df.Division == Divisions[i])]


      # Get the position of categorical columns
      catColumnsPos = [newdf.columns.get_loc(col) for col in list(newdf.select_dtypes('object').columns)]
  
      dfMatrix = newdf.to_numpy()
      # Fit the cluster
      kprototype = KPrototypes(n_jobs = -1, n_clusters = 3,init = 'Huang', random_state = 0)
      kprototype.fit_predict(dfMatrix, categorical = catColumnsPos)
      # Cluster centorid
      kprototype.cluster_centroids_
      # Check the iteration of the clusters created
      kprototype.n_iter_
      # Check the cost of the clusters created
      kprototype.cost_
      # Add the cluster to the dataframe
      newdf['Cluster Labels'] = kprototype.labels_
      newdf['Segment'] = newdf['Cluster Labels'].map({0:'First', 1:'Second', 2:'Third'})
      # Order the cluster
      newdf['Segment'] = newdf['Segment'].astype('category')
      newdf['Segment'] = newdf['Segment'].cat.reorder_categories(['First','Second','Third'])
      
      myVars = locals()
      myVars[Divisions[i]] = newdf
           
    # File Exporting to csv
      output_file = Divisions[i] + ".csv"
      newdf.to_csv(output_file)
      
    
