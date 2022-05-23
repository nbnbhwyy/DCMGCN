## prediction and pattern discovery for drug combination based on multimodel friendship features

Our paper is at https:

![image](https://github.com/nbnbhwyy/DCGMCN/Flowchart.jpg)

## Installation
First install the dependencies via conda:
 * sklearn
 * numpy
 * Python >= 3.7
 * Pytorch
 
### Quick start
We provide an example script to run experiments on our dataset: 

- Run `DCGCN.ipynb`: predict drug-drug combinations, and evaluate the results with cross-validation. 

**Note:** For a detailed description of the data, please refer to the section below.
 
 
## Data Description  
This drug information is in the `Data/` folder.  

**drug_name.txt**: Drugbank id for all drugs. 
**drug_name_708.txt**: Drugbank id for all drugs.    
**gold_combination.txt**: Our Gold Standard Drug Combination Dataset.    
**Atc_ori.txt**: Similarity of drug pairs calculated from drug pathway feature.   
**Chemical_ori.txt**: Similarity of drug pairs calculated from drug atc feature.   
**Drug_drug_ori.txt**: Similarity of drug pairs calculated from drug chemical structure feature.   
**Sider_ori.txt**: Similarity of drug pairs calculated from drug adverse feature.   
**Target_ori.txt**: Similarity of drug pairs calculated from drug target feature.   
**mat_drug_disease.txt**: Similarity of drug pairs calculated from drug target feature.   
**Sim_mat_drug_disease.txt**: Similarity of drug pairs calculated from drug target feature. 


## Citation


### Contacts
If you have any questions,contact the maintainer of this package: HG_Chen chenhg25@mail2.sysu.edu.cn


