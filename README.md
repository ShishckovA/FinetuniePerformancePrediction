# Predicting finetune quality using TDA

A repository for research paper "Predicting finetune quality using TDA". Here we calculate some features about model.

There are two main feature types: 

1. Probing results. Probing results are calculated using run_senteval.ipynb
2. Topological data of attention features. This is collected using calculate_TDA_features.ipynb.

To collect data (find models that achieve vatient quality on target dataset), we use tangle_model_on_scrambled_wikipedia.ipynb. This notebook finetunes base model on scrambled Wikipedia, gradually decreasing quality of the model.

Final regressor is built in final_regressor.ipynb, where you can inspect quality benifit from TDA.
