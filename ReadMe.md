# Movie Reviews Using Simple RNN

1. Use the IMDB dataset nothing but an reviews in text format.
2. Will convert the reviews into Positive/Negative output using simple RNN.

```Reviews Dataset -> Feature Transformation -> Simple RNN -> Store model into .h5 -> Strimlit Web App -> Deployment```

## Simple RNN
It has 2 components
a) Embedding Layer -> Convert word intot vectors
b) Simple RNN

### Embedding Layer
It's a technique to convert word into vectors.

#### OneHotEncoding
If we have a word i.e. `man` & we've vocabulary i.e. |v| then that word will be coverted into of size 10000. In which only one of cell will have value as `1`.

|v| = 10000 
** Example:
 [1304, 3033, 7156, 249] -> 'the glass of tea'
 [1304, 3033, 7156, 3172]   -> 'the glass of juice'

#### Word Embedding [word2vec]

For instance, consider the word "tasty." Using Word2Vec, the word "tasty" might be represented as a vector like (0.5, 0.2, 0.8) in three dimensions. This representation maintains relationships with other words based on context.

eg.

##### Details:

###### Functionality: 
Word2Vec captures semantic meanings of words by positioning similar words closer together in the vector space.
###### Practical Use: 
The model analyzes surrounding words in texts (context) to create these vectors, allowing for a deeper understanding of linguistic relationships, such as synonyms or antonyms.


# Notes
1. You can use free powerful machine such as Google Colab.
    - To create the model.
2. Keep two points going through the projects
    - Vector size will be 10000.
    - Feature Dimensions will be 300.


