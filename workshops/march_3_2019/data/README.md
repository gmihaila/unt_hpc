# Prep Data

All files generated here are using the **data/data_prep.ipynb** Colab Notebook:
  * Prep data from `tensorflow_datasets` of **imdb_reviews** dataset.
  * Prep data from [The Signal Media One-Million News Articles Dataset](https://research.signal-ai.com/newsir16/signal-dataset.html).

  <a target="_blank"   href="https://colab.research.google.com/github/gmihaila/gtc2020_instructor_training/blob/master/data/data_prep.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" /> Run data_prep.ipynb in Google Colab</a>


## Files:

  * **data/mdb_reviews_subwords8k_text_features.pickle** contains the text encoder - decoder binary file of type `info.features['text'].encoder` from `tensorflow_datasets`
    ```python
    (train_data, test_data), info = tfds.load('imdb_reviews/subwords8k', 
                                          split = (tfds.Split.TRAIN, tfds.Split.TEST),
                                          as_supervised=True,
                                          with_info=True)

    text_features = info.features['text'].encoder
    ```
  * **data/imdb_reviews_50k.csv** contains all movie revies and their sentiments:
  
    | review                                            	| sentiment 	|
    |---------------------------------------------------	|-----------	|
    | This was an absolutely terrible movie. Don't b... 	| 0         	|
    | I have been known to fall asleep during films,... 	| 0         	|
    
  * **data/movies_reviews_embeddings_part1.npy** and **data/movies_reviews_embeddings_part2.npy** contain BERT Embeddings of all `50,000` movie revies. They are saved in numpy format binary. 
   They are the output of running `SentenceTransformer` on all the text using `bert-base-nli-mean-tokens` pretrained model:
   ```python
   name_of_model='bert-base-nli-mean-tokens'
   batch_size=1000
   use_device="cuda"

   embed_model = SentenceTransformer(model_name_or_path=name_of_model,
                                       device=torch.device(use_device))

   movies_reviews_embeddings = embed_model.encode(sentences=reviews_texts, 
                                                 batch_size=batch_size, 
                                                 show_progress_bar=True)

   movies_reviews_embeddings = np.array(movies_reviews_embeddings)
   ```
   In order to load them:
   ```python
   movies_reviews_embeddings_part1 = np.load('movies_reviews_embeddings_part1.npy')
   movies_reviews_embeddings_part2 = np.load('movies_reviews_embeddings_part2.npy')

   movies_reviews_embeddings = np.concatenate((movies_reviews_embeddings_part1, movies_reviews_embeddings_part2))
   ```
